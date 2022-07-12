import unittest
from app.customer.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self) -> None:
        self.customer = Customer('Juan','j@j.com','my address')        

    def test_update_mail(self):
        newEmail='new@j.com'
        self.customer.update_email(newEmail)
        self.assertEqual(self.customer.email,newEmail)

        newEmail='new@j'
        self.customer.update_email(newEmail)
        self.assertEqual(self.customer.email,newEmail)

        self.customer.update_email(None)
        self.assertEqual(self.customer.email,newEmail)

        self.customer.update_email('no valid email')
        self.assertEqual(self.customer.email,newEmail)


    def test_get_all_data_to_review(self):
        # print(customer.toJSON())
        dict=self.customer.get_all_data_to_review()
        # print(dict)
        self.assertEqual(dict['name'],self.customer.name)
