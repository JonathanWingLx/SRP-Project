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
    print(len(col))
    print(colNum)
    #print(colNum)
    cs.execute("CREATE TABLE IF NOT EXISTS {}({} TEXT)".format('DB_'+fileName[-1], col[0]))
    file.commit()
    for x in range(colNum):
        i += 1
        e = 0
        print(x)
        if col[i] == 'When':
            col[i] = col[i]+col[i+1]
            col[i] = col[i]+col[i+2]
            e = 1
        col[i] = col[i].replace('#', '')
        col[i] = col[i].replace(' ', '_')
        col[i] = col[i].replace('/', '_')
        col[i] = col[i].replace('"', '')
        col[i] = col[i].replace('&', 'and')
        #if col[i] = 'When' then col[i] + col[i+1] + col[i+2] .join
        #then delete col[i+1] and col[i+2]
        if col[i] == 'When':
            col[i] = col[i]+col[i+1]
            col[i] = col[i]+col[i+2]
            print(col[i])
        cs.execute("ALTER TABLE {} ADD {} TEXT".format('DB_'+fileName[-1], col[i]))

        file.commit()
        if e == 1:
            e += 2
            e = 0
    file.close()

def AddToDB(ItemList, fileName):
    i = 0
    file = connect("Test.db")
    cs = file.cursor()
    fileName = fileName.replace(' ', '_')
    fileName = fileName.split('/')
    #print(ItemList)
    cs.execute("""
        INSERT INTO {} VALUES
        ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
         '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
         '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
         '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
         '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
         '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
         '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
         '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',
         '{}', '{}', '{}', '{}', '{}')
        """.format('DB_'+fileName[-1], ItemList[0],
ItemList[1], ItemList[2], ItemList[3], ItemList[4], ItemList[5],
ItemList[6], ItemList[7], ItemList[8], ItemList[9], ItemList[10],
ItemList[11], ItemList[12], ItemList[13], ItemList[14], ItemList[15],
ItemList[16], ItemList[17], ItemList[18], ItemList[19], ItemList[20],
ItemList[21], ItemList[22], ItemList[23], ItemList[24], ItemList[25],
ItemList[26], ItemList[27], ItemList[28], ItemList[29], ItemList[30],
ItemList[31], ItemList[32], ItemList[33], ItemList[34], ItemList[35],
ItemList[36], ItemList[37], ItemList[38], ItemList[39], ItemList[40],
ItemList[41], ItemList[42], ItemList[43], ItemList[44], ItemList[45],
ItemList[46], ItemList[47], ItemList[48], ItemList[49], ItemList[50],
ItemList[51], ItemList[52], ItemList[53], ItemList[54], ItemList[55],
ItemList[56], ItemList[57], ItemList[58], ItemList[59], ItemList[60],
ItemList[61], ItemList[62], ItemList[63], ItemList[64], ItemList[65],
ItemList[66], ItemList[67], ItemList[68], ItemList[69], ItemList[70],
ItemList[71], ItemList[72], ItemList[73], ItemList[74], ItemList[75],
ItemList[76], ItemList[77], ItemList[78], ItemList[79], ItemList[80],
ItemList[81], ItemList[82], ItemList[83], ItemList[84]))
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
        AddToDB(item, FN)
        #break
    LW.close()

#https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/
#https://www.w3schools.com/sql/sql_alter.asp
