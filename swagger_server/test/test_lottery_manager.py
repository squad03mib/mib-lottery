from __future__ import absolute_import
from swagger_server.test import BaseTestCase


class TestLotteryManager(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestLotteryManager, cls).setUpClass()
        from .test_lottery import TestLottery
        cls.test_lottery = TestLottery
        from swagger_server.dao import lottery_manager
        cls.lottery_manager = lottery_manager.LotteryManager

    def test_crud(self):
        for _ in range(0, 10):
            lottery = self.test_lottery.generate_random_lottery()
            self.lottery_manager.create_lottery(lottery=lottery)
            lottery1 = self.lottery_manager.retrieve_by_id(lottery.id)
            self.test_lottery.assertLotteryEquals(lottery, lottery)
            lottery.points = 10
            lottery.trials = 5
            self.lottery_manager.update_lottery(lottery=lottery)
            lottery1 = self.lottery_manager.retrieve_by_id(lottery.id)
            self.test_lottery.assertLotteryEquals(lottery1, lottery)
