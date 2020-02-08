import connexion
import six
from datetime import datetime

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.garage import Garage  # noqa: E501
from swagger_server.models.garage_detail import GarageDetail  # noqa: E501
from swagger_server import util

from ..db import get_db
from .util import api_base_url


def add_garage(garage):  # noqa: E501
    """create a new garage

     # noqa: E501

    :param body: garage to create
    :type body: dict | bytes

    :rtype: GarageDetail
    """
    garage.setdefault('date_created', datetime.now().isoformat() + 'Z')
    garageDetail = GarageDetail.from_dict(garage)
    
    stmt = '''
        insert into garage (name, address, date_created, max_capacity)
        values (?, ?, ?, ?);
    '''
    args = (garageDetail.name,
            garageDetail.address,
            garageDetail.date_created,
            garageDetail.max_capacity
            )

    with get_db() as con:
        cur = con.execute(stmt, args)

        garageDetail.id = cur.lastrowid
        garageDetail.cars = []

        return garageDetail, 201, { 'Location': '/api/v1.0.0/garages/{}'.format(garageDetail.id) }    


def get_garage(garage_id):  # noqa: E501
    """get the details of an existing garage

     # noqa: E501

    :param garage_id: id of existing garage
    :type garage_id: int

    :rtype: GarageDetail
    """
    
    stmt = '''
        select g.id, name, address, date_created, max_capacity, group_concat(c.id) as cars
        from garage as g left join car as c 
        on g.id = c.garage_id
        where g.id = ?
        group by g.id
    '''
    args = (garage_id,)
    record = get_db().execute(stmt, args).fetchone()

    if record is None:
        return ApiResponse(code=404, type='error', message='cannot find garage {}'.format(garage_id)), 404

    dikt = { key: record[key] for key in record.keys() }

    car_ids = [] if dikt['cars'] is None else dikt['cars'].split(',')
    
    dikt['cars'] = ['{}/garages/{}/cars/{}'.format(api_base_url(), garage_id, car_id)
                    for car_id in car_ids]
    
    return GarageDetail.from_dict(dikt)


def purge_garage(garage_id):  # noqa: E501
    """delete an existing garage and all of its cars

     # noqa: E501

    :param garage_id: id of existing garage to be purged
    :type garage_id: int

    :rtype: None
    """
    
    with get_db() as con:
        # removes associated cars by cascade
        cur = con.execute('delete from garage where id = ?', (garage_id,))
    
        if cur.rowcount < 1:
            return ApiResponse(code=404, type='error', message='cannot find garage {}'.format(garage_id)), 404
