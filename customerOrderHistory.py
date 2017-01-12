import os, sys
import csv

import agate
import agatesql

seperator = '\n' + '========================================' + '\n'
yes = set(['yes','ye','y',''])
no = set(['no','n'])

openfile = 'customerOrderHistory.csv'

customerFile = 'customers.csv'
orderHistoryFile = 'orderHistory.csv'

## DEFS
def filterDate():
    # limit by date
    filterDate = input('Do you want to filter to date of last purchase? (y/n) ')
    # Close
    if filterDate in no:
        saveCustomersAll = input('Do you want to save "Last Order per Ship To" to a csv? (y/n) ')
        if saveCustomersAll in no:
            sys.exit('Closing')
        elif saveCustomersAll in yes:
            fileNameAll = input('Enter file name with ".csv" ')
            joined.to_csv(fileNameAll)
            # Not a true check of file saving
            sys.exit(seperator + 'File Saved. Closing Script.' + seperator)

    elif filterDate in yes:
        as400Date = input('What is the date in the AS400 date format?:  ')
        date = int(as400Date)
        filteredByDate = joined \
            .select(['Ship To','Company Name','Order Date']) \
            .where(lambda row: row['Order Date'] > date) \
            .order_by('Ship To')

        print(seperator + 'Last Order per Ship To after '+ str(date) + seperator)
        filteredByDate.print_table()
        print('\n')

        saveCustomersFiltered = input('Do you want to save "Last Order per Ship To after" '+ str(date)  +' to a csv? (y/n) ')
        if saveCustomersFiltered in no:
            sys.exit('Closing')
        elif saveCustomersFiltered in yes:
            fileNameAll = input('Enter file name with ".csv" ')
            filteredByDate.to_csv(fileNameAll)
            # Not a true check of file saving
            sys.exit(seperator + 'File Saved. Closing Script.' + seperator)


customers = agate.Table.from_csv(customerFile)
orders = agate.Table.from_csv(orderHistoryFile)


# Join the two tables together by Ship To Customer Number
# Select only Ship To and Order Date Columns
# Order by Order Date from most recent. Script pulls first distinct it gets to for ship number so this gets the latest date per distinct Ship To
# Get distinct Ship To
# Sort Table by lowest Ship To
joined = customers \
    .join(orders, 'Ship To', 'Customer No', inner=True) \
    .select(['Ship To','Company Name','Order Date']) \
    .order_by('Order Date', reverse=True) \
    .distinct('Ship To') \
    .order_by('Ship To')


# Print Table
print(seperator + 'Last Order per Ship To' + seperator)
joined.print_table()
print('\n')

filterDate()
