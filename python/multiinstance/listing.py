import json
import os


class InstanceListing:
    def __init__(self, directory):
        self.directory = directory

    def get(self):
        instances = []
        for dirname, dirnames, filenames in os.walk(self.directory):
            for filename in filenames:
                if not filename.startswith('openslides_instance_') or not filename.endswith('.json'):
                    continue
                instance_data = json.load(open(os.path.join(dirname, filename), 'r'), encoding='utf-8')
                instances.append(instance_data)
        return instances
