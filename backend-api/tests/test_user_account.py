from user.user_account import UserAccount
import unittest


class TestMailManager(unittest.TestCase):

    def test_create_account(self):
        user = UserAccount(
            name = "test name",
            email = "test@test.com",
            skin_list= [1,2,3]
        )
        self.assertEqual(user.name,"test name")
        self.assertEqual(user.email,"test@test.com")
        self.assertEqual(user.skin_list,[1,2,3])

    def test_user_invalid_email(self):
        with self.assertRaises(SyntaxError) as context:
            user = UserAccount(
                name="test",
                email = "test@test@test.com-",
                skin_list=[1,2,3]
            )

        self.assertTrue('Email not valid' in str(context.exception))
