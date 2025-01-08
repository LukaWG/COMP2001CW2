class AccountInformation:
    def __init__(self):
        self.userID = None
        self.emailAddress = None
        self.isLoggedIn = False
        self.isAdmin = False

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

    def is_admin(self):
        return self.isAdmin
    
    def set_admin(self, isAdmin):
        self.isAdmin = isAdmin