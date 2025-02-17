# A CAN bus node (or Board unit)

class Node(object):
    """An NODE on the CAN bus.

    """

    def __init__(self,
                 name,
                 comment=None,
                 dbc_specifics=None,
                 autosar_specifics=None):
        self._name = name

        # If the 'comment' argument is a string, we assume that is an
        # English comment. This is slightly hacky, because the
        # function's behavior depends on the type of the passed
        # argument, but it is quite convenient...
        if isinstance(comment, str):
            # use the first comment in the dictionary as "The" comment
            self._comments = { None: comment }
        else:
            # assume that we have either no comment at all or a
            # multi-lingual dictionary
            self._comments = comment

        self._dbc = dbc_specifics
        self._autosar = autosar_specifics

    @property
    def name(self):
        """The node name as a string.

        """

        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def comment(self):
        """The node's comment, or ``None`` if unavailable.

        Note that we implicitly try to return the English comment if
        multiple languages were specified.

        """
        if self._comments is None:
            return None
        elif self._comments.get(None) is not None:
            return self._comments.get(None)
        elif self._comments.get("FOR-ALL") is not None:
            return self._comments.get("FOR-ALL")

        return self._comments.get('EN')

    @property
    def comments(self):
        """The dictionary with the descriptions of the bus in multiple
        languages. ``None`` if unavailable.

        """
        return self._comments

    @comment.setter
    def comment(self, value):
        self._comment = value

    @property
    def dbc(self):
        """An object containing dbc specific properties like e.g. attributes.

        """

        return self._dbc

    @dbc.setter
    def dbc(self, value):
        self._dbc = value

    @property
    def autosar(self):
        """An object containing AUTOSAR specific properties of the node.

        """

        return self._autosar

    @autosar.setter
    def autosar(self, value):
        self._autosar = value

    def __repr__(self):
        return "node('{}', {})".format(
            self._name,
            "'" + self.comment + "'" if self.comment is not None else None)
