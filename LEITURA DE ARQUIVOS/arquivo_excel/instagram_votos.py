# Create a simple Excel file 'instagram.xlsx' to begin with!
import xlrd

workbook = xlrd.open_workbook('instagram.xlsx')
sheet_names = workbook.sheet_names()
sheet = workbook.sheet_by_name(sheet_names[0])
print("numero de linhas: ",sheet.nrows)
print("numero de colunas: ",sheet.ncols)
print(sheet.cell(3,2))
for row_idx in range(sheet.nrows):
    for col_idx in range(sheet.ncols):
        cell = sheet.cell(row_idx, col_idx)
        print(cell.value, end="\t")
    print()