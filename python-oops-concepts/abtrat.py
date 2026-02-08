#  Abstraction 

class SendEmail:
    def _connect(self):
        print("connecting to server ")
        
    def _authenticate(self):
        print("authentication of the email")
        
    def send(self):
        self._connect()
        self._authenticate()
        print("sending the email")
        self._disconnect()
        
    def _disconnect(self):
        print("disconnecting the email")
    
    
email=SendEmail()
email.send()