import os
import uuid

import json
from flask import Flask
from multiinstance.listing import InstanceListing, VersionListing
from multiinstance.models import Instance, OpenSlidesVersion

import jsonapi.flask
from jsonapi.base.schema import Schema

instance_meta_dir = '/home/ab/git/openslides_ansible/tmp/meta'
versions_meta_dir = '/home/ab/git/openslides_ansible/tmp/meta'


class Database(jsonapi.base.database.Database):
    def session(self):
        return Session(self.api)


class Session(jsonapi.base.database.Session):
    def __init__(self, *args, **kwargs):
        super(Session, self).__init__(*args, **kwargs)
        self.instances = InstanceListing(instance_meta_dir)

    def query_size(self, typename, *, sorting=None, limit=None, offset=None, filters=None):
        pass

    def commit(self):
        pass

    def delete(self, resources):
        pass

    def save(self, resources):
        for resource in resources:
            if isinstance(resource, Instance):
                instance_id = uuid.uuid4().__str__()
                resource.data['id'] = instance_id
                f = open(os.path.join(instance_meta_dir, "openslides_instance_" + instance_id + '.json'), "w")
                f.write(json.dumps(resource.data, indent=4))
                f.close()

    def get(self, identifier, required=False):
        pass

    def query(self, typename, *, sorting=None, limit=None, offset=None, filters=None, order=None):
        if typename == 'instances':
            return self.instances.get()
        elif typename == 'openslides-versions':
            return VersionListing(versions_meta_dir).get()
        pass

    def get_many(self, identifiers, required=False):
        events = [self.instances.get_event(i) for i in identifiers]
        return dict([(event.id, event) for event in events if event is not None])


app = Flask(__name__)

api = jsonapi.flask.FlaskAPI("/api", db=Database(), flask_app=app)

api.add_type(Schema(Instance, typename='instances'))
api.add_type(Schema(OpenSlidesVersion, typename='openslides-versions'))

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
