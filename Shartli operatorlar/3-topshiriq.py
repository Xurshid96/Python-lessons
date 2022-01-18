a = int(input("a - o'zgarivchini kiriting : "))
b = int(input("b - o'zgarivchini kiriting : "))
c = int(input("c - o'zgarivchini kiriting : "))

if b**2 - 4*a*c == 0:
    print("ax^2 + bx + c = 0 kvadrat tenglama 1ta yechimga ega")
elif b**2 - 4*a*c < 0:
    print("ax^2 + bx + c = 0 kvadrat tenglama 0ta yechimga ega")
elif b**2 - 4*a*c > 0:
    print("ax^2 + bx + c = 0 kvadrat tenglama 2ta yechimga ega")