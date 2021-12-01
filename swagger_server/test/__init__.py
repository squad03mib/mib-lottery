import unittest


class BaseTestCase(unittest.TestCase):
    """
    This class should be implemented by
    all classes that tests resources
    """
    client = None

    @classmethod
    def setUpClass(cls):
        from swagger_server import create_app
        app = create_app()
        cls.client = app.test_client()

        from .test_lottery import TestLottery
        cls.test_lottery = TestLottery

        from swagger_server.dao.lottery_manager import LotteryManager
        cls.lottery_manager = LotteryManager()
