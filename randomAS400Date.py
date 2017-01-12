import random
import csv

seperator = '\n' + '========================================' + '\n'

print(seperator)
print("""This is a quick AS400 Date generator. \n
Enter how many dates you need to generate, a two digit start year and two digit end year.
For simplicity sake the DD is only a range of 1 - 30.
There is no check for going past the current date in the year we are in.""")
print(seperator)

numRows = input('How many dates do you need to generate? : ')
startYear = input('What is the TWO DIGIT start year (currently works with 2000+)? : ')
endYear = input('What is the TWO DIGIT final year? : ')
with open("as400dates.csv", 'w') as f:
    writer = csv.writer(f, dialect='excel')
    i = 0
    while i < int(numRows):
        year = str(random.randint(int(startYear),int(endYear))).rjust(2,"0")
        # randomyear = str(random.choice(year))
        month = str(random.randint(1,12)).rjust(2,"0")
        day = str(random.randint(1,30)).rjust(2,"0")
        # Get random YY
        # print(str(1)+randomyear+month+day)
        date = str(1)+year+month+day
        writer.writerow([date])

        i += 1
