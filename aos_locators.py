from faker import Faker

fake = Faker(locale='en_CA')

# ************************ VariableS***************************************

website_home_url = 'https://advantageonlineshopping.com/#/'
# website _title = ' Advantage Shopping'
website_title = '\xa0Advantage Shopping'

# ***********Fake data*****************************
first_name = fake.first_name()[:8]
last_name = fake.last_name()[:5]
phone_number = fake.phone_number()
user_name = f'{first_name}{last_name}'
email = f'{user_name}@{fake.free_email_domain()}'
password = fake.password(length=10)
confirm_password = password
address = fake.address().replace("\n", " ")[:10]
country = fake.current_country()[:5]
city = fake.city()[:5]
province = fake.province()[:5]
postal_code = fake.postcode()
subject = f'I want to know more details about Laptop. Please email me on {email}'

list_labels = ['Username', 'Email' 'Password' 'Confirm Password',
               'First Name', 'Last Name', 'Phone Number',
               'Country', 'City', 'Address', 'Province', 'PostalCode']

list_names = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage',
              'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage',
              'countryListboxRegisterPage', 'cityRegisterPage', 'addressRegisterPage',
              'state_/_province_/_regionRegisterPage', 'postal_codeRegisterPage']

list_values = [user_name, email, password, confirm_password,
               first_name, last_name, phone_number,
               country, city, address, province, postal_code]

list_homepagetext = ['SPEAKERS', 'TABLETS', 'LAPTOPS', 'MICE', 'HEADPHONES']

list_homepagetext_element = ['speakersTxt', 'tabletsTxt', 'laptopsTxt', 'miceTxt', 'headphonesTxt']

# ***************************************************************************
