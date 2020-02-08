import connexion
import six
import decimal
import sqlite3

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.car import Car  # noqa: E501
from swagger_server.models.car_detail import CarDetail  # noqa: E501
from swagger_server.models.car_update import CarUpdate  # noqa: E501
from swagger_server import util

from ..db import get_db
from .util import api_base_url


SQL_INF = '9e999'


def add_car(garage_id, car):  # noqa: E501
    """add a car to a garage

     # noqa: E501

    :param garage_id: id of garage in which to parc the car
    :type garage_id: int
    :param body: car to create
    :type body: dict | bytes

    :rtype: CarDetail
    """
    carDetail = CarDetail.from_dict(car)

    # added input validation - this should go into the model code
    # but the framework does not catch and wrap errors other than
    # can be expected from the yaml specification
    try:
        decimal.Decimal(carDetail.price)
    except decimal.InvalidOperation:
        return ApiResponse(code=604, type='error', message='invalid input, price must be decimal'), 400

    try:
        with get_db() as con:
            cursor = con.cursor()

            # TODO: verify isolation level
            # this calls for a transaction:
            # - insert the car (optimistically)
            # - then check garage capacity to eventually rollback
            cursor.execute('BEGIN TRANSACTION')

            check_stmt = '''
                select g.max_capacity, count(c.id) as no_cars
                from garage as g left join car as c
                on g.id = c.garage_id
                where g.id = ?
                group by g.id
            '''
            check_args = (garage_id,)
            check_record = cursor.execute(check_stmt, check_args).fetchone()

            # garage not found
            if check_record is None:
                return ApiResponse(code=602, type='error', message='cannot find garage {}'.format(garage_id)), 400

            from pprint import pprint
            pprint({ key: check_record[key] for key in check_record.keys() })

            # garage already full
            if check_record['no_cars'] > check_record['max_capacity']:
                return ApiResponse(code=603, type='error', message='garage {} is already full'.format(garage_id)), 400

            create_stmt = '''
                insert into car (registration, brand, model, price, garage_id)
                values (?, ?, ?, ? ,?);
            '''
            create_args = (carDetail.registration,
                           carDetail.brand,
                           carDetail.model,
                           carDetail.price,
                           garage_id
                           )

            cursor.execute(create_stmt, create_args)
            cursor.execute('END TRANSACTION')
            
            carDetail.id = cursor.lastrowid

            return carDetail, 201, { 'Location': '{}/garages/{}/cars/{}'.format(api_base_url(), garage_id, carDetail.id) }

    except sqlite3.IntegrityError as err:
        msg, = err.args

        if 'UNIQUE' in msg:
            return ApiResponse(code=601, type='error', message='car registration already exists'), 400
        elif 'FOREIGN KEY' in msg:
            return ApiResponse(code=602, type='error', message='cannot find garage {}'.format(garage_id)), 400
        

def empty_garage(garage_id):  # noqa: E501
    """remove all cars from a garage

     # noqa: E501

    :param garage_id: id of garage in which to parc the car
    :type garage_id: int

    :rtype: None
    """
    with get_db() as con:
        cur = con.execute('delete from car where garage_id = ?', (garage_id,))
        
        if cur.rowcount < 1:
            return ApiResponse(code=404, type='error', message='cannot find garage {}'.format(garage_id)), 404


def get_car(garage_id, car_id):  # noqa: E501
    """get car details

     # noqa: E501

    :param garage_id: id of garage
    :type garage_id: int
    :param car_id: id of car
    :type car_id: int

    :rtype: CarDetail
    """

    stmt = 'select * from car as c where c.id = ? and c.garage_id = ?'
    args = (car_id, garage_id)
    record = get_db().execute(stmt, args).fetchone()

    if record is None:
        return ApiResponse(code=404, type='error', message='cannot find car {} in garage {}'.format(car_id, garage_id)), 404

    dikt = { key: record[key] for key in record.keys() }
    dikt['garage'] = '{}/garages/{}'.format(api_base_url(), garage_id)
    
    return CarDetail.from_dict(dikt)


def get_cars(garage_id, min_price=0, max_price=SQL_INF):  # noqa: E501
    """get all cars of a garage

     # noqa: E501

    :param garage_id: id of garage in which to parc the car
    :type garage_id: int
    :param min_price: minimum inclusive price
    :type min_price: str
    :param max_price: maximum inclusive price
    :type max_price: str

    :rtype: List[Car]
    """

    try:
        decimal.Decimal(min_price)
        decimal.Decimal(max_price)
    except decimal.InvalidOperation:
        return ApiResponse(code=605, type='error', message='invalid input, min_ and max_price must be decimal')

    stmt = '''
        select id, registration, brand, model, price
        from car as c
        where c.garage_id = ? and c.price >= ? and c.price <= ?
    '''
    args = (garage_id, min_price, max_price)

    records = get_db().execute(stmt, args).fetchall()

    return [Car.from_dict({ key: record[key] for key in record.keys() })
            for record in records]


def remove_car(garage_id, car_id):  # noqa: E501
    """remove car from garage

     # noqa: E501

    :param garage_id: id of garage
    :type garage_id: int
    :param car_id: id of car
    :type car_id: int

    :rtype: None
    """
    
    with get_db() as con:
        cur = con.execute('''
            delete from car where id = ? and garage_id = ?
        ''', (car_id, garage_id))

        if cur.rowcount < 1:
            return ApiResponse(code=404, type='error', message='cannot find car {} in garage {}'.format(car_id, garage_id)), 404


def update_car_registration(garage_id, car_id, car_update):  # noqa: E501
    """update existing car registration

     # noqa: E501

    :param garage_id: id of garage
    :type garage_id: int
    :param car_id: id of car
    :type car_id: int
    :param body: new car registration
    :type body: dict | bytes

    :rtype: None
    """
    upd = CarUpdate.from_dict(car_update)

    try:
        with get_db() as con:
            cur = con.execute('''
                update car set registration = ? where id = ? and garage_id = ?
            ''', (upd.registration, car_id, garage_id))

            if cur.rowcount < 1:
                return ApiResponse(code=404, type='error', message='cannot find car {} in garage {}'.format(car_id, garage_id)), 404

    except sqlite3.IntegrityError as err:
        msg, = err.args

        if 'UNIQUE' in msg:
            return ApiResponse(code=600, type='error', message='registration {} is already taken'.format(upd.registration)), 400
