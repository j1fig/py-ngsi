class ContextElement(object):
    """
    NGSI Context Element
    """
    def __init__(self, type_, attributes, id_=None, isPattern=False):
        self.type = type_
        self.attributes = attributes
        self.id = id_
        self.isPattern = isPattern

        # Assigns an unique id if none given
        if not id_:
            self.id = type_ + '-' + uuid4()


class Attribute(object):
    """
    NGSI Context Element Attribute
    """
    pass


class QueryError(Exception):
    pass
