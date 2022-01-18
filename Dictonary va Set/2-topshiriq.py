def is_anagram (s1, s2):
    if(sorted(s1) == sorted(s2)):
        return True
    return False


s1 = input("1 - so'zni : ")
s2 = input("2 - so'zni : ")

print(is_anagram(s1,s2))