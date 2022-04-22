import sqlite3

db=sqlite3.connect("data/B/DB_B.sqlite")
cursor=db.cursor()
for row in cursor.execute('''select cast(confirmed*100 as real)/test
from Time
where date='2020-05-05' '''):
    ans=(str(row))
print(ans[1:-2]+'%')