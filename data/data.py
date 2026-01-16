from helpers.generate_a_user import UserData

class TestData:

    BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru/"


    # Existing test account
    EXISTING_EMAIL = 'sdf@sdf.com'
    EXISTING_PASSWORD = 'DRC5PzUBX!Xern!'

    VALID_USER = UserData.generate_valid_user()

    VALID_RECIPE = UserData.generate_valid_recipe()


        
