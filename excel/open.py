import openpyxl as px

workbook = px.load_workbook("kobeweather.xlsx", data_only=True)
print(workbook.sheetnames)

worksheet = workbook['Sheet1']

for row in worksheet.values:
    print(row)
    for value in row:
        print(value)



