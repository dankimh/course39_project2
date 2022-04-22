import sqlite3

db=sqlite3.connect("data/A/DB_A.sqlite")
cursor=db.cursor()

for row in cursor.execute('''select age, infection_case, cast(cast(100*count(case when state='isolated' then 1 end) as real)/count(state) as text)||'%', cast(cast(100*count(case when state='released' then 1 end) as real)/count(state) as text)||'%', cast(cast(100*count(case when state='deceased' then 1 end) as real)/count(state) as text)||'%'
from (select * 
    from (
        select patient_id, count(DISTINCT province||city) as cityCount
        from PatientRoute
        group by patient_id
    ) as patient_with_cityCount natural join (select patient_id,age,infection_case,state from PatientInfo)
    where cityCount>1
    order by age)
group by age, infection_case;'''):
    print(row[0],row[1],row[2],row[3],row[4])
