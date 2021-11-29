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
    trials = db.Column(db.Integer, default=1)

    def __init__(self, *args, **kw):
        super(Lottery, self).__init__(*args, **kw)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_id_user(self):
        return self.id_user

    def set_id_user(self, id_user):
        self.id_user = id_user

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    def get_trials(self):
        return self.trials

    def set_trials(self, trials):
        self.trials = trials

    def serialize(self):
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
