Users = []

class UsersReg:
    """docstring for UsersReg"""
    def __init__(self, username, email, pwd):
        self.username = username
        self.email = email
        self.pwd = pwd

    def addUsersReg(username, email, pwd):
        if username == '' or email =='' or pwd == '':
            return {'status': False, 'message': "you can't leave a field empty. Are you crazy"}

        else:
            UserDetails = {}
            UserDetails['username'] = username
            UserDetails['email'] = email
            UserDetails['pwd'] = pwd

            Users.append(UserDetails)

            return {'status': True, 'UsersReg': Users}




		