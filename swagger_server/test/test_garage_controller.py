# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.garage import Garage  # noqa: E501
from swagger_server.models.garage_detail import GarageDetail  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGarageController(BaseTestCase):
    """GarageController integration test stubs"""

    def test_add_garage(self):
        """Test case for add_garage

        create a new garage
        """
        garage = Garage()
        response = self.client.open(
            '/espretto/garagiste/1.0.0/garages',
            method='POST',
            data=json.dumps(garage),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_garage(self):
        """Test case for get_garage

        get the details of an existing garage
        """
        response = self.client.open(
            '/espretto/garagiste/1.0.0/garages/{garage_id}'.format(garage_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_purge_garage(self):
        """Test case for purge_garage

        delete an existing garage and all of its cars
        """
        response = self.client.open(
            '/espretto/garagiste/1.0.0/garages/{garage_id}'.format(garage_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
