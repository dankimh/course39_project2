import sqlite3

db=sqlite3.connect("data/B/DB_B.sqlite")
cursor=db.cursor()
confirmed=[]
for row in cursor.execute('''select date,cast(confirmed*100 as real)/test
from Time'''):
    confirmed.append(row)
i=1
j=0
max_date=['2020-03-03',]
max_confirmed=[-0xffff,]
while i<len(confirmed):
    #print(max_confirmed)
    if(max_confirmed[j]<(confirmed[i][1]-confirmed[i-1][1])):
        del max_date[:]
        del max_confirmed[:]
        j=0
        max_date.append(confirmed[i][0])
        max_confirmed.append(confirmed[i][1]-confirmed[i-1][1])
    if(max_confirmed==(confirmed[i][1]-confirmed[i-1][1])):
        max_date.append(confirmed[i][0])
        max_confirmed.append(confirmed[i][1]-confirmed[i-1][1])
        j=j+1
    i=i+1
print(j)
i=0
while i<=j:
    for row in cursor.execute("""select date, age, cast(cast(confirmed*100 as real)/(select sum(confirmed) from TimeAge where date='"""+max_date[i]+"""') as text)||'%', cast(cast(deceased*100 as real)/(select sum(deceased) from TimeAge where date='"""+max_date[i]+"""') as text)||'%'
from TimeAge
where date='"""+max_date[i]+"""';"""):
        print(row[0],row[1],row[2],row[3])
    #print('''select * from TimeAge where date='''+"'"+max_date[i]+"'")
    i=i+1
