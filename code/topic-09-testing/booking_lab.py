"""Completed repair used by the guided testing lab."""
def booking_total_cents(quantity):
    if type(quantity) is not int or not 1 <= quantity <= 8:
        raise ValueError("Enter a whole number from 1 to 8")
    if quantity >= 5:
        price = 1000
    else:
        price = 1200
    return quantity * price

if __name__ == "__main__":
    expected = {1: 1200, 2: 2400, 3: 3600, 4: 4800,
                5: 5000, 6: 6000, 7: 7000, 8: 8000}
    for quantity, total in expected.items():
        assert booking_total_cents(quantity) == total
    for invalid in [0, 9, -1, 2.5, "five", "5"]:
        try:
            booking_total_cents(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Accepted invalid quantity: {invalid}")
    print("Booking checks passed")
