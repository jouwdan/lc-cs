count = 0
total = 0
while True:
    try:
        score = int(input("Score (0-100), or -1 to finish: "))
    except ValueError:
        print("Enter a whole number.")
        continue
    if score == -1:
        break
    if not 0 <= score <= 100:
        print("Score must be from 0 to 100.")
        continue
    total = total + score
    count = count + 1
print("Count:", count)
print("Total:", total)
