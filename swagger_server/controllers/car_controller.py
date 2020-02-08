import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.car import Car  # noqa: E501
from swagger_server.models.car_update import CarUpdate  # noqa: E501
from swagger_server import util


def add_car(garage_id, car):  # noqa: E501
    """add a car to a garage

     # noqa: E501

    :param garage_id: id of garage in which to parc the car
    :type garage_id: int
    :param car: car to create
    :type car: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        car = Car.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def empty_garage(garage_id):  # noqa: E501
    """remove all cars from a garage

     # noqa: E501

    :param garage_id: id of garage to empty
    :type garage_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_car(garage_id, car_id):  # noqa: E501
    """get car details

     # noqa: E501

    :param garage_id: id of garage
    :type garage_id: int
    :param car_id: id of car
    :type car_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_cars(garage_id, min_price=None, max_price=None):  # noqa: E501
    """get all cars of a garage

     # noqa: E501

    :param garage_id: id of garage
    :type garage_id: int
    :param min_price: minimum inclusive price
    :type min_price: str
    :param max_price: maximum inclusive price
    :type max_price: str

    :rtype: List[Car]
    """
    return 'do some magic!'


def remove_car(garage_id, car_id):  # noqa: E501
    """remove car from garage

     # noqa: E501

    :param garage_id: id of garage
    :type garage_id: int
    :param car_id: id of car
    :type car_id: int

    :rtype: None
    """
    return 'do some magic!'


def update_car_registration(garage_id, car_id, car_update):  # noqa: E501
    """update existing car registration

     # noqa: E501

    :param garage_id: id of garage
    :type garage_id: int
    :param car_id: id of car
    :type car_id: int
    :param car_update: new car registration
    :type car_update: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        car_update = CarUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
