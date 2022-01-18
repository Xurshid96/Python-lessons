def ismlar(name, n):
    if n == 0:
        return str(name[0])
    else:
        return str(name[n]) + str(ismlar(name, n-1))


first_name = input("Ismlarni kiriting : ")
name = ismlar(first_name, len(first_name)-1)
print(name)