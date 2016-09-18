from python.multiinstance.schema import ToOneRelationship
from .schema import ObjectIDAttribute, ObjectAttribute, ParentIDAttribute


class SimpleApiObject:
    def __init__(self, *args, **kwargs):
        self.data = kwargs


class OpenSlidesVersion(SimpleApiObject):
    name = ObjectIDAttribute("name")
    image = ObjectAttribute("image")


class Instance(SimpleApiObject):
    id = ObjectIDAttribute("id")
    slug = ObjectAttribute("slug")
    parent_domain = ObjectAttribute("parent_domain")
    name = ObjectAttribute("name")

    osversion = ToOneRelationship("osversion")

    # admin properties
    admin_first_name = ObjectAttribute("admin_first_name")
    admin_last_name = ObjectAttribute("admin_last_name")
    admin_initial_password = ObjectAttribute("admin_initial_password")

    # event properties
    event_name = ObjectAttribute("event_name")
    event_description = ObjectAttribute("event_description")
    event_date = ObjectAttribute("event_date")
    event_location = ObjectAttribute("event_location")
    event_organizer = ObjectAttribute("event_organizer")
