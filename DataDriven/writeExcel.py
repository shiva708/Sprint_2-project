import openpyexcel

#load the workbook
workbook = openpyexcel.load_workbook("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\Book1.xlsx")

#load the sheet
sheet =workbook.active

#write the data into excel using for loop
for r in range(7,8):
    for c in range(1,2):
        sheet.cell(row=r,column=c).value="Pune"


#after adding the data we can save the value into excel file.
workbook.save("C:\\Users\\Shiva\\OneDrive\\Desktop\\capgemini training\\Automation testing\\selenium\\sprint _2\\Book1.xlsx")
print("written of file writting")