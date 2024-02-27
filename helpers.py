import random
def generate_email():
    email = "margatitalugovaya5" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + "@yandex.ru"
    return email