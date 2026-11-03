from tickets import ticket_price_cents

ages = [12, 16, 70]
total = 0
for age in ages:
    price = ticket_price_cents(age)
    total = total + price
    print(age, price, total)
print(f"Group total: EUR {total / 100:.2f}")
