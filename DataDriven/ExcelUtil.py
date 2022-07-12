import openpyexcel

#creating rowcounting function
def getRowCount(file,sheet):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook.get_sheet_by_name(sheet)
    return(sheet.max_row)

#creat columncount function
def getColumnCount(file,sheetname):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook.get_sheet_by_name(sheetname)
    return (sheet.max_column)

#creat an function to read data from excel
def ReadData(file: object, sheetname: object, rownum: object, columnno: object) -> object:
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook.get_sheet_by_name(sheetname)
    return sheet.cell(row=rownum,column=columnno).value

#creat an function to write data into excel file
def WriteData(file,sheetname,rowno,columnno,data):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook.get_sheet_by_name(sheetname)
    sheet.cell(row=rowno,column=columnno).value=data
    workbook.save(file)
