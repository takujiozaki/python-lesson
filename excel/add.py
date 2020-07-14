import openpyxl as px

# worksheetに書き込む内容
schedule = (
    ('09/01', '宮野', '開発演習'),
    ('09/02', '', '就活日'),
    ('09/03', '平井', 'C'),
    ('09/04', '宮野', '開発演習'),
    ('09/07', '', '指定来所日'),
    ('09/08', '宮野', '開発演習'),
    ('09/09', '平井', 'C'),
    ('09/10', '川畑', '開発演習'),
    ('09/11', '宮野', '開発演習'),
)

# ワークブックを開く
workbook = px.load_workbook("schedule.xlsx", data_only=True)
# 新しいシートを作成する
new_worksheet = workbook.create_sheet('2020_09_授業予定', 1)


# 見出し行を挿入
new_worksheet.append(["日付", "担当講師", "授業内容"])

# 内容を書き込む
for row in schedule:
    new_worksheet.append([row[0], row[1], row[2]])

# excel形式に書き出し
workbook.save('schedule.xlsx')