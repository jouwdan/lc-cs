"""Original Topic 05 model solutions; run with Python 3 for self-checks."""

def buses_needed(passengers, capacity=12):
    if type(passengers) is not int or type(capacity) is not int:
        raise ValueError("Passenger count and capacity must be integers")
    if passengers < 0 or capacity <= 0:
        raise ValueError("Passenger count must be non-negative and capacity positive")
    buses = passengers // capacity
    if passengers % capacity > 0:
        buses += 1
    return buses


def count_at_least(values, threshold):
    count = 0
    for value in values:
        if value >= threshold:
            count += 1
    return count


def self_check():
    for passengers, expected in [(0, 0), (1, 1), (11, 1), (12, 1), (13, 2), (24, 2), (25, 3)]:
        assert buses_needed(passengers) == expected
    assert buses_needed(31, 16) == 2
    assert buses_needed(32, 16) == 2
    for passengers, capacity in [(-1, 12), (1, 0), (1.5, 12), (True, 12)]:
        try:
            buses_needed(passengers, capacity)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid booking accepted")
    assert count_at_least([48, 72, 50, 31], 50) == 2
    assert count_at_least([], 50) == 0
    assert count_at_least([50, 50], 50) == 2
    print("Topic 05 checks passed")


if __name__ == "__main__":
    self_check()
