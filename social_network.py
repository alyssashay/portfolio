class User:
    # Define the fields and methods for your object here.
    def __init__ (self, user_name, password):
    	self.user_name = user_name
    	self.password = password
    	self.connections = []

    def addUsername (self):
    	return self.user_name

    def addPassword (self):
    	return self.password

    def getConnections(self):
    	return self.connections

    def addConnections(self, connections_id):
    	self.connections.append(connenction_id)
  

class Network:
    # Define the fields and methods for your object here.
    def __init__ (self):
    	self.users = []
    

def main():
    # Define the program flow for your user interface here.


# Runs your program.
if __name__ == '__main__':
    main():