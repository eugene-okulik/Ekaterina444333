def fibonachi(limit):
    a , b = 0, 1
    count = 0
    while True:
        yield a
        a, b = b, a + b
        count += 1


right_count = [5, 200, 1000, 100000]
count = 0
for number in fibonachi(100000):
    count += 1
    if count in right_count:
        print(number)
    if count == 100000:
        break



