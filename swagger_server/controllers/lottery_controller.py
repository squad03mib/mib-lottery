import connexion
import six

from swagger_server.models.lottery_info import LotteryInfo  # noqa: E501
from swagger_server import util


def mib_resources_users_get_lottery_info(user_id):  # noqa: E501
    """mib_resources_users_get_lottery_info

    Get earned points and trials left # noqa: E501

    :param user_id: User Unique ID
    :type user_id: int

    :rtype: LotteryInfo
    """
    return 'do some magic!'


def mib_resources_users_spin_roulette(user_id):  # noqa: E501
    """Spin the roulette to earn points

     # noqa: E501

    :param user_id: User Unique ID
    :type user_id: int

    :rtype: LotteryInfo
    """
    return 'do some magic!'
