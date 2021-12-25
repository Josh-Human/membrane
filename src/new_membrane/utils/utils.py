def check_dict_values_postive(self, key):
    return any(v < 0 for v in iter(self._data[key].values()))
