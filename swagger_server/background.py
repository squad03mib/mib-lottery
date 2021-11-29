from celery import Celery
from swagger_server.dao.lottery_manager import LotteryManager
from swagger_server import db
from datetime import timedelta

BACKEND = BROKER = 'redis://localhost:6379'
celery = Celery(__name__, backend=BACKEND, broker=BROKER)


@celery.on_after_configure.connect
def setup_periodic_task(sender, **kwargs):
    sender.add_periodic_task(timedelta(seconds=30),
                             increase_trials, expires=10)


@celery.task
def increase_trials():
    from swagger_server import create_app
    app = create_app()
    db.init_app(app)

    with app.app_context():
        LotteryManager.update_trials()
