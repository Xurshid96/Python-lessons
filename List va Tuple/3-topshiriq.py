words = input("Vergul bilan ajratib so'zlar kiriting: ").split(sep=",")

words.sort()
for i in range(0, len(words), 1):
    print(words[i])
