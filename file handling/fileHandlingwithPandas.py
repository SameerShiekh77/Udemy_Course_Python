import pandas as pd
files = pd.ExcelFile("sales.xlsx")
print(files.sheet_names)
print(type(files))
sheet = files.parse('sales')
print("Sales Sheet")
# print(sheet)
# print(type(sheet))
# print(sheet.Amount)
# print(sheet.Amount.sum())
# print(sheet.loc[2])
# print(sheet.loc[2,'Amount'])
sheet.set_index("Customer", inplace = True)
print(sheet.loc['MMC Inc.'])
sheet = sheet.reset_index()
print(sheet['Invoice'])
print(sheet.loc[sheet['Amount'] > 2000])
print(sheet.loc[sheet['Amount'].idxmax()])
print(sheet.loc[sheet['Amount'] > 1800])
print(sheet.loc[sheet['Amount']>1800].unique())