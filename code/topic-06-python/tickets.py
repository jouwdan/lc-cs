"""Completed single-ticket function used by the guided lab."""
def ticket_price_cents(age):
    if type(age) is not int or not 0 <= age <= 120:
        raise ValueError("Age must be a whole number from 0 to 120")
    if age < 16:
        return 800
    elif age < 65:
        return 1200
    else:
        return 900

if __name__ == "__main__":
    for age in [0, 15, 16, 64, 65, 120]:
        print(age, ticket_price_cents(age))
    assert ticket_price_cents(16) == 1200
    assert ticket_price_cents(65) == 900
