class topicCommands:
    def topicCommandsCheck():
        if connectCommand[0] == "imq" and connectCommand[1]=="connect":
 		    if connectCommand[2] is in topicList:
 				 connectCommand[2], operateCommand[1];
 			else:
 				print("topic does not exist")
 				exit()
 		else:
 			print("Not a valid command")
 			exit()	
