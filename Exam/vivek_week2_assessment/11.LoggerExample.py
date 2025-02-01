# •	11. Create a class `Logger` with a method `log(message)`. 
# Implement method overloading to log different message types 
# (`error`, `warning`, `info`).
class Logger:
    def log(self,message:str):
        print(message)
    
    def log(self,message:str,message_type:str):
        if message_type=="error":
            print(f"Error: {message}")
    def log(self,message:str,message_type:str):
        if message_type=="warning":
            print(f"Warning: {message}")
    def log(self,message:str,message_type:str):
        if message_type=="info":
            print(f"Info: {message}")

message_type,message=map(str,input("Enter message type and message: ").split())
logger1=Logger()    
logger1.log(message,message_type)
