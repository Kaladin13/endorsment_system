from flask import Flask, jsonify
from sqlalchemy.dialects.postgresql import psycopg2
import psycopg2 as postgres

from scripts import recommend
from controllers.projects import projects_, recommend_users
from models.models import db



app = Flask(__name__)
app.config.from_pyfile('config/db.py')
connection = postgres.connect(user="postgres",
                              password="postgres",
                              host="127.0.0.1",
                              port="5432")
db.init_app(app)
#Рекомендация категории на проект
@app.route('/category_name_by_role_uuid/<project_uuid>')
def category_by_project_uuid(project_uuid):
    responce = jsonify(recommend.get_category_by_role(project_uuid, connection))
    responce.headers.add("Access-Control-Allow-Origin", "*")
    return responce

#Рекомендация вакансию на проект
@app.route('/role_by_project_uuid/<project_uuid>')
def role_by_project_uuid(project_uuid):
    responce = jsonify(recommend.get_role_by_project_uuid(project_uuid, connection))
    responce.headers.add("Access-Control-Allow-Origin", "*")
    return responce

#Рекомендация людей на вакансию в проекте
@app.route('/user_uuid_by_project_uuid/<project_uuid>')
def user_uuid_by_project_uuid(project_uuid):
    responce = jsonify(recommend.get_user_uuid_by_project_uuid(project_uuid, connection))
    responce.headers.add("Access-Control-Allow-Origin", "*")
    return responce

#Рекомендация проектов в ленту
@app.route('/projects_by_user_uuid/<user_uuid>')
def projects_by_user_uuid(user_uuid):
    responce = jsonify(recommend.get_projects_by_user_uuid(user_uuid, connection))
    responce.headers.add("Access-Control-Allow-Origin", "*")
    return responce

@app.route('/projects/<project_id>')
def projects(project_id):
    return projects_(project_id)


@app.route('/projects/<project_uuid>/recommend-users')
def recc_projects(project_uuid):
    return recommend_users(project_uuid)

@app.route('/')
def quote():
    return 'We will definitely bang. And more than once. The whole world is in dust. But then.'

if __name__ == '__main__':
    app.run()
