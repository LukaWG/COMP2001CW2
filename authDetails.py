class AccountInformation:
    def __init__(self):
        self.userID = None
        self.emailAddress = None
        self.isLoggedIn = False

    def login(self, emailAddress):
        self.emailAddress = emailAddress
        self.isLoggedIn = True

    def logout(self):
        try:
            self.userID = None
            self.emailAddress = None
            self.isLoggedIn = False
            return True
        except AttributeError:
            return False
        return False
    def is_logged_in(self):
        return self.isLoggedIn
    
    def get_email_address(self):
        return self.emailAddress
    
    def get_user_id(self):
        return self.userID
    
    def set_user_id(self, userID):
        self.userID = userID