from models.user import UserModel
from werkzeug.security import safe_str_cmp  #For safe string comparison including encoding


def authenticate(username, password):
    ''' This func will be called when user logins for the 1st time and generate jwt'''
    user = UserModel.find_by_username(username) 
    if user and safe_str_cmp(user.password, password):
        return user
    
def identity(payload):
    ''' This function will be called for verifying the authenticity of JWT'''
    user_id=payload['identity'] #JWT payload will contain identity info
    return UserModel.find_by_id(user_id)
