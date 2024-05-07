
from modules.base import MongoDB
import faker


dbase = MongoDB(db_name='article', collection='user')

faker_obj = faker.Faker()

user_profile = faker_obj.simple_profile()
user_profile['birthdate'] = user_profile['birthdate'].strftime('%d/%m/%Y')
print(user_profile)

dbase.create_user(user_profile)



