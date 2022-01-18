name_person = input("Your name: ")
greeting = 'Salom %s' % {name_person}
print(greeting)

greeting = "Salom {}".format(name_person)
print(greeting)

greeting = f"Salom {name_person}"
print(greeting)