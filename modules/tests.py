from modules.base import MongoDB, CharDB
import faker

'''
dbase = MongoDB()

faker_obj = faker.Faker()

user_profile = faker_obj.simple_profile()
user_profile['birthdate'] = user_profile['birthdate'].strftime('%d/%m/%Y')
print(user_profile)

#dbase.create_user(user_profile)'''

char_base = CharDB()

# char_base.test()
print(char_base.find_by_name("Уэллби Мертвослав"))

