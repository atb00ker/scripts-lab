from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FlaskModel(db.Model):
    __tablename__ = "flask"

    id = db.Column(db.Integer, primary_key=True)
    flask_name = db.Column(db.String())

    def __init__(self, flask_name):
        self.flask_name = flask_name

    def __repr__(self):
        return f"{self.flask_name}"

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return {
            'id': self.id,
            'flask_name': self.flask_name,
        }
