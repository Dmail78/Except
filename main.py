from typing import Any


class Check_User_data(Exception):
    def __init__(self, message = "Данные некорректны") -> None:
        super().__init__(message)

class UserAlreadyExistsError(Exception):
# Исключение, выбрасываемое, если пытаются добавить пользователя с уже существующим именем.
    def __init__(self, message = "Попытка добавить пользователя с уже существующим именем") -> None:
        super().__init__(message)

class UserNotFoundError(Exception):
# Исключение, выбрасываемое, если пользователь с указанным именем не найден.
    def __init__(self, message = "пользователь с указанным именем не найден") -> None:
        super().__init__(message)



class User(): 
    def __new__(cls, *args, **kwargs):
        username, email, age = args
        mes_user_not = f"Пользователь с данными {args} не создан"
        if not isinstance(username, str) or not isinstance(email, str):
                 raise Check_User_data(f" {mes_user_not}, имя пользователя или адрес эл.почты имеет не строковый тип")
        if not isinstance(age, int):
                 raise Check_User_data(f" {mes_user_not}, возраст имеет не целочисленный тип")
        elif age <= 0:
                raise Check_User_data(f" {mes_user_not}, возраст не может быть отрицательный или равен 0")
        res = super().__new__(cls)
        print(f"Пользователь {username} создан")
        return res
    
    def __init__(self, username:str, email:str, age:int) -> None:
        self.username = username
        self.email = email
        self.age = age 
    
    def __str__(self) -> str:
        return f"Имя пользователя: {self.username}; Email: {self.email}; Возраст: {self.age}"



class UserManager():
    def __init__(self) -> None:
        self.users = {}
        
    def add_user(self, user):
        if user in self.users.values():
                raise UserAlreadyExistsError()
        else:
            self.users[user.username] = user
        
    
    def remove_user(self, user):
        if user in self.users.values():
                del self.users[user.username]
        else:
            raise UserNotFoundError()
    
    def find_user(self, user):
        if user in self.users.values():
                print(user)
        else:
            raise UserNotFoundError()
    
# Проверка пользователя
users_list = []
tests_user = [("user1", "user1@mail.ru", 25), ("user1", "user1@mail.ru", -5), (1, "user1@mail.ru", 25),("user1", 1, 25) ]
for user in tests_user:
    try:
        users_list.append(User(*user)) 
    except Check_User_data as cud:
        print(cud)
print(f"Итого из {len(tests_user)} возможных пользователей создано {len(users_list)} пользователей")

user_manager = UserManager()
temp = users_list[0]

print("Проверяем на добавление существующего пользователя")
user_manager.add_user(temp)
try:
    user_manager.add_user(temp)
except Exception as e:
    print(e.__class__.__name__, e)
print()

print("Проверяем на удаление несуществующего пользователя")
user_manager.remove_user(temp)
try:
    user_manager.remove_user(temp)
except Exception as e:
    print(e.__class__.__name__, e)
print()

print("Проверяем на поиск  несуществующего пользователя")
user_manager.add_user(temp)
user_manager.find_user(temp)
user_manager.remove_user(temp)
try:
    user_manager.find_user(temp)
except Exception as e:
    print(e.__class__.__name__, e)
    