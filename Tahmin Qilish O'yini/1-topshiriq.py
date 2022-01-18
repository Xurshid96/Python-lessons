import random

GameOver = ValueError

def random_number():
    return random.randint(1, 10)

def check_number(number, guess):
    message = "Men o'ylagan son"
    if number < guess :
        return f"{message} {guess}dan kichikroq."

    if number > guess :
        return f"{message} {guess}dan kattaroq."

    raise GameOver

def main():
    number = random_number()
    print("Men 1-10 gacha son o'yladim.")
    imhoniyat_soni = 0
    while imhoniyat_soni < 3:
        try:
            guess = int(input("Tahminingizni kiriting : "))
            message = check_number(number, guess)
            print(message)
            imhoniyat_soni += 1
        except GameOver:
            print("O'ylagan sonni topdingiz!")
            break
    else:
        print("Afsus siz topa olmadiz. ")

if __name__ == '__main__':
    main()
