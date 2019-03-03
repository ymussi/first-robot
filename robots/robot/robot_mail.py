from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from configparser import ConfigParser

config = ConfigParser()
config.read('../config.ini')

url = config['SITES']['URL']
email = config['MAIL']['EMAIL']
senha = config['MAIL']['SENHA']
to = config['MAIL']['TO']
subject = config['MAIL']['SUBJECT']
contents = config['MAIL']['CONTENTS']

def login_gmail():
    driver = webdriver.Safari()
    
    driver.get(url)
    driver.maximize_window()

    mail = driver.find_element_by_id("identifierId")
    mail.send_keys(email)

    btn_email = driver.find_element_by_id("identifierNext")
    btn_email.click()

    sleep(1)
    sen = driver.find_element_by_class_name('whsOnd')
    sen.send_keys(senha)

    sleep(2)
    btn_passwd = driver.find_element_by_class_name("RveJvd")
    btn_passwd.click()

    sleep(8)
    novo_email = driver.find_element_by_class_name('z0')
    novo_email.click()

    sleep(2)
    to_email = driver.find_element_by_id(':168')
    to_email.send_keys(to)

    sleep(2)
    subject_mail = driver.find_element_by_id(':15q')
    subject_mail.send_keys(subject)

    sleep(2)
    contents_mail = driver.find_element_by_id(':16v')
    contents_mail.send_keys(contents)

    sleep(2)
    send_email = driver.find_element_by_id(':15g')
    send_email.click()

    sleep(5)
    driver.close()

if __name__ == "__main__":
    login_gmail()
    pass