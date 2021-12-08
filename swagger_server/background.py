from celery import Celery
from datetime import timedelta
import celery
from swagger_server import create_app
from os import environ

environ.setdefault('CELERY_CONFIG_MODULE', 'swagger_server.background_config')

celery = Celery(__name__)
celery.config_from_envvar('CELERY_CONFIG_MODULE')
_APP = create_app()


@celery.on_after_configure.connect
def setup_periodic_task(sender, **kwargs):
    sender.add_periodic_task(timedelta(minutes=10),
                             increase_trials, expires=10)


@celery.task
def increase_trials():
    with _APP.app_context():
        from swagger_server.dao.lottery_manager import LotteryManager

        LotteryManager.update_trials()
