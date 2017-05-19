class SillyDict(object):
    """
    This is the silliest pure-python dict that you can ever write
    """
    def __init__(self):
        """
        Initialie internal data sctructure
        """
        super(SillyDict, self).__init__()
        self._keys = []
        self._vals = []

    def __getitem__(self, key):
        """
        Get an Item
        """
        try:
            idx = self._keys.index(key)
            return self._vals[idx]
        except ValueError:
            raise KeyError(key)

    def __setitem__(self, key, val):
        """
        Set an Iterm
        """
        if key in self._keys:
            idx = self._keys.index(key)
            self._vals[idx] = val
        else:
            self._keys.append(key)
            self._vals.append(val)

    def pop(self, key):
        """
        Remove and return the value for a key
        """
        try:
            idx = self._keys.index(key)
            del self._keys[idx]
            val = self._vals[idx]
            del self._vals[idx]
            return val
        except ValueError:
            raise KeyError(key)

    def __delitem__(self, key):
        """
        Delete is just `pop` without return
        """
        self.pop(key)

    def __contains__(self, key):
        """
        Check if a key is in the dictionary
        """
        key in self._keys

    def keys(self):
        """
        Return a list of keys in the dictionary
        """
        return self._keys

    def values(self):
        """
        Return a list of values in the dictionary
        """
        return self._vals

    def _zipped(self):
        """
        Return Zipped keys and vals
        """
        return zip(self._keys, self._vals)

    def items(self):
        """
        Return a list of key-value pairs
        """
        return self._zipped()

    def clear(self):
        """
        Clear the dictionary of all data
        """
        self._keys = []
        self._vals = []

    def __iter__(self):
        """
        Just an Itrator ovet things
        """
        return self._zipped()

    def iterkeys(self):
        """
        Return an iterator over the keys in the dictionary
        """
        return self._keys

    def itervalues(self):
        """
        Return an iterator over the values in the dictionary
        """
        return self._vals

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
        return len(self._keys)

    def __repr__(self):
        """
        Representation on this SillyDict
        """
        r = ["{0!r} : {1!r}".format(k, v) for k, v in self.iteritems()]
        return "SillyDict({" + ", ".join(r) + "})"
