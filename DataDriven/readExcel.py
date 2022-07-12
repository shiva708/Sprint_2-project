import openpyexcel

#creat an interface load the work book
workbook = openpyexcel.load_workbook("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\Book1.xlsx")

#creat an interface to load the sheet
sheet = workbook.active

#count the row & column
rows = sheet.max_row
column = sheet.max_column

#print no.of row & column
print(rows)
print(column)

# print the excel value using for loop

for r in range(1,rows+1):
    for c in range(1,column+1):
        print(sheet.cell(row=r,column=c).value,end=" ")
#this print will make a space for the each value
    print()