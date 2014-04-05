from flask import Flask, request
from flask.ext import restful
from flask.ext.basicauth import BasicAuth
from flask.ext.restful import reqparse
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from geoalchemy2.types import Geometry
import geojson
import json
import os

app = Flask(__name__)

# Auth
if os.environ.get('BASIC_AUTH_USERNAME'):
    app.config['BASIC_AUTH_USERNAME'] = os.environ['BASIC_AUTH_USERNAME']
    app.config['BASIC_AUTH_PASSWORD'] = os.environ['BASIC_AUTH_PASSWORD']
    app.config['BASIC_AUTH_FORCE'] = True
    basic_auth = BasicAuth(app)
#
# if 'DATABASE_URL' in os.environ:
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'].replace('postgres://', 'postgresql+psycopg2://')
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://titles:password@%s/titles' % os.environ['TITLESDB_1_PORT_5432_TCP'].replace('tcp://', '')
#
# db = SQLAlchemy(app)

api = restful.Api(app)
#
# #Models
# class TitleModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title_number = db.Column( db.String(80) )
#     extent = db.Column(Geometry('POLYGON'))

def validate_geojson_point(data):
    try:
        data = json.loads(data)
        point =  geojson.Point(type=data['type'], coordinates=data['coordinates'])
        return data
    except ValueError:
        raise ValueError

#Resources
class Title(restful.Resource):
    def get(self, title_number):

        restful.abort( 404 )

class TitleList(restful.Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        super(TitleList, self).__init__()

    def get(self):

        result = []

        self.parser.add_argument('near', type=validate_geojson_point, help='A geojson point in space')
        args = self.parser.parse_args()

        if args.get('near', None):
            with open('sample-data.json', 'r') as f:
                result = json.loads(f.read())

        return result

api.add_resource(Title, '/titles/<string:title_number>')
api.add_resource(TitleList, '/titles')
# db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8005, debug=True)
