import sqlite3

db=sqlite3.connect("data/A/DB_A.sqlite")
cursor=db.cursor()

cursor.execute('''update PatientInfo set age='0s' where 2020-birth_year+1 between 0 and 9;''')
cursor.execute('''update PatientInfo set age='10s' where 2020-birth_year+1 between 10 and 19;''')
cursor.execute('''update PatientInfo set age='20s' where 2020-birth_year+1 between 20 and 29;''')
cursor.execute('''update PatientInfo set age='30s' where 2020-birth_year+1 between 30 and 39;''')
cursor.execute('''update PatientInfo set age='40s' where 2020-birth_year+1 between 40 and 49;''')
cursor.execute('''update PatientInfo set age='50s' where 2020-birth_year+1 between 50 and 59;''')
cursor.execute('''update PatientInfo set age='60s' where 2020-birth_year+1 between 60 and 69;''')
cursor.execute('''update PatientInfo set age='70s' where 2020-birth_year+1 between 70 and 79;''')
cursor.execute('''update PatientInfo set age='80s' where 2020-birth_year+1 between 80 and 89;''')
cursor.execute('''update PatientInfo set age='90s' where 2020-birth_year+1 between 90 and 99;''')
db.commit()
#don't have to change age='100s'