def check_dict_values_postive(d):
    return any(v < 0 for v in iter(d.values()))
