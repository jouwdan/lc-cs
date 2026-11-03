"""Original Topic 06 solutions. Prices are fictional, in integer cents."""

def ticket_price_cents(age):
    if type(age) is not int or not 0 <= age <= 120:
        raise ValueError("Age must be a whole number from 0 to 120")
    if age < 16:
        return 800
    elif age < 65:
        return 1200
    return 900


def group_total_cents(ages):
    total = 0
    for age in ages:
        total += ticket_price_cents(age)
    return total


def score_summary(entries):
    """Process valid integer scores until -1; reject other invalid values."""
    count = 0
    total = 0
    for score in entries:
        if type(score) is not int:
            raise ValueError("Score must be a whole number")
        if score == -1:
            break
        if not 0 <= score <= 100:
            raise ValueError("Score must be from 0 to 100")
        count += 1
        total += score
    return count, total


def prompt_for_age():
    while True:
        try:
            age = int(input("Age (0-120): "))
            ticket_price_cents(age)
        except ValueError as error:
            print(error)
        else:
            return age


def self_check():
    assert (17 // 5, 17 % 5, 3 + 4 * 2, (3 + 4) * 2) == (3, 2, 11, 14)
    assert "3" + "4" == "34"
    for age, expected in [(0, 800), (15, 800), (16, 1200), (64, 1200), (65, 900), (120, 900)]:
        assert ticket_price_cents(age) == expected
    for age in [-1, 121, 16.5, "16", True]:
        try:
            ticket_price_cents(age)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid age accepted")
    assert group_total_cents([12, 16, 70]) == 2900
    assert group_total_cents([]) == 0
    assert f"{ticket_price_cents(12) / 100:.2f}" == "8.00"
    assert score_summary([40, 60, -1, 99]) == (2, 100)
    assert score_summary([-1]) == (0, 0)
    assert score_summary([]) == (0, 0)
    for entries in [[101], [-2], ["40"]]:
        try:
            score_summary(entries)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid score accepted")
    print("Topic 06 checks passed")


if __name__ == "__main__":
    self_check()
