from flask import Blueprint, jsonify
from flask_apispec import use_kwargs
from marshmallow import fields

blueprint = Blueprint('tasks', __name__)

@blueprint.route('/api/tasks', methods=('GET',))
@use_kwargs({'fav': fields.Str(), 'limit': fields.Int(), 'offset': fields.Int()})
def get_tasks(fav=None, limit=20, offset=0):
    return 'Hello World'