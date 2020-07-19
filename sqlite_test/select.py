import sqlite3

db = 'sample.sqlite'
connection = sqlite3.connect(db)
cursor = connection.cursor()

try:
    cursor.execute('select * from text order by id')
    # 全件取得
    fetch_all = cursor.fetchall()
    print(fetch_all)
    # 件数取得
    print(len(fetch_all))

    # 単件取得
    cursor.execute('select * from sample order by id')
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())

    # UPDATE
    cursor.execute('UPDATE sample set name=? where id=?', ('澤田恵美', 3))
    connection.commit()

    # DELETE
    cursor.execute('DELETE FROM sample where id=?', (2, ))
    connection.commit()

    # loop
    cursor.execute('select * from sample order by id')
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(e.args[0])

