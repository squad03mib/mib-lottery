from swagger_server import db


class Lottery(db.Model):
    """Representation of Lottery model."""

    # The name of the table that we explicitly set
    __tablename__ = 'Lottery'

    # A list of fields to be serialized
    SERIALIZE_LIST = ['id', 'points', 'trials']

    # All fields of user
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer)
    points = db.Column(db.Integer, default=0)
    trials = db.Column(db.Integer, default=0)

    def __init__(self, *args, **kw):
        super(Lottery, self).__init__(*args, **kw)

    def set_points(self, points):
        self.points = points

    def set_trials(self, trials):
        self.trials = trials

    def serialize(self):
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
