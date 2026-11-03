"""Deliberately faulty lab specimen: its assertion MUST fail."""
def faulty_booking_total(quantity):
    if quantity > 5:
        price = 1000
    else:
        price = 1200
    return quantity * price

if __name__ == "__main__":
    print("Actual cents:", faulty_booking_total(5))
    assert faulty_booking_total(5) == 5000
