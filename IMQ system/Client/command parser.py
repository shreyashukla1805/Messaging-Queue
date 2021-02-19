class commandParser:
    def commandCheck(message):
        if message[0:3] == 'imq':
            print("execute")
            command, Input = message.split(" -")
            command = command[4:]
            if command == 'login':
                
        else :
            exit()

        # command, Input = message.split(' -')
        # command = command[4:]
        # if command == 'login':
        #     elif command =='signup':
        #     message = Input+' -'+command
        #     return message
        # elif command =='topic_list':
        #     message = Input+' -'+command
        #     return message
        # else :
        #     message = 'stop'
        #     return message
#         topicList = [topicnames]
# int(input(Enter your ID:-)) Exception ID should be integer
# connectCommand = input(Enter the command with valid topic name to connect to topicqueue:-"imq connect {topicname}")
# ---------> connectCommand.split(" ")
# 		if(connectCommand[0] == "imq" && connectCommand[1]=="connect"):
# 			if(connectCommand[2] is in topicList):-
# 				send connectCommand[2], operateCommand[1];
# 			else:
# 				print("topic does not exist")
# 				exit()
# 		else:
# 			print("Not a valid command")
# 			exit()	
# print("Use command to operate:-")
# print("1. imq publish message
#        2. imq push message"
#        3. imq create topicname")
# operateCommand = input()
# ---------> operateCommand.split(" ")
# 		if(operateCommand[0] == "imq" && operateCommand[1]=="publish"):
# 			if(operateCommand[2] is in topicList):-
# 				send operateCommand[2], operateCommand[1];
# 			else:
# 				print("topic does not exist")
# 				exit()
# 		elif(operateCommand[0] == "imq" && operateCommand[1]=="pull"):
# 			if(operateCommand[2] is in topicList):-
# 				send operateCommand[2], operateCommand[1];
# 			else:
# 				print("topic does not exist")
# 				exit()
# 		elif(operateCommand[0] == "imq" && operateCommand[1]=="create"):
# 			if(operateCommand[2] is in topicList):-
# 				print("topic exist")
# 				exit()
# 			else:
# 				send operateCommand[2], operateCommand[1];
# 		else:
# 			print("Not a valid command")
# 			exit()	

