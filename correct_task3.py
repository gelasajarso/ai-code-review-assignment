def average_valid_measurements(values):
    total = 0.0
    count = 0

    for v in values:
        if v is None:
            continue

        try:
            total += float(v)
            count += 1
        except (TypeError, ValueError):
            continue

    if count == 0:
        return 0.0

    return total / count
