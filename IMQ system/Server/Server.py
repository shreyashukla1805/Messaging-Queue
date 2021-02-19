import socket
from _thread import *
from Constants import *
from Response import *
from Parser import *
from ServerFunctions import *


class Server:
    def createSocket(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return serverSocket

    def checkSocketStatus(self, serverSocket):
        if serverSocket is None:
            print("Oops! Something went wrong, please try again later...")
        print("Server Socket successfull ")

    def bindServerSocket(self, serverSocket):
        try:
            serverSocket.bind((HOST, PORT))
        except socket.error:
            print("Right now not able to bind with socket")
            exit()

    def putServerToListeningMode(self, serverSocket):
        serverSocket.listen(maximumNoOfConnections)
        print('Server is listening for connections.\.\.')

    def makeConnectionToClient(self, serverSocket):
        return serverSocket.accept()

    def connectToClient(self, serverSocket):
        while True:
            clientConnection, IPAddress = self.makeConnectionToClient(
                serverSocket)
            print('Connected to: ' + IPAddress[0] + ":" + str(IPAddress[1]))
            clientTableName = "client"+"_"+str(IPAddress[1])
            try:
                start_new_thread(
                    self.start_new_client_thread, (clientConnection, IPAddress))
            except:
                print("Oops! Something went wrong, please try again later...")

    def start_new_client_thread(self, clientConnection, IPAddress):
        self.sendMessageToClient(
            clientConnection, "Hey Client, Welcome to the Server!\n")
        
        while True:
            response = self.receiveMessageFromClient(clientConnection)
            clientJsonMessage = Parser().deserializeJsonFormattedData(response)
            if clientJsonMessage['data'].lower() == 'stop':
                break
            # try:
            #     databaseObject.saveServerClientDataToDataBase(
            #         databaseConnection, databaseCursor, str(IPAddress), clientJsonMessage['data'])
            # except:
            #     print("Not able to save the data in table, please check the enter")
            #     exit()
            responseObject = self.getResponseObject(clientJsonMessage)
            response = Parser().serializeToJsonConvertor(responseObject)
            self.sendMessageToClient(clientConnection, response)
        clientConnection.close()

    def sendMessageToClient(self, connection, message):
        connection.sendall(str.encode(message))

    def receiveMessageFromClient(self, connection):
        data = connection.recv(maxMessageSize)
        return data.decode(decodingType)

    def getResponseObject(self, clientJsonObject):
        data = clientJsonObject['data']
        ServerFunctionObject = ServerFunction()
        ReturnData = ServerFunctionObject.CommandCompare(data)
        sourceIp = HOST
        desitantionIP = HOST
        responseObject = Response(ReturnData, sourceIp, desitantionIP)
        print(responseObject)
        return responseObject
    
    

    def closeSocket(self, serverSocket):
        serverSocket.close()


def main():
    serverObject = Server()
    serverSocket = serverObject.createSocket()
    serverObject.checkSocketStatus(serverSocket)
    serverObject.bindServerSocket(serverSocket)
    serverObject.putServerToListeningMode(serverSocket)
    serverObject.connectToClient(serverSocket)
    serverObject.closeSocket(serverSocket)


main()
