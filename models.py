from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String(80), unique=False, nullable=False)
    number_chapter = db.Column(db.Integer)
    number_task = db.Column(db.Integer)
    body = db.Column(db.String(800), unique=True, nullable=False)
    img = db.Column(db.String(120), unique=True, nullable=False)
    solution = db.Column(db.Text)

    def __repr__(self):
        return '<body %r>' % self.body
