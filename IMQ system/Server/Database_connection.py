import pyodbc
import pandas as pd
import datetime


class databaseInsert:
    def __init__(self):
        self.cnxn = pyodbc.connect('Trusted_Connection=yes',
                            driver='SQL SERVER', server='ITT-SHREYA\SHREYA',
                            database='MessagingQueue')

    
    def TopicList(self):
        queryPart1 = """
        SELECT * FROM Topic"""
        df = pd.read_sql_query(queryPart1, self.cnxn)
        val = df['TopicName']
        s = list(val)
        str1 = "" 
        for ele in s:  
            str1 += ele +"\n"
        return str1



    def ChooseTopicName(self,TopicName):
        queryPart1 = """
        SELECT TopicId FROM Topic WHERE TopicName = '"""
        queryPart2 = TopicName
        queryPart3 = """'"""
        query = queryPart1+queryPart2+queryPart3
        df = pd.read_sql_query(query, self.cnxn)
        TopicId = df['TopicId'].values[0]
        return TopicId
    
    
    def CheckTopicName(self,TopicName):
        queryPart1 = """
        SELECT IIF (EXISTS (SELECT TopicName FROM Topic WHERE TopicName ='"""
        queryPart2 = TopicName
        queryPart3 = """'), 1, 2) as TopicNameCheck"""    
        query = queryPart1+queryPart2+queryPart3
        df = pd.read_sql_query(query, self.cnxn)
        val = df['TopicNameCheck'].values[0]
        if val == 2:
            return "No Match"
        else:
            return "Match"


    def AddTopic(self,TopicName):
        cur = self.cnxn.cursor()
        queryPart1 = "EXEC InsertIntoTopic @TopicName = '"
        queryPart2 = TopicName
        queryPart3 = "';"
        query = queryPart1+queryPart2+queryPart3
        cur.execute(query)
        cur.commit()
    


    def CheckUserName(self,UserName):
        queryPart1 = """
        SELECT IIF (EXISTS (SELECT UserName FROM Users WHERE UserName ='"""
        queryPart2 = UserName
        queryPart3 = """'), 1, 2) as UserNameCheck"""    
        query = queryPart1+queryPart2+queryPart3
        df = pd.read_sql_query(query, self.cnxn)
        val = df['UserNameCheck'].values[0]
        if val == 2:
            return "No Match"
        else:
            return "Match"


    def AddUser(self,UserName):
        cur = self.cnxn.cursor()
        queryPart1 = "EXEC InsertIntoUsers @Username = '"
        queryPart2 = UserName
        queryPart3 = "';"
        query = queryPart1+queryPart2+queryPart3
        cur.execute(query)
        cur.commit()



    def GetUserID(self,UserName):
        queryPart1 = """
        SELECT UserId FROM Users WHERE UserName = '"""
        queryPart2 = UserName
        queryPart3 = """'"""
        query = queryPart1+queryPart2+queryPart3
        df = pd.read_sql_query(query, self.cnxn)
        UserId = df['UserId'].values[0]
        return UserId
    

        

    def pushMessage(self,Message,UserId,TopicId):
        cur = self.cnxn.cursor()
        queryPart1 = "exec InsertIntoMessage "
        queryPart2 = Message
        queryPart3 = ",'"
        queryPart4 = UserId
        queryPart5 = "','"
        queryPart6 = TopicId
        queryPart7 = "';"
        query = queryPart1+queryPart2+queryPart3+queryPart4+queryPart5+queryPart6+queryPart7
        cur.execute(query)
        cur.commit()


    
if __name__ == '__main__':
    d= databaseInsert()
    d.CheckTopicName()
    d.ChooseTopicName(input("Enter topic Name"))
    d.InsertIntoMessage(input('Enter SerialNumber'),input("Message"))