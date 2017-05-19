class SillyHashDict(object):
    """
    This is the silliest pure-python hash dict that you can ever write
    """
    def __init__(self, max_len=10):
        """
        Initialie internal data sctructure
        """
        super(SillyHashDict, self).__init__()
        self.max_len = max_len
        self._items = [None] * self.max_len

    def _hash(self, key):
        """
        Calculate Hash
        + Compressor function
        # sum([ord(i) for i in a])
        """
        return len(key) % self.max_len  # Here, '%' is the compressor function

    def __getitem__(self, key):
        """
        Get an Item
        """
        idx = self._hash(key)
        item = self._items[idx]
        if item is None:
            raise KeyError(key)
        return item[2]

    def __setitem__(self, key, val):
        """
        Set an Iterm
        """
        idx = self._hash(key)
        self._items[idx] = (idx, key, val)

    def pop(self, key):
        """
        Remove and return the value for a key
        """
        idx = self._hash(key)
        item = self._items[idx]
        self._items[idx] = None
        if item is None:
            raise KeyError(key)
        return item[2]

    def __delitem__(self, key):
        """
        Delete is just `pop` without return
        """
        self.pop(key)

    def __contains__(self, key):
        """
        Check if a key is in the dictionary
        """
        idx = self._hash(key)
        item = self._items[idx]
        return item is not None

    def keys(self):
        """
        Return a list of keys in the dictionary
        """
        return [item[1] for item in self.items if item is not None]

    def values(self):
        """
        Return a list of values in the dictionary
        """
        return [item[2] for item in self.items if item is not None]

    def items(self):
        """
        Return a list of key-value pairs
        """
        return [(item[1], item[2]) for item in self._items if item is not None]

    def clear(self):
        """
        Clear the dictionary of all data
        """
        self._keys = []
        self._items = []

    def __iter__(self):
        """
        Just an Itrator ovet things
        """
        return self.items()

    def iterkeys(self):
        """
        Return an iterator over the keys in the dictionary
        """
        return self.keys()

    def itervalues(self):
        """
        Return an iterator over the values in the dictionary
        """
        return self.values()

    def iteritems(self):
        """
        Return an iterator over key-value pairs
        """
        return self.items()

    def get(self, key, default=None):
        """
        Return the value for key if it exists otherwise the default
        """
        try:
            return self[key]
        except KeyError:
            return default

    def __len__(self):
        """
        Len of dict
        """
        return len(self._items)

    def __repr__(self):
        """
        Representation on this SillyDict
        """
        r = ["{0!r} : {1!r}".format(k, v) for k, v in self.iteritems()]
        return "SillyHashDict({" + ", ".join(r) + "})"
