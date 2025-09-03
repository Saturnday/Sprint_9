from faker import Faker
import random

fake = Faker("ru_RU")

class UserData:

    @staticmethod
    def generate_valid_user():
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = fake.user_name()
        email = fake.email()
        password = fake.password()

        return {
            "first_name": first_name,
            "last_name": last_name,
            "user_name": username,
            "email": email,
            "password": password
        }
    @staticmethod
    def generate_valid_recipe():
        name=fake.color_name()
        ingredient = 'абри'
        amount=random.randint(5, 100)
        time=random.randint(1, 60)
        description = fake.color_name()


        return {
            "name": name,
            "amount": amount,
            "time": time,
            "description": description,
            "ingredient": ingredient
        }