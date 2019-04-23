class BaseEntity(object):
    def __init__(self, document):
        super(BaseEntity, self).__init__()
        self._document = document

        for k, v in document.iteritems():
            setattr(self, k, v)

    @property
    def id(self):
        return self._document.get('_id')

    @id.setter
    def id(self, new_id):
        if self.id:
            raise BaseException()
        self._document['_id'] = new_id

    @property
    def document(self):
        return copy.deepcopy(self._document)