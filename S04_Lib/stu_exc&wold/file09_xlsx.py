import openpyxl as pxl
import random

wb = pxl.load_workbook(r"D:\A_Files_Saved\files\Excel_1.xlsx")
ws = wb["Sheet1"]

for cell in ws[1][:10]:
    cell.value = random.randint(1, 10)

wb.save(r"D:\A_Files_Saved\files\Excel_1.xlsx")
