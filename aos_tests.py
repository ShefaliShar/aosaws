import unittest
import aos_methods as methods
import aos_locators as locators


class AOSAppPositiveTestCases (unittest.TestCase):

    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.create_new_user_account()
        methods.logout()
        methods.logger('created')
        methods.login()
        methods.homepagetext()
        methods.logout()
        methods.login()
        methods.delete()
        methods.logger('deleted')
        methods.tearDown()
