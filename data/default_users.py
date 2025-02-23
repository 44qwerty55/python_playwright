import os
from dotenv import load_dotenv

from model.user import User

load_dotenv()

class DefaultUsers:
    def __init__(self):
        self.users = [
            User("standard_user", os.getenv("DEFAULT_PASSWORD")),
            User("problem_user", os.getenv("DEFAULT_PASSWORD")),
            User("performance_glitch_user", os.getenv("DEFAULT_PASSWORD")),
            User("error_user", os.getenv("DEFAULT_PASSWORD")),
            User("visual_user", os.getenv("DEFAULT_PASSWORD")),
        ]

    def get_users(self):
        return self.users

    def get_user_by_name(self, name: str):
        for user in self.users:
            if user.get_name() == name:
                return user
        return None

    def get_standard_user(self):
        return self.get_user_by_name("standard_user")

    def get_problem_user(self):
        return self.get_user_by_name("problem_user")

    def get_performance_glitch_user(self):
        return self.get_user_by_name("performance_glitch_user")

    def get_error_user(self):
        return self.get_user_by_name("error_user")

    def get_visual_user(self):
        return self.get_user_by_name("visual_user")
