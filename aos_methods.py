import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
import aos_locators as locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# s = Service(executable_path='C://Users//GAURAV//PycharmProjects//pythonProject//chromedriver.exe')
# driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch Advantage shopping Online Application\n')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.website_home_url)
    print(f'URL is:', driver.current_url)
    print(f'Title is:', driver.title)
    if driver.current_url == locators.website_home_url and driver.title == locators.website_title:
        print(f'Welcome to Online shopping page!! URL {locators.website_home_url} and Title is {locators.website_title}')
    else:
        print(f'Something went wrong!')
        tearDown()


def create_new_user_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(0.25)
    print('Click on Create New Account\n')
    for i in range(len(locators.list_values)):
        names, values = locators.list_names[i], locators.list_values[i]
        driver.find_element(By.NAME, names).send_keys(values)
        sleep(0.25)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    print(f'Register Button clicked\n')
    print(f'User created with Username: {locators.user_name}, Password: {locators.password}, Email: {locators.email}')
    sleep(0.25)
    # assert driver.find_element(By.XPATH, f'//*[contains(.,"{user_name}")]').is_displayed()


def logout():
    driver.find_element(By.LINK_TEXT, locators.user_name).click()
    sleep(0.25)
    print(f'User created is displayed on the top right \n')
    # driver.find_element(By.ID, 'menuUserSVGPath').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"Sign out")]').click()
    print(f'***Congratulations!! \033[1m {locators.user_name} \033[0m has been logout***\n')
    sleep(0.25)


def login():
    assert driver.current_url == locators.website_home_url and driver.title == locators.website_title
    sleep(2)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.25)
    driver.find_element(By.NAME, 'username').send_keys(locators.user_name)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)
    assert driver.find_element(By.LINK_TEXT, locators.user_name).is_displayed()
    print(f'\033[1m User is login!!\033[0m Username: {locators.user_name} and Email: {locators.email}\n')
    sleep(0.25)


def homepagetext():
    # driver.find_element(By.ID, 'speakersTxt').is_displayed()
    assert driver.title == locators.website_title
    driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
    for i in range(len(locators.list_homepagetext)):
        element = locators.list_homepagetext_element[i]
        driver.find_element(By.ID, element).is_displayed()
    print(f'*****All texts {locators.list_homepagetext} is displayed*****')
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
    sleep(0.25)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('HP Chromebook 14 G1('
                                                                                           'ENERGY STAR)')
    sleep(0.25)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').clear()
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject)
    sleep(2)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(0.25)
    # assert driver.find_element(By.ID, 'registerSuccessCover').is_displayed()
    assert driver.find_element(By.XPATH, '//*[contains(.,"Thank you for contacting Advantage support.")]').is_displayed()
    assert driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').is_displayed()
    print(f'-----THANK YOU FOR CONTACTING US-----')
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[contains(.,"FOLLOW US")]').is_displayed()
    sleep(0.25)
    assert driver.find_element(By.NAME, 'follow_facebook').is_enabled()
    sleep(0.25)
    assert driver.find_element(By.NAME, 'follow_twitter').is_enabled()
    sleep(0.25)
    assert driver.find_element(By.NAME, 'follow_linkedin').is_enabled()
    sleep(0.25)
    print(f' **** ALL Logos are enabled ****\n')


def delete():
    driver.find_element(By.LINK_TEXT, locators.user_name).click()
    sleep(1)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My orders")]').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//div/label[contains(.,"No orders")]').is_displayed()
    sleep(0.25)
    print(f' No Orders is displayed \n')
    driver.find_element(By.LINK_TEXT, locators.user_name).click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a/div/label[contains(.,"My account")]').click()
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.user_name}")]').is_displayed()
    print(f'Full Username is displayed in Account Details \n')
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div[@class="deletePopupBtn deleteRed"]').click()
    print(f'\033[31;1m****Account has been deleted.****\033[31;0m \n')
    sleep(3)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.NAME, 'username').send_keys(locators.user_name)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)
    driver.find_element(By.ID, 'signInResultMessage').is_displayed()
    print(f'\033[31;1m****Incorrect user name or password.****\033[31;0m')


def tearDown():
    if driver is not None:
        print('-----**********---------------------')
        print('Test Completed at:', datetime.datetime.now())
        sleep(2)
        driver.close()
        driver.quit()


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('data.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.user_name}\t'
          f'{locators.password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


# setUp()
# create_new_user_account()
# logout()
# logger('created')
# # ------New User login--------------
# login()
# logout()
# -----------------------------------------
# tearDown()
