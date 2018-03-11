
class User():

    def __init__(self, email, password, created_at, activated):
        self.email = email
        self.password = password
        self.created_at = created_at
        self.activated = activated


    def json(self):
        return {'email':self.email,'password':self.password,'created_at':self.created_at,'activated':self.activated}
