import sqlite3
from sqlite3 import OperationalError
import os
db=sqlite3.connect('data/A/DB_A.sqlite')
cursor=db.cursor()

fo=open('DB_A.sql','r')
sqlFile=fo.read()
fo.close()

sqlCommands=sqlFile.split(';')

for command in sqlCommands:
    try:
        cursor.execute(command)
    except OperationalError:
        None
db.commit()

path="./data/A"
fileList=os.listdir(path)
csvList=[file for file in fileList if file.endswith(".csv")]

for file in csvList: #for each csv files
    
    tupleData=[]

    fo=open('data/A/'+file,'r')
    file=file[:-4] #delete filename extension(.csv)

    csvFile=fo.read() #all data
    csvLine=csvFile.split('\n') #data split
    csvLine.pop(-1) #delete space
    for factor in csvLine: #for each line in file
        tempData=factor.split(',')
        #for cnt in tempData:
        #    imsi.append('?')
        tupleData.append(tempData)
    tupleData.pop(0)
    
    
    #print(tupleData)
    tuple(tupleData)
    #print(tupleData)
    for factor in tupleData:
        imsiData=[]
        imsiCol=[]
        imsi=[]
        k=0
        imsiLine=csvLine[0]
        imsiLine=imsiLine.split(',')
        while k<len(factor):
            if(factor[k]!=''):
                imsiData.append(factor[k])
                imsiCol.append(imsiLine[k])
                imsi.append('?')
            k=k+1
        imsi=','.join(imsi)
        tuple(imsiData)
        finalCol=str(imsiCol)
        finalCol=finalCol.replace("'","")
        #print(finalCol[1:-1])
        cursor.execute('INSERT INTO '+file+'('+finalCol[1:-1]+') VALUES('+imsi+')',imsiData)
    #cursor.executemany('INSERT INTO '+file+'('+csvLine[0]+') VALUES('+imsi+')',tupleData)
db.commit()
