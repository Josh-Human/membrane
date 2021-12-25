def check_values_positive(d):
    return any(v < 0 for v in iter(d.values()))
