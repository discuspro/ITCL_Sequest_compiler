import xlrd

path = r'C:\testbook1.xlsx'

book = xlrd.open_workbook(path)
sheet = book.sheet_by_index(0)
a1 = sheet.cell_value(rowx=2, colx=4)
print (a1)