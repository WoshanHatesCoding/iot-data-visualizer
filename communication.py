class Communication:
    def __init__(self,on_send=None,on_receive = None):
        self.on_receive = on_receive
        self.on_send = on_send
        
    def send_data(self,data):
        if self.on_send != None:
            self.on_send(data)
        
    def receive_data(self, data):
        if self.on_receive != None:
            self.on_receive()
        

