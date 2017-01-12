import os, sys
import csv

import agate
import agatesql

seperator = '\n' + '========================================' + '\n'
yes = set(['yes','ye','y',''])
no = set(['no','n'])

openfile = 'customerOrderHistory.csv'

customerFile = 'customers_real.csv'
orderHistoryFile = 'orderHistory_real.csv'


# column headers
shipTo = 'Customer'
billTo = 'Bill-to'
orderDate = 'Order Date'
customerNumberCustomersFile = ''
customerNumberOrdersFile = 'Ship-to'
customerName = 'CustomerName'


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
            .select([shipTo,billTo,customerName,orderDate]) \
            .where(lambda row: row[orderDate] > date) \
            .order_by(shipTo)

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


# Join the two tables together by Ship To Customer Number - .join(orders table name from agate, customer id in customers table from agate, customer id in orders table from agate, inner=True)
# Select only Ship To and Order Date Columns
# Order by Order Date from most recent. Script pulls first distinct it gets to for ship number so this gets the latest date per distinct Ship To
# Get distinct Ship To
# Sort Table by lowest Ship To
joined = customers \
    .join(orders, shipTo, customerNumberOrdersFile, inner=True) \
    .select([shipTo,billTo,customerName,orderDate]) \
    .order_by(orderDate, reverse=True) \
    .distinct(shipTo) \
    .order_by(shipTo)


# Print Table
print(seperator + 'Last Order per Ship To' + seperator)
joined.print_table()
print('\n')

filterDate()
