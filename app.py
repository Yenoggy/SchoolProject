from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from models import db, Task
from flask_migrate import Migrate
from markupsafe import escape

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db.app = app
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def main():
    tasks = Task.query.all()
    return render_template('index.html', title='Задачи по физике', tasks=tasks)


if __name__ == '__main__':
    app.run()
