# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.lottery_info import LotteryInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLotteryController(BaseTestCase):
    """LotteryController integration test stubs"""

    def test_mib_resources_users_get_lottery_info(self):
        """Test case for mib_resources_users_get_lottery_info

        
        """
        response = self.client.open(
            '/users/{user_id}/lottery'.format(user_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mib_resources_users_spin_roulette(self):
        """Test case for mib_resources_users_spin_roulette

        Spin the roulette to earn points
        """
        response = self.client.open(
            '/users/{user_id}/lottery'.format(user_id=789),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
