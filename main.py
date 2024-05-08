
from modules.base import CharDB
import faker


#dbase = MongoDB()

faker_obj = faker.Faker()

user_profile = faker_obj.simple_profile()
user_profile['birthdate'] = user_profile['birthdate'].strftime('%d/%m/%Y')
print(user_profile)

#dbase.create_user(user_profile)
#dbase.get_all_users()

char_base = CharDB()

char_base.test()
print(char_base.find_by_name("Уэллби Мертвослав"))

