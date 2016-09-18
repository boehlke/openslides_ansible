from .models import Instance, OpenSlidesVersion
from .utils import get_json_data


class VersionListing:
    def __init__(self, directory):
        self.directory = directory

    def get(self):
        versions = []
        for version_data in get_json_data(self.directory, 'openslides_version_'):
            versions.append(OpenSlidesVersion(**version_data))

        return versions

    def get_by_name(self, name):
        return next(filter(lambda v: v.data['name'] == name, self.get()), None)

class InstanceListing:
    def __init__(self, directory):
        self.directory = directory

    def get(self):
        instances = []
        for instance_data in get_json_data(self.directory, 'openslides_instance_'):
            instance = Instance(**instance_data)

            instance.data['osversion'] = VersionListing(self.directory).get_by_name(instance.osversion)
            instances.append(instance)
        return instances
