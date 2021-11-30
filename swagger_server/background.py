from celery import Celery
from datetime import timedelta
BACKEND = BROKER = 'redis://redis:6379'
celery = Celery(__name__, backend=BACKEND, broker=BROKER)


@celery.on_after_configure.connect
def setup_periodic_task(sender, **kwargs):
    sender.add_periodic_task(timedelta(seconds=5),
                             increase_trials, expires=10)


@celery.task
def increase_trials():
    from swagger_server import create_app
    app = create_app()
    from swagger_server.dao.lottery_manager import LotteryManager

    LotteryManager.update_trials()
