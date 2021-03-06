# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401
import re
from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CarDetail(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, registration: str=None, brand: str=None, model: str=None, price: str=None, garage: str=None):  # noqa: E501
        """CarDetail - a model defined in Swagger

        :param id: The id of this CarDetail.  # noqa: E501
        :type id: int
        :param registration: The registration of this CarDetail.  # noqa: E501
        :type registration: str
        :param brand: The brand of this CarDetail.  # noqa: E501
        :type brand: str
        :param model: The model of this CarDetail.  # noqa: E501
        :type model: str
        :param price: The price of this CarDetail.  # noqa: E501
        :type price: str
        :param garage: The garage of this CarDetail.  # noqa: E501
        :type garage: str
        """
        self.swagger_types = {
            'id': int,
            'registration': str,
            'brand': str,
            'model': str,
            'price': str,
            'garage': str
        }

        self.attribute_map = {
            'id': 'id',
            'registration': 'registration',
            'brand': 'brand',
            'model': 'model',
            'price': 'price',
            'garage': 'garage'
        }

        self._id = id
        self._registration = registration
        self._brand = brand
        self._model = model
        self._price = price
        self._garage = garage

    @classmethod
    def from_dict(cls, dikt) -> 'CarDetail':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CarDetail of this CarDetail.  # noqa: E501
        :rtype: CarDetail
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this CarDetail.


        :return: The id of this CarDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this CarDetail.


        :param id: The id of this CarDetail.
        :type id: int
        """

        self._id = id

    @property
    def registration(self) -> str:
        """Gets the registration of this CarDetail.


        :return: The registration of this CarDetail.
        :rtype: str
        """
        return self._registration

    @registration.setter
    def registration(self, registration: str):
        """Sets the registration of this CarDetail.


        :param registration: The registration of this CarDetail.
        :type registration: str
        """
        if registration is None:
            raise ValueError("Invalid value for `registration`, must not be `None`")  # noqa: E501
        if registration is not None and not re.search(r'^[A-Z]{2}-\d{3}-[A-Z]{2}$', registration):  # noqa: E501
            raise ValueError("Invalid value for `registration`, must be a follow pattern or equal to `/^[A-Z]{2}-\d{3}-[A-Z]{2}$/`")  # noqa: E501

        self._registration = registration

    @property
    def brand(self) -> str:
        """Gets the brand of this CarDetail.


        :return: The brand of this CarDetail.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand: str):
        """Sets the brand of this CarDetail.


        :param brand: The brand of this CarDetail.
        :type brand: str
        """
        if brand is None:
            raise ValueError("Invalid value for `brand`, must not be `None`")  # noqa: E501

        self._brand = brand

    @property
    def model(self) -> str:
        """Gets the model of this CarDetail.


        :return: The model of this CarDetail.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this CarDetail.


        :param model: The model of this CarDetail.
        :type model: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def price(self) -> str:
        """Gets the price of this CarDetail.


        :return: The price of this CarDetail.
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price: str):
        """Sets the price of this CarDetail.


        :param price: The price of this CarDetail.
        :type price: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def garage(self) -> str:
        """Gets the garage of this CarDetail.


        :return: The garage of this CarDetail.
        :rtype: str
        """
        return self._garage

    @garage.setter
    def garage(self, garage: str):
        """Sets the garage of this CarDetail.


        :param garage: The garage of this CarDetail.
        :type garage: str
        """

        self._garage = garage
