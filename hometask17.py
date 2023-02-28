# Необходимо создать класс Human с атрибутами:
# name # surname # age # phone # address
# Атрибуты должны заполняться в методе __init__
# Так-же нужно написать методы:
# get_info() - который возвращает словарь в котором находится информация о человеке
# call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
# Нужно создать 3 обьекта класса Human и вызвать у них метод get_info


class Human:
    def __init__(self, name: str, surname: str, age: int, phone: int, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        my_dict = {'name': {self.name}, 'surname': {self.surname}, 'age': {self.age}, 'phone': {self.phone},
                   'address': {self.address}}
        print(my_dict)

    def call(self, phone_number: int):
        print(f'{self.phone} вызывает абонента {phone_number}')


human_1 = Human("Tom", "Hens", 23, +10235680912, "Wales street, 30")
human_2 = Human('Oleg', "Vaselenko", 40, +380632063050, "Derebasovskaya street, 7")
human_3 = Human('Maria', "Ivanova", 27, +380990158996, "Lozenko steet, 4")

human_1.get_info()
human_2.get_info()
human_3.get_info()
human_2.call(+10232523523)
