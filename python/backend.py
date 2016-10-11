import copy
import os
import uuid
import json
from datetime import datetime
from time import strftime

from flask import Flask
from multiinstance.listing import InstanceListing, VersionListing
from multiinstance.models import Instance, Version
import jsonapi.flask
from jsonapi.base.schema import Schema
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--instance-meta-dir", dest="instance_meta_dir",
                  help="directory containing instance meta files", metavar="INSTANCE_META_DIR")
parser.add_option("--versions-meta-dir", dest="versions_meta_dir",
                  help="directory containing version meta files",
                  metavar="VERSIONS_META_DIR")

(options, args) = parser.parse_args()

instance_meta_dir = options.instance_meta_dir
versions_meta_dir = options.versions_meta_dir


class Database(jsonapi.base.database.Database):
    def session(self):
        return Session(self.api)


class Session(jsonapi.base.database.Session):
    def __init__(self, *args, **kwargs):
        super(Session, self).__init__(*args, **kwargs)
        self.instances = InstanceListing(instance_meta_dir)
        self.versions = VersionListing(versions_meta_dir)

    def query_size(self, typename, *, sorting=None, limit=None, offset=None, filters=None):
        pass

    def commit(self):
        pass

    def delete(self, resources):
        pass

    def save(self, resources):
        for resource in resources:
            if isinstance(resource, Instance):
                now = datetime.now()
                instance_id = uuid.uuid4().__str__()
                journal_file = os.path.join(instance_meta_dir, "openslides_instance.journal")
                if os.path.isfile(journal_file):
                    with open(journal_file, 'rb') as fh:
                        last = fh.readlines()[-1].decode()
                        last_number = int(last.split(';')[0])
                else:
                    last_number = 0

                number = last_number + 1
                with open(journal_file, 'a') as fh:
                    fh.write(str(number) + ';' + instance_id + "\n")

                resource.data['id'] = instance_id
                f = open(os.path.join(instance_meta_dir, "openslides_instance_" + instance_id + '.json'), "w")
                data = copy.copy(resource.data)
                data['osversion'] = data['osversion'].data['id']
                data['number'] = number
                data['created_date'] = now.strftime('%Y-%m-%d')
                f.write(json.dumps(data, indent=4))
                f.close()

    def get(self, identifier, required=False):
        if identifier[0] == 'version':
            return self.versions.get_by_id(identifier[1])
        pass

    def query(self, typename, *, sorting=None, limit=None, offset=None, filters=None, order=None):
        if typename == 'instances':
            return self.instances.get()
        elif typename == 'versions':
            return VersionListing(versions_meta_dir).get()
        pass

    def get_many(self, identifiers, required=False):
        objs = [self.get(identifier, required) for identifier in identifiers]
        return dict([((obj.type, obj.data['id']), obj) for obj in objs if obj is not None])


app = Flask(__name__)

api = jsonapi.flask.FlaskAPI("/api", db=Database(), flask_app=app)

api.add_type(Schema(Instance, typename='instances'))
api.add_type(Schema(Version, typename='versions'))

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
