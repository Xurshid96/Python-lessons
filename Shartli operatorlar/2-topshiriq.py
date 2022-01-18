son = int(input("Sonni kiriting : "))

if son%3 == 0 and son%5 == 0:
    print("FizBiz")
elif son%3 == 0:
    print("Fiz")
elif son%5 == 0 :
    print("Biz")
else:
    print(son)