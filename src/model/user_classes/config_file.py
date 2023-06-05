import json


class ConfigFile:
    USER_PATH = "data_persistence/users.json"

    @staticmethod
    def save_user(new_json_user):
        with open(ConfigFile.USER_PATH, 'r+') as file:
            already_exist = False
            users = json.load(file)
            for user in users:
                if user["_User__student_id"] == new_json_user["_User__student_id"]:
                    already_exist = True
                    print("Sorry, this student id already exits.")
                    break
            if not already_exist:
                users.append(new_json_user)
                file.seek(0)
                json.dump(users, file, indent=4)
                print("Registered!")
