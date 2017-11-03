Users = []

class UsersReg:

    """docstring for UsersReg"""
    def __init__(self, username, email, pwd):
        self.username = username
        self.email = email
        self.pwd = pwd

    def addUsersReg(username, email, pwd):
        response = checkUser(username,pwd)
        response2 = checkUser(email, pwd)
        if username == '' or email =='' or pwd == '':
            return {'status': False, 'message': "you can't leave a field empty. Are you crazy"}

        elif response2['status'] == True or response['status'] == True:
            return {'status': False, 'message' : "Sorry but it seems a user by that username or email exists"}

        else:
            UserDetails = {}
            UserDetails['username'] = username
            UserDetails['email'] = email
            UserDetails['pwd'] = pwd

            Users.append(UserDetails)

            return {'status': True, 'UsersReg': Users}

def checkUser(username, pwd2):

    if Users == []:
        return {'status':False}
    else:    
        for uDetails in Users:
            
            for key, value in uDetails.items():
                
                if value == username:
                    if uDetails['pwd'] == pwd2:
                        return {'status':True, 'realName': uDetails['username']}
                    else:
                        return {'status':False, 'message' :"Your username or password don't match!!"}
                
        return {'status':False, 'message' :"You are not registered. Please Register!!!"}
        
