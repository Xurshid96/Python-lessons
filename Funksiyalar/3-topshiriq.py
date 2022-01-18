def ismlar(names):
    list = []
    for i in range (0, len(names), 1):
        list.append(len(names[i]))
    x = max(list)
    for i in range(0, len(names), 1):
        if  x == len(names[i]):
            return print(names[i])

ismlar(input("Ismlarni kiriting : ").split(sep=", "))

# Dildora, Dili, Honzodabegim, Ahmadjon, Bobur