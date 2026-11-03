from booking_lab import booking_total_cents

try:
    quantity = int(input("Tickets (1-8): "))
    cents = booking_total_cents(quantity)
except ValueError:
    print("Enter a whole number from 1 to 8")
else:
    print(f"Total: EUR {cents / 100:.2f}")
