from tickets import ticket_price_cents

try:
    age = int(input("Age (0-120): "))
    cents = ticket_price_cents(age)
except ValueError:
    print("Enter a whole-number age from 0 to 120.")
else:
    print(f"Price: EUR {cents / 100:.2f}")
