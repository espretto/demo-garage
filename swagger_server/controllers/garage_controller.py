import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.garage import Garage  # noqa: E501
from swagger_server.models.garage_detail import GarageDetail  # noqa: E501
from swagger_server import util


def add_garage(garage):  # noqa: E501
    """create a new garage

     # noqa: E501

    :param garage: garage to create
    :type garage: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        garage = Garage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_garage(garage_id):  # noqa: E501
    """get the details of an existing garage

     # noqa: E501

    :param garage_id: id of existing garage
    :type garage_id: int

    :rtype: GarageDetail
    """
    return 'do some magic!'


def purge_garage(garage_id):  # noqa: E501
    """delete an existing garage and all of its cars

     # noqa: E501

    :param garage_id: id of existing garage to be purged
    :type garage_id: int

    :rtype: None
    """
    return 'do some magic!'
