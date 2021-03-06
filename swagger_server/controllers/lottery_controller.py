import connexion
import six

from swagger_server.models.points import Points  # noqa: E501
from swagger_server import util
from swagger_server.models_db.lottery import Lottery  # noqa: E501
from swagger_server.dao.lottery_manager import LotteryManager
from flask import jsonify, abort
from random import SystemRandom


def create_lottery(user_id):

    lottery = Lottery()
    lottery.id_user = user_id
    lottery.points = 0
    lottery.trials = 1
    LotteryManager.create_lottery(lottery)

    return lottery


def mib_resources_users_get_lottery_info(user_id):  # noqa: E501
    """mib_resources_users_get_lottery_info

    Get earned points and trials left # noqa: E501

    :param user_id: User Unique ID
    :type user_id: int

    :rtype: LotteryInfo
    """
    lottery = LotteryManager.retrieve_by_id_user(user_id)

    if lottery is None:
        lottery = create_lottery(user_id)

    return jsonify(lottery.serialize()), 200


def mib_resources_users_spin_roulette(user_id):  # noqa: E501
    """Spin the roulette to earn points

     # noqa: E501

    :param user_id: User Unique ID
    :type user_id: int

    :rtype: LotteryInfo
    """

    lottery = LotteryManager.retrieve_by_id_user(user_id)

    if lottery is None:
        lottery = create_lottery(user_id)
    else:
        if lottery.trials > 0:
            prizes = [10, 20, 40, 80]
            rand = SystemRandom()
            prize = rand.choice(prizes)
            lottery.points = lottery.points + prize
            lottery.trials = lottery.trials - 1
            LotteryManager.update_lottery(lottery)

    return jsonify(lottery.serialize()), 201

def mib_resources_users_use_lottery_points(body, user_id):  # noqa: E501
    """Use lottery points

     # noqa: E501

    :param body: Points to be spent
    :type body: dict | bytes
    :param user_id: User Unique ID
    :type user_id: int

    :rtype: LotteryInfo
    """
    if connexion.request.is_json:
        body :Points = Points.from_dict(connexion.request.get_json())  # noqa: E501

    lottery = LotteryManager.retrieve_by_id_user(user_id)

    if lottery is None:
        abort(404)
    else:
        lottery.points = lottery.points - body.count
        LotteryManager.update_lottery(lottery)

    return jsonify(lottery.serialize()), 201
