import sqlite3

db = 'sample.sqlite'
connection = sqlite3.connect(db)
cursor = connection.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS test")
    cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO test VALUES(1, '山田修一郎')")
    cursor.execute("INSERT INTO test VALUES(2, ?)", ('山本晋作',))
    cursor.execute("INSERT INTO test VALUES(?, ?)", (3, '沢田恵美'))
    cursor.execute("INSERT INTO test VALUES(:id, :name)", {'id':4, 'name':'植田美佐江'})
except sqlite3.Error as e:
    print(e.args[0])

connection.commit()
connection.close()
