import jsonapi.flask
from flask import Flask
from jsonapi.base.schema import Schema
from pip._vendor.distlib.resources import ResourceBase


class Database(jsonapi.base.database.Database):

    def session(self):
        return Session(self.api)


class Session(jsonapi.base.database.Session):

    def query_size(self, typename,
        *, sorting=None, limit=None, offset=None, filters=None
        ):
        pass

    def commit(self):
        pass

    def delete(self, resources):
        pass

    def save(self, resources):
        pass

    def get(self, identifier, required=False):
        pass

    def query(self, typename, *, sorting=None, limit=None, offset=None, filters=None, order=None):
        if isinstance()

    def get_many(self, identifiers, required=False):
        pass

app = Flask(__name__)

api = jsonapi.flask.FlaskAPI("/api", db=Database(), flask_app=app)

class Instance:
    pass

schema = Schema(Instance, typename='instances')
api.add_type(schema)

instance_meta_dir = '/tmp/meta'

# @app.route("/instances")
# def instances():
#     result = []
#     for instance in InstanceListing(instance_meta_dir).get():
#         instance['type'] = "instance"
#         result.append(instance)
#
#     return jsonify({
#         data: result
#     })

if __name__ == "__main__":
    app.run()
