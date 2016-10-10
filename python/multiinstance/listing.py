from .models import Instance, Version
from .utils import get_json_data


class VersionListing:
    def __init__(self, directory):
        self.directory = directory

    def get(self):
        versions = []
        for version_data in get_json_data(self.directory, 'openslides_version_'):
            versions.append(Version(**version_data))

        return versions

    def get_by_id(self, name):
        return next(filter(lambda v: v.data['id'] == name, self.get()), None)

class InstanceListing:
    def __init__(self, directory):
        self.directory = directory

    def get(self):
        instances = []
        for instance_data in get_json_data(self.directory, 'openslides_instance_'):
            instance = Instance(**instance_data)

            instance.data['osversion'] = VersionListing(self.directory).get_by_id(instance.osversion)
            instances.append(instance)
        return instances
