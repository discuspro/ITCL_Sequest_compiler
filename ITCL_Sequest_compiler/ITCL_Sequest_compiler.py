import xlrd

path = "testbook1.xlsx"

book = xlrd.open_workbook(path)
sheet = book.sheet_by_index(0)
a1 = sheet.cell_value(rowx=2, colx=4)
print (a1)

import xlwt
 
book = xlwt.Workbook()
sheet = book.add_sheet("PySheet1")
sheet.write(0, 0, a1) # row, column, value
book.save("test1.xls")
