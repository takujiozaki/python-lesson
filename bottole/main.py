from bottle import route, run, request
import openpyxl as px
import os


def writepage():
    return '''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="h3">書籍データベース</h1>
        <form method="post">
            <div class="form-row">
                <div class="col">
                    <input type="text" name="title" id="" class="form-control" placeholder="書籍名">
                </div>
                <div class="col">
                    <input type="text" name="author" id="" class="form-control" placeholder="著者">
                </div>
                <div class="col">
                    <input type="number" name="pages" id="" class="form-control" placeholder="ページ数">
                </div>
                <div class="col"><button type="submit" class="btn btn-primary">登録</button></div>
            </div>
        </form>
    </div>
    
</body>
</html>
    '''


@route('/')
def input():
    return writepage()


@route('/', method='POST')
def input_sheet():
    # Requestを受け取る
    title = request.forms.title
    author = request.forms.author
    pages = request.forms.pages
    data_list = read_data()

    #data_listの初期化
    if data_list == []:
        data_list.append(["title", "author", "pages"])

    # Requestを追加
    data_list.append([title, author, pages])

    #workbookを作成
    workbook = px.Workbook()
    worksheet = workbook.active
    for data in data_list:
        worksheet.append(data)

    workbook.save('books.xlsx')

    return writepage()


def read_data():
    path = "books.xlsx"
    if os.path.exists(path):
        workbook = px.load_workbook(path, data_only=True)
        worksheet = workbook.active
        return list(worksheet.values)

    # 存在しない場合は空のリストを返す
    return []


run(host='localhost', port=8782)
