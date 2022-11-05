import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Project(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(sa.String)
    name = sa.Column(sa.String)

    lineups = db.relationship('Lineup', backref='project', lazy='select')

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'uuid': self.uuid,
            'name': self.name,
            'lineups': [lp.serialize for lp in self.lineups]
        }


class Lineup(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(sa.String)
    team_uuid = sa.Column(sa.String)
    role_uuid = sa.Column(sa.String, sa.ForeignKey('role.uuid'), nullable=False)
    profile_uuid = sa.Column(sa.String)
    project_uuid = sa.Column(sa.String, sa.ForeignKey('project.uuid'), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'uuid': self.uuid,
            'team_uuid': self.team_uuid,
            'role_uuid': self.role_uuid,
            'profile_uuid': self.profile_uuid,
            'project_uuid': self.project_uuid
        }


class Role(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(sa.String)
    name = sa.Column(sa.String)
    specialization_uuid = sa.Column(sa.String, sa.ForeignKey('specialization.uuid'), nullable=False)

    lineups = db.relationship('Lineup', backref='role', lazy='select')

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'uuid': self.uuid,
            'name': self.name,
            'lineups': [lp.serialize for lp in self.lineups]
        }


class Specialization(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(sa.String)
    name = sa.Column(sa.String)
    value = sa.Column(sa.String)

    roles = db.relationship('Role', backref='specialization', lazy='select')

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'uuid': self.uuid,
            'name': self.name,
            'value': self.value,
            'roles': [lp.serialize for lp in self.roles]
        }


class Profile(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    user_uuid = sa.Column(sa.String)
    specialization_uuid = sa.Column(sa.String)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_uuid': self.user_uuid,
            'specialization_uuid': self.specialization_uuid
        }
