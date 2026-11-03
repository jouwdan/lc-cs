"""Original Topic 09 debugging exercise and regression checks."""

def faulty_booking_total(quantity):
    """Deliberately wrong teaching specimen; do not use as the solution."""
    if quantity > 5:
        price = 1000
    else:
        price = 1200
    return quantity * price


def booking_total_cents(quantity):
    if type(quantity) is not int or not 1 <= quantity <= 8:
        raise ValueError("Enter a whole number from 1 to 8")
    if quantity >= 5:
        price = 1000
    else:
        price = 1200
    return quantity * price


def total_from_text(text):
    try:
        quantity = int(text)
    except ValueError as error:
        raise ValueError("Enter a whole number from 1 to 8") from error
    cents = booking_total_cents(quantity)
    return f"Total: EUR {cents / 100:.2f}"


def self_check():
    assert faulty_booking_total(5) == 6000
    assert faulty_booking_total(5) != 5000
    expected = {1: 1200, 2: 2400, 3: 3600, 4: 4800, 5: 5000, 6: 6000, 7: 7000, 8: 8000}
    for quantity, total in expected.items():
        assert booking_total_cents(quantity) == total
    for quantity in [0, 9, -1, 2.5, "five", "5", True]:
        try:
            booking_total_cents(quantity)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid quantity accepted")
    assert total_from_text("5") == "Total: EUR 50.00"
    assert total_from_text(" 4 ") == "Total: EUR 48.00"
    for text in ["five", "2.5", "0", "9", ""]:
        try:
            total_from_text(text)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid input accepted")
    assert (3 == "3") is False
    try:
        "3" + 4
    except TypeError:
        pass
    else:
        raise AssertionError("Unexpected Python coercion")
    print("Topic 09 checks passed")


if __name__ == "__main__":
    self_check()
