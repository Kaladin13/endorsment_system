from flask import Flask

from controllers.projects import projects_, recommend_users
from models.models import db

app = Flask(__name__)

app.config.from_pyfile('config/db.py')

db.init_app(app)


@app.route('/projects/<project_id>')
def projects(project_id):
    return projects_(project_id)


@app.route('/projects/<project_uuid>/recommend-users')
def recc_projects(project_uuid):
    return recommend_users(project_uuid)


if __name__ == '__main__':
    app.run()
