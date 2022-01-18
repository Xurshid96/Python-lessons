try:
    # IndexError
    list = [3, 5, 6, 10]
    print(list[5])
    # KeyError
    list = {"name": "Jahongir", "age":23, "country":"Uzbekistan"}
    print(list["Last_name"])
    # TypeError
    number = 5
    name = "Komil"
    print(type(number + name))
except (IndexError, KeyError, TypeError) as exception:
    print(exception)