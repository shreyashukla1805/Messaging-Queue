from Database_connection import *
class ServerFunction:
    def CommandCompare(self,data):
        message = ''
        DatabaseObject = databaseInsert()
        InputType,Input,UserId,TopicId = data.split(' --')
        print(Input,InputType,UserId,TopicId)

        if UserId == ' ' and TopicId ==' ':
            if InputType == 'imq login':
                CheckForUsername = DatabaseObject.CheckUserName(Input)
                if CheckForUsername == 'No Match':
                    Return = '0'
                    ReturnType = 'Login does not exist' 
                    message = Return+ReturnType
                else :
                    Return = DatabaseObject.GetUserID(Input)
                    ReturnType = ' --UserId'
                    message =  Return+ReturnType
                    
            elif InputType == 'imq signup':
                CheckForUsername = DatabaseObject.CheckUserName(Input)
                if CheckForUsername == 'No Match':
                    DatabaseObject.AddUser(UserName)
                    Return = DatabaseObject.GetUserID(Input)
                    ReturnType = ' --UserSignUp'
                    message =  Return+ReturnType
                else:
                    Return = '0'
                    ReturnType = ' --UserAlreadyExist'
                    message =  Return+ReturnType
            else :
                Return = '0'
                ReturnType = ' --printStage1Commands'
                message =  Return+ReturnType


        elif UserId != ' ' and TopicId ==' ':
            if InputType == 'imq topiclist':
                Return = DatabaseObject.TopicList()
                ReturnType = ' --topiclist'
                message =  Return+ReturnType

            elif InputType == 'imq topicname':
                Return = DatabaseObject.ChooseTopicName(Input)
                ReturnType = ' --TopicId'
                message =  Return+ReturnType

            elif InputType == 'imq add_topic':
                CheckForTopicName = DatabaseObject.CheckTopicName(Input)
                if CheckForTopicName == "No Match":
                    n = 0
                    DatabaseObject.AddTopic(Input)
                    Return = DatabaseObject.ChooseTopicName(Input)
                    ReturnType = ' --TopicAdded'
                    message =  Return+ReturnType
                else:
                    Return = '0'
                    ReturnType = ' --TopicExists'
                    message =  Return+ReturnType
            else :
                Return = '0'
                ReturnType = ' --printStage2Commands'
                message =  Return+ReturnType


        elif UserId != ' ' and TopicId !=' ':
            if InputType == 'imq push_Message':
                Message,UserId,TopicId = Input.split(" ,")
                print(Message,UserId,TopicId)
                DatabaseObject.pushMessage(Message,UserId,TopicId)
                Return = 'Message pushed'
                ReturnType = '--MessageAdded'
                message =  Return+ReturnType
            else:
                Return = '0'
                ReturnType = ' --printStage3Commands'
                message =  Return+ReturnType


                
        return message