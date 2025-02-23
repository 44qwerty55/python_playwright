class User:

    def __init__(self, name: str, password: str):
        self.__name = name
        self.__password = password

    def get_name(self) -> str:
        return self.__name

    def get_password(self) -> str:
        return self.__password

    def set_name(self, name: str):
        self.__name = name

    def set_password(self, password: str):
        self.__password = password
