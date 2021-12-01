from __future__ import absolute_import
from swagger_server.test import BaseTestCase
import unittest
from random import SystemRandom

rand = SystemRandom()


class TestLottery(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestLottery, cls).setUpClass()

        from swagger_server.models_db import lottery
        cls.lottery = lottery

    @staticmethod
    def assertLotteryEquals(value, expected):
        t = unittest.FunctionTestCase(TestLottery)
        t.assertEqual(value.id, expected.id)
        t.assertEqual(value.id_user, expected.id_user)
        t.assertEqual(value.points, expected.points)
        t.assertEqual(value.trials, expected.trials)

    @staticmethod
    def generate_random_lottery():

        id_user = rand.randrange(0, 100)
        points = rand.choice([10, 20, 40, 80])
        trials = rand.randrange(1, 50)

        from swagger_server.models_db.lottery import Lottery

        lottery = Lottery(
            id_user=id_user,
            points=points,
            trials=trials
        )

        return lottery

    @staticmethod
    def test_id():
        lottery = TestLottery.generate_random_lottery()
        id_lottery = lottery.get_id()

        new_id_lottery = rand.randrange(0, 100)
        lottery.set_id(new_id_lottery)

        assert new_id_lottery == lottery.id

    @staticmethod
    def test_id_user():
        lottery = TestLottery.generate_random_lottery()
        id_user = lottery.get_id_user()

        new_id_user = rand.randrange(0, 100)
        lottery.set_id_user(new_id_user)

        assert new_id_user == lottery.id_user

    @staticmethod
    def test_points():
        lottery = TestLottery.generate_random_lottery()
        points = lottery.get_points()

        new_points = rand.choice([10, 20, 40, 80])
        lottery.set_points(new_points)

        assert new_points == lottery.points

    @staticmethod
    def test_trials():
        lottery = TestLottery.generate_random_lottery()
        trials = lottery.get_trials()

        new_trials = rand.randrange(1, 50)
        lottery.set_trials(new_trials)

        assert new_trials == lottery.trials
