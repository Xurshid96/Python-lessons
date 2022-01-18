import  time
from datetime import datetime

while True:
    print(" 2 minit kutamiz")
    now = datetime.now()
    print(now.strftime("%c"))
    time.sleep(2)