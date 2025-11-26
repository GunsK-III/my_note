import openpyxl as xl

wb = xl.load_workbook(r"D:\A_Files_Saved\files\Excel_2.xlsx")
ws = wb["Sheet"]
print(ws.rows)
for row in ws.rows:
    print(row[0].value)