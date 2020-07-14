import openpyxl as px

# worksheetに書き込む内容
schedule = (
    ('08/03', '川畑', '開発演習'),
    ('08/04', '尾崎', 'Python'),
    ('08/05', '宮野', '開発演習'),
    ('08/06', '', '指定来所日'),
    ('08/07', '宮野', '開発演習'),
    ('08/11', '尾崎', 'Python'),
    ('08/12', '宮野', '開発演習'),
)

# workbookオブジェクトを生成
new_workbook = px.Workbook()

# worksheetオブジェクトを作成
new_worksheet = new_workbook.create_sheet('2020_08_授業予定', 0)

# 見出し行を挿入
new_worksheet.append(["日付", "担当講師", "授業内容"])

# 内容を書き込む
for row in schedule:
    new_worksheet.append([row[0], row[1], row[2]])

# excel形式に書き出し
new_workbook.save('schedule.xlsx')