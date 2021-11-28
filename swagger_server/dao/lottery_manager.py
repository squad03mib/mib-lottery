from swagger_server.dao.manager import Manager
from swagger_server.models_db.lottery import Lottery


class LotteryManager(Manager):

    @staticmethod
    def create_lottery(lottery: Lottery):
        Manager.create(lottery=lottery)

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Lottery.query.get(id_)

    @staticmethod
    def retrieve_by_id_user(id_user_):
        Manager.check_none(id_user=id_user_)
        return Lottery.query.filter(Lottery.id_user == id_user_).first()

    @staticmethod
    def update_lottery(lottery: Lottery):
        Manager.update(lottery=lottery)
