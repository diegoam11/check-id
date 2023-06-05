from .config_file import ConfigFile


class User:
    def __init__(self, first_name: str, last_name: str, student_id: int):
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name

    @staticmethod
    def register():
        first_name = input("Name: ")
        last_name = input("Lastname: ")
        student_id = int(input("Student id: "))
        new_user = {"_User__student_id": student_id, "_User__first_name": first_name, "_User__last_name": last_name}
        ConfigFile.save_user(new_user)

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_student_id(self):
        return self.__student_id

