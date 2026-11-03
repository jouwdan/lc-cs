# Run this complete example; change passengers to test another case.
passengers = 25
capacity = 12

if type(passengers) is not int or passengers < 0:
    print("Invalid passenger count")
else:
    buses = passengers // capacity
    if passengers % capacity > 0:
        buses = buses + 1
    print("Buses:", buses)
