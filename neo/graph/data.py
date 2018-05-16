from py2neo import Database
from py2neo.ogm import GraphObject, Property
import datetime


class Node(GraphObject):

    # __primarykey__ = 'pk'

    property_title = Property(key='title')
    property_pk = Property(key='pk')

    def __init__(self, title, label="Node"):

        self.property_title = title
        self.property_pk = label + ':' + title

        self.__primarylabel__ = label


class TimeMixin(GraphObject):

    property_created = Property(key='created')
    property_updated = Property(key='updated')

    def __init__(self):
        self.property_created = str(datetime.datetime.now())
        self.property_updated = str(datetime.datetime.now())


class DataMixin(GraphObject):

    property_parseable = Property(key='parseable')
    property_parsed = Property(key='parsed')
    property_data = Property(key='data')

    def __init__(self):
        self.property_parseable = True
        self.property_parsed = False
        self.property_data = None


class DefaultGraphMixin(GraphObject):

    property_graph = Property(key='graph')

    def __init__(self):

        identifier = Database.store_id
        time_created = Database.store_creation_time

        self.graph = "{} : {}".format(identifier, time_created)

