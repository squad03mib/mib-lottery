import connexion
import six
import datetime
from swagger_server.models_db.lottery import Lottery  # noqa: E501
from swagger_server.models.lottery_info import LotteryInfo
from swagger_server import util
from swagger_server.dao.lottery_manager import LotteryManager
from flask import jsonify


def mib_resources_users_get_lottery_info(user_id):  # noqa: E501
    """mib_resources_users_get_lottery_info

    Get earned points and trials left # noqa: E501

    :param user_id: User Unique ID
    :type user_id: int

    :rtype: LotteryInfo
    """
    lottery = LotteryManager.retrieve_by_id_user(user_id)

    return jsonify(lottery.serialize())


def mib_resources_users_spin_roulette(user_id):  # noqa: E501
    """Spin the roulette to earn points

     # noqa: E501

    :param user_id: User Unique ID
    :type user_id: int

    :rtype: LotteryInfo
    """

    lottery = LotteryManager.retrieve_by_id_user(user_id)

    lottery_ = Lottery()

    if lottery is None:
        lottery_.id_user = user_id
        lottery_.points = 10
        lottery_.trials = 1
        LotteryManager.create_lottery(lottery_)
    else:
        lottery.id_user = user_id
        lottery.points = lottery.points + 10
        lottery.trials = lottery.trials - 1
        LotteryManager.update(lottery)

    return {'msg': 'OK'}
