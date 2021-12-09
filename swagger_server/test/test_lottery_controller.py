# coding: utf-8

from __future__ import absolute_import
from swagger_server.test import BaseTestCase
from swagger_server.models.points import Points
import json


class TestLotteryController(BaseTestCase):
    """LotteryController integration test stubs"""

    def test_mib_resources_users_spin_roulette(self):
        """Test case for mib_resources_users_spin_roulette

        Spin the roulette to earn points
        """
        response = self.client.open(
            '/users/{user_id}/lottery'.format(user_id=1),
            method='POST')
        assert response.status_code == 201

        response = self.client.open(
            '/users/{user_id}/lottery'.format(user_id=1),
            method='POST')
        assert response.status_code == 201

    def test_mib_resources_users_get_lottery_info(self):
        """Test case for mib_resources_users_get_lottery_info


        """
        response = self.client.open(
            '/users/{user_id}/lottery'.format(user_id=1),
            method='GET')
        assert response.status_code == 200

        response = self.client.open(
            '/users/{user_id}/lottery'.format(user_id=-1),
            method='GET')
        assert response.status_code == 404

    def test_mib_resources_users_use_lottery_points(self):
        """Test case for     def test_mib_resources_users_use_lottery_points


        """
        body = Points()
        body.count = 5
        response = self.client.open(
            '/users/{user_id}/lottery/use'.format(user_id=1),
            method='POST',
            data=json.dumps(body.to_dict()),
            content_type='application/json')
        assert response.status_code == 201


