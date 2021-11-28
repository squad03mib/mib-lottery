import connexion
import six
import datetime
from swagger_server.models_db.user import User  # noqa: E501
from swagger_server import util
from swagger_server.dao.user_manager import UserManager


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

    user = User()
    body = connexion.request.get_json()
    user.set_email(body.email)
    user.set_password(body.password)
    user.set_first_name(body.firstname)
    user.set_last_name(body.lastname)
    UserManager.create_user(user)

    response_object = {
        'user': user.serialize(),
        'status': 'success',
        'message': 'Successfully registered',
    }

    return response_object
