import socket
from Constants import *
import sys
from Request import *
from Parser import *


class Client:
    def createSocket(self):
        try:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Client Socket successfully created")
        except socket.error as err:
            print("socket creation failed with error %s" % (err))
        return clientSocket

    def connectToServer(self, clientSocket):
        try:
            clientSocket.connect((HOST, PORT))
        except socket.error as errorMessage:
            print(str(errorMessage))
            exit()

    def receiveMessageFromServer(self, clientSocket):
        response = clientSocket.recv(maxMessageSize)
        return response.decode(decodingType)

    def sendMessageToServer(self, clientSocket, message):
        clientSocket.send(str.encode(message))

    def closeSocket(self, clientSocket):
        clientSocket.close()



def clientStart(message):
    clientInstance = Client()
    clientSocket = clientInstance.createSocket()
    print("waiting for connection with server")
    try:
        clientInstance.connectToServer(clientSocket)
        response = clientInstance.receiveMessageFromServer(clientSocket)
        requestObject = Request(message, HOST, HOST)
        request = Parser().serializeToJsonConvertor(requestObject)
        clientInstance.sendMessageToServer(clientSocket, request)
        response = clientInstance.receiveMessageFromServer(clientSocket)
        responseJsonMessage = Parser().deserializeJsonFormattedData(response)
        Response = responseJsonMessage['data']
        print(Response)
        # print(responseJsonMessage)
        # print(responseJsonMessage['data'] +
        #     "\n"+responseJsonMessage['status'])
        clientInstance.closeSocket(clientSocket)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
    return Response




def publisher_service(UserId):
    UserId =UserId
    while True:
        print("Please Select from the list below:-")
        print("CLIENT: Topic List")
        print("CLIENT: Register to new topic")
        print("CLIENT: Back")
        print("CLIENT: choose from above")
        choice = input()
        if choice.lower() == 'topic list':
            Input = ''
            InputType = ' -topiclist'
            message = Input+InputType
            Response = clientStart(message)
            Return, ReturnType = Response.split(' -')
            TopicList = list(Return.split(" ")) 
            for Topic in TopicList:
                print(Topic)
            while True:
                print("Please Select from the list below:-")
                print("CLIENT: Choose Topic")
                print("CLIENT: Register to new topic")
                print("CLIENT: Back")
                print("Choose from above")
                choice2 = input()
                if choice2.lower() == 'choose topic':
                    print("Enter your choice")
                    TopicName = input()
                    InputType = ' -topicname'
                    message = TopicName+InputType
                    Response = clientStart(message)
                    TopicId,ReturnType = Response.split(' -')
                    print("Please Select from the list below:-")
                    print("CLIENT: Push message")
                    print("CLIENT: Back")
                    choice3 = input()
                    if choice3.lower() =='push message' :
                        print("Enter your message")
                        Message = input()+" ,"+UserId+" ,"+TopicId
                        InputType = ' -pushMessage'
                        message = Message+InputType
                        Response = clientStart(message)
                        Return,ReturnType = Response.split(' -')
                        if ReturnType == 'MessageAdded':
                            print(Return)
                    elif choice3.lower() == 'back':
                        break
                elif choice2.lower() == 'register to new topic':
                    n=1
                    while n == 1:
                        print("Enter Topic Name")
                        TopicName = input()
                        InputType = ' -TopicToRegister'
                        message = TopicName+InputType
                        Response = clientStart(message)
                        Return,ReturnType = Response.split(' -')
                        #CheckForTopicName = databaseObject.CheckTopicName(TopicName)
                        if ReturnType == "TopicAdded":
                            n = 0
                            print(Return)
                            #databaseObject.AddTopic(TopicName)
                        elif ReturnType == "TopicExists":
                            print("TopicName Exsits")
                    break
                elif choice2.lower() == 'break':
                    break
        elif choice.lower() == 'register to new topic':
            n=1
            while n == 1:
                print("Enter Topic Name")
                TopicName = input()
                InputType = ' -TopicToRegister'
                message = TopicName+InputType
                Response = clientStart(message)
                Return,ReturnType = Response.split(' -')
                        
                #CheckForTopicName = databaseObject.CheckTopicName(TopicName)
                if ReturnType == "TopicAdded":
                    n = 0
                    print(Return)
                    #databaseObject.AddTopic(TopicName)
                elif ReturnType == "TopicExists":
                    print("TopicName Exsits")
            break
        elif choice.lower() == 'back':
            break




def subscriber_service(UserId):
    UserId = UserId
    while True:
        print("Please Select from the list below:-")
        print("CLIENT: Topic List")
        print("CLIENT: Acknowledge to topic")
        print("CLIENT: Back")
        print("choose from above")
        choice = input()
        if choice.lower() == 'topic list':
            Input = ''
            InputType = ' -topiclist'
            message = Input+InputType
            Response = clientStart(message)
            Return, ReturnType = Response.split(' -')
            TopicList = list(Return.split(" "))  
            for Topic in TopicList:
                print(Topic)      
            #databaseObject.TopicList()
            while True:
                print("Please Select from the list below:-")
                print("CLIENT: Choose Topic")
                print("CLIENT: Back")
                print("choose from above")
                choice2 = input()
                if choice2.lower() == 'choose topic':
                    print("Enter your choice")
                    TopicName = input()
                    InputType = ' -topicname'
                    message = TopicName+InputType
                    Response = clientStart(message)
                    TopicId,ReturnType = Response.split(' -')
                    break
                elif choice2.lower() == 'back':
                    break
        elif choice.lower() =='acknowledge to topic' :
            print("Acknowlege to topic")
        elif choice.lower() == 'back':
            break
    



def client_service(UserId):
    UserId =UserId
    #PublisherObject = Publisher()
    #SubscriberObject = Subscriber()
    while True:
        print("Please Select from the list below:-")
        print("CLIENT: Login as publisher")
        print("CLIENT: Login as subscriber")
        print("CLIENT: Back")
        choice = input()
        if choice.lower() == 'login as publisher':
            print("Logging in as publisher")
            publisher_service(UserId)
            #PublisherObject.publisher_service(UserId)      
        elif choice.lower() == 'login as subscriber':
            print("Logging in as subscriber")
            subscriber_service(UserId)
            #SubscriberObject.subscriber_service(UserId)
        elif choice.lower() == 'back':
            break





def Login_Service():
    while True:
        print("Please Select from the list below:-")
        print("CLIENT: Login ")
        print("CLIENT: Signup")
        choice = input()
        if choice.lower() == 'login':
            n=1
            while n == 1:
                print("Enter User Name0")
                UserName = input()
                message = UserName+' -usernameforlogin'
                Response = clientStart(message)
                Return, ReturnType = Response.split(' -')
                if ReturnType == "No Match For Login":
                    n = 0
                    print("User does not exist")
                    print("Do you want to signup? Y/N")
                    choice2 = input()
                    if choice2 == 'Y':
                        choice = 'signup'
                    break
                else:
                    UserId = Return
                    client_service(UserId)
                   # client_object.client_service(UserId)
                    break
        if choice.lower() == 'signup':
            n=1
            while n == 1:
                print("Enter User Name3")
                UserName = input()
                message = UserName+' -usernameforsignup'
                Response = clientStart(message)
                Return, ReturnType = Response.split(' -')
                if ReturnType == "UserSignUp":
                    n = 0
                    UserId = Return
                    print(UserId)
                    client_service(UserId)
                    #client_object.client_service(UserId)
                    break
                elif ReturnType == 'UserAlreadyExist':
                    print("User already exists")
                    print("Do you want to Login? Y/N")
                    choice2 = input()
                    if choice2 == 'Y':
                        choice = 'login'
                    break
            
        
Login_Service()
