import random


i = 0
while i < 20:
    year = [15,16]
    randomyear = str(random.choice(year))
    month = str(random.randint(1,12)).rjust(2,"0")
    day = str(random.randint(1,30)).rjust(2,"0")
    # Get random YY
    print(str(1)+randomyear+month+day)
    i += 1
