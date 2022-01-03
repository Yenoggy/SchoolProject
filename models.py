from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String(80), unique=True, nullable=False)
    number = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(800), unique=True, nullable=False)
    img = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<body %r>' % self.body
