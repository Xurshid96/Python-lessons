numbers = input("Ixtiyoriy son kiriting : ").split(sep=" ")
for number in numbers:
        for i in range(-1, -len(number)-1, -1):
                print(number[i], end="")
        print(end=" ")

