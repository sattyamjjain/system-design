class UserInfoService:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password, email):
        if username in self.users:
            raise Exception("User already exists")
        self.users[username] = {"password": password, "email": email, "profile": {}}

    def authenticate_user(self, username, password):
        if username not in self.users:
            return False
        return self.users[username]["password"] == password

    def get_user_profile(self, username):
        if username not in self.users:
            return None
        return self.users[username]["profile"]

    def update_user_profile(self, username, profile):
        if username not in self.users:
            return False
        self.users[username]["profile"] = profile
        return True

    def delete_user(self, username):
        if username not in self.users:
            return False
        del self.users[username]
        return True
