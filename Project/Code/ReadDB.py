import re
from sqlite3 import *

'''def AddToDB(ItemList):
    i = 0
    for x in ItemList:
        #add item[i] to DB
        file = connect("Test.db")
        cs = file.cursor()
        cs.execute("""
            INSERT INTO LightWright
            (
            {}, {}, {}
            ) VALUES ('{}', '{}', '{}')
            """.format('Channel', 'Dimmer', 'Address', ItemList[1], ItemList[2], ItemList[3]))
        file.commit()
        file.close()
        print(ItemList[i])
        i += 1
        break
        #print('t')'''

def MakeDB(col, fileName):
    i = 0
    file = connect("Test.db")
    cs = file.cursor()
    fileName = fileName.replace(' ', '_')
    fileName = fileName.split('/')
    #print(fileName[-1])
    colNum = len(col)-1
    #print(colNum)
    cs.execute("CREATE TABLE IF NOT EXISTS {}({} TEXT)".format('DB_'+fileName[-1], col[0]))
    file.commit()
    for x in range(colNum):
        i += 1
        print(col[i])
        col[i] = col[i].replace('#', '')
        col[i] = col[i].replace(' ', '_')
        col[i] = col[i].replace('/', '_')
        #if col[i] = 'When' then col[i] + col[i+1] + col[i+2] .join
        #then delete col[i+1] and col[i+2]
        cs.execute("ALTER TABLE {} ADD {} TEXT".format('DB_'+fileName[-1], col[i]))

        file.commit()
    file.close()

def AddToDB(ItemList):
    i = 0
    file = connect("Test.db")
    cs = file.cursor()
    cs.execute("""
        INSERT INTO LightWright
        (
        {}, {}, {}
        ) VALUES ('{}', '{}', '{}')
        """.format('Channel', 'Dimmer', 'Address', ItemList[1], ItemList[2], ItemList[3]))
    file.commit()
    file.close()
    #print(ItemList[i])
    i += 1
    #print('t')



def Read(FN):
    LW = open(FN, 'r')
    attr = LW.readline()
    attrSplit = re.split('\t|,', str(attr))
    MakeDB(attrSplit, FN)
    for line in LW:
        #print(line)
        item = re.split('\t|,', str(line))
        AddToDB(item)
        #break
    LW.close()

#https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/
#https://www.w3schools.com/sql/sql_alter.asp
