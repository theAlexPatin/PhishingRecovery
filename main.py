from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from faker import Faker
fake = Faker()

URL = 'https://www.rafola.appdealer.top/'
EMAIL_INPUT = 'mail'
PASSWORD_INPUT = 'password'

def get_fake_email():
	return fake.simple_profile()['mail']


def _get_fake_phrase():
	phrase = fake.words(3, None, True)
	if not random.randint(0,3):
		for i in range(len(phrase)):
			phrase[i] = phrase[i].capitalize()
	phrase = ''.join(str(e) for e in phrase)
	if random.randint(0,1):
		phrase = phrase + str(random.randint(0,100))
	if random.randint(0,1):
		phrase = phrase + '!'
	return phrase

def _get_fake_alphanum():
	length = random.randint(8,16)
	digits = random.randint(0,1)
	upper_case = random.randint(0,1)
	lower_case = random.randint(0,1)
	special_chars = random.randint(0,1)
	return fake.password(length, special_chars, digits, upper_case, lower_case)

def get_fake_password():
	if random.randint(0,5):
		return _get_fake_phrase()
	else:
		return _get_fake_alphanum()

def navigate():
	driver = webdriver.Chrome()
	driver.get(URL)
	username = driver.find_element_by_name(EMAIL_INPUT)
	username.send_keys(get_fake_email())
	password = driver.find_element_by_name(PASSWORD_INPUT)
	password.send_keys(get_fake_password())
	password.send_keys(Keys.RETURN)


def main():
	while(True):
		navigate()

if __name__ == '__main__':
	main()