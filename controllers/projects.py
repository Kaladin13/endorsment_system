import uuid

from lib.fetch_lineup import fetch_lineup
from lib.get_by_uuid import get_by_uuid
from lib.handlers import bad_request
from models.models import Project
from utils.response_converter import convert_recommend_response


def projects_(project_id):
    try:
        projects_data = Project.query.join(Project.lineups)
        project = [x for x in projects_data if x.id == int(project_id)][0]
        return project.serialize
        # return [pr.serialize for pr in projects_data]
    except Exception as e:
        return bad_request('Error when fetching projects')

def projects_by_user_uud(project_id):
    try:
        projects_data = Project.query.join(Project.lineups)
        project = [x for x in projects_data if x.id == int(project_id)][0]
        return project.serialize
        # return [pr.serialize for pr in projects_data]
    except Exception as e:
        return bad_request('Error when fetching projects')

def recommend_users(project_uuid):
    try:
        projects = Project.query.join(Project.lineups)
        project = get_by_uuid(projects, uuid.UUID(project_uuid))

        response = []

        for lineup in project.lineups:
            [users, specialization_uuid] = fetch_lineup(lineup)
            response.append(convert_recommend_response(users, specialization_uuid, lineup.uuid))

        print(response)
        return response
    except Exception as e:
        print(e)
        return bad_request('Error when recommending users in projects')
