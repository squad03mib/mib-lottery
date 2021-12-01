from datetime import date
from swagger_server.test import BaseTestCase
from swagger_server.background import increase_trials


class TestApp(BaseTestCase):

    def test_increase(self):
        response = self.client.open(
            '/users/{user_id}/lottery'.format(user_id=1),
            method='POST')
        assert response.status_code == 201

        increase_trials.apply()

        response = self.client.open(
            '/users/{user_id}/lottery'.format(user_id=1),
            method='POST')
        assert response.status_code == 201
