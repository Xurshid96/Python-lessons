number = int(input("Sonni kiriting : "))

list = []
for i in range(1, number+1, 1):
    if i%3 == 0 and i%5 == 0:
        list.append("FizzBuzz")
    elif i%3 == 0:
        list.append("Fizz")
    elif i%5 == 0:
        list.append("Buzz")
    else:
        list.append(i)
print(list)