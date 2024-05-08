import json

from cffi.backend_ctypes import unicode

from modules.base import CharDB
import faker

faker_obj = faker.Faker()

'''
dbase = MongoDB()

faker_obj = faker.Faker()

user_profile = faker_obj.simple_profile()
user_profile['birthdate'] = user_profile['birthdate'].strftime('%d/%m/%Y')
print(user_profile)

#dbase.create_user(user_profile)'''

char_base = CharDB()


def get_test():
    char = char_base.find_by_name("Уэллби")
    print(char)
    print(type(char))
    char_str = json.dumps(char)
    print(char_str)
    print(type(char_str))
    char = {k: unicode(v).encode("utf-8") for k, v in char.items()}
    print(char)
    print(type(char))


char_profile = {
    'isDefault': True,
    'jsonType': 'character',
    'template': 'default',
    'name': {
        'value': 'Third'
    },
    'info': {
        'charClass': {
            'name': 'charClass',
            'label': 'класс и уровень',
            'value': 'Жрец(Домен сумрака)'
        },
        'level': {
            'name': 'level',
            'label': 'уровень',
            'value': 3
        }}}
print(char_profile['name'])
creation = char_base.create_char(char_profile)
