import openpyxl as px

# ファイルを開く
workbook = px.load_workbook('schedule.xlsx')

# worksheetを取得(List形式)
worksheets = workbook.sheetnames
print(worksheets)
list = []

for worksheet in worksheets:
    print(type(worksheet)) #自身のシート名
    data = workbook[worksheet]
    for row in data:
        for cells in row:
            if cells.value == "C":
                cells.value = cells.value + "言語"
                print(cells.value)



# excel形式に書き出し
workbook.save('schedule.xlsx')