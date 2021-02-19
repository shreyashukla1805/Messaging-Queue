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




def clientStart():
    clientInstance = Client()
    clientSocket = clientInstance.createSocket()
    print("waiting for connection with server")
    try:
        clientInstance.connectToServer(clientSocket)
        response = clientInstance.receiveMessageFromServer(clientSocket)
        userID =''
        TopicId = ''
        print(response)
        while True:
            message = input("Say Something\n")
            if userID == '' and TopicId == '':
                messagedata = message+' --  -- '
            elif userID != '' and TopicId == '':
                messagedata = message+' --'+userID+' -- '
            elif userID != '' and TopicId != '':
                messagedata = message+' --'+userID+ ' --'+TopicId
            print(messagedata)
            requestObject = Request(messagedata, HOST, HOST)
            request = Parser().serializeToJsonConvertor(requestObject)
            clientInstance.sendMessageToServer(clientSocket, request)
            response = clientInstance.receiveMessageFromServer(clientSocket)
            responseJsonMessage = Parser().deserializeJsonFormattedData(response)
            Return, ReturnType = responseJsonMessage['data'].split(" --")
            if ReturnType == 'UserId':
                userID = Return
                print(userID)
            elif ReturnType == 'TopicId':
                TopicId = Return
                print(TopicId)
            elif ReturnType == 'printStage1Commands':
                print("You can enter the following commands: ")
                print("imq login --<Username>")
                print("imq signup --<Username>")
            elif ReturnType == 'printStage2Commands':
                print("You can enter the following commands: ")
                print("imq topiclist --t")
                print("imq topicname --<Topic Name>")
                print("imq add_topic --<Topic Name>")
            elif ReturnType == 'printStage3Commands':
                print("You can enter the following commands: ")
                print("imq pushmessage --<message.")
                print("imq pullmessage --p")
            
            if message.lower() == 'stop':
                break
            print(responseJsonMessage['data'] +
                  "\n"+responseJsonMessage['status'])
        clientInstance.closeSocket(clientSocket)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")




clientStart()
