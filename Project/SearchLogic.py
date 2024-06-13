from sqlite3 import *

def Search(FN, C1, C2):
    #print("Test")

    file = connect("Test.db")
    cs = file.cursor()
    FN = FN.replace(' ', '_')
    FN = FN.split('/')
    FN = 'DB_'+FN[-1]



    if C1 == 0:
        print("Missing")
        print(FN)
        cs.execute("""SELECT * FROM {} WHERE {} IS ''
            """.format(FN, C2))
        return cs.fetchall()
    elif C1 == 1:
        print("Duplicate")
        cs.execute("""SELECT * FROM {} WHERE {} IN
                     (SELECT {} FROM {} GROUP BY {} HAVING COUNT(*) > 1 AND {} IS NOT NULL)
                   """.format(FN, C2, C2, FN, C2, C2))
        return cs.fetchall()


        #file = connect("Test.db")
        #cs = file.cursor()
        #fileName = fileName.replace(' ', '_')
        #fileName = fileName.split('/')

#SELECT Channel, Dimmer FROM DB_9_to_5_Paperwork_Exported_Data
#WHERE Dimmer IN (SELECT Dimmer FROM DB_9_to_5_Paperwork_Exported_Data
#GROUP BY Dimmer HAVING COUNT(*) > 1 AND Dimmer IS NOT NULL)

#        col[i] = col[i].replace('#', '')
#        col[i] = col[i].replace(' ', '_')
#        col[i] = col[i].replace('/', '_')
#        col[i] = col[i].replace('"', '')
#        col[i] = col[i].replace('&', 'and')
