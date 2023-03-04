class npsp_connection:
    def __init__(self, username, password, security_token):
        self.username = username
        self.password = password
        self.security_token = security_token
        self.sf = None
        
    def connect(self):
        from simple_salesforce import Salesforce
        self.sf = Salesforce (username=self.username, password=self.password, security_token=self.security_token)