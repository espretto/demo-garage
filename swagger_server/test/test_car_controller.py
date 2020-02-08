# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.car import Car  # noqa: E501
from swagger_server.models.car_update import CarUpdate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCarController(BaseTestCase):
    """CarController integration test stubs"""

    def test_add_car(self):
        """Test case for add_car

        add a car to a garage
        """
        car = Car()
        response = self.client.open(
            '/espretto/garagiste/1.0.0/garages/{garage_id}/cars'.format(garage_id=789),
            method='POST',
            data=json.dumps(car),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_empty_garage(self):
        """Test case for empty_garage

        remove all cars from a garage
        """
        response = self.client.open(
            '/espretto/garagiste/1.0.0/garages/{garage_id}/cars'.format(garage_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_car(self):
        """Test case for get_car

        get car details
        """
        response = self.client.open(
            '/espretto/garagiste/1.0.0/garages/{garage_id}/cars/{car_id}'.format(garage_id=789, car_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cars(self):
        """Test case for get_cars

        get all cars of a garage
        """
        query_string = [('min_price', '0'),
                        ('max_price', 'infinity')]
        response = self.client.open(
            '/espretto/garagiste/1.0.0/garages/{garage_id}/cars'.format(garage_id=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_car(self):
        """Test case for remove_car

        remove car from garage
        """
        response = self.client.open(
            '/espretto/garagiste/1.0.0/garages/{garage_id}/cars/{car_id}'.format(garage_id=789, car_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_car_registration(self):
        """Test case for update_car_registration

        update existing car registration
        """
        car_update = CarUpdate()
        response = self.client.open(
            '/espretto/garagiste/1.0.0/garages/{garage_id}/cars/{car_id}'.format(garage_id=789, car_id=789),
            method='PUT',
            data=json.dumps(car_update),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
