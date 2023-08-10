from io import StringIO
from unittest import TestCase, mock
from unittest.mock import patch
import unittest
from shop import Shop, User, FundsError

#Requirements: 5 tests, if needed each test has multiple scenarios
#I have researched unittest methods in order to do this

class ShopTest(unittest.TestCase):
    def setUp(self):
        #The shop needs to be set up first before any testing can begin
        self.comp_shop = Shop("Tech Store")
        self.comp_shop.items = {
            "xbox": {"price": 400, "stock": 1},
            "controller": {"price": 25, "stock": 5},
            "disk drive": {"price": 16.99, "stock": 2},
            "mouse": {"price": 15.50, "stock": 3},
        }
        self.new_user = User("John", 100, self.comp_shop)
        self.comp_shop.add_user(self.new_user)

    def test_greet_user(self):
        #Test for valid greet response

        expected_output = "Welcome John! This is the Tech Store\nThe products available today are:\n- xbox : £ 400 ( Stock: 1 )\n- controller : £ 25 ( Stock: 5 )\n- disk drive : £ 16.99 ( Stock: 2 )\n- mouse : £ 15.5 ( Stock: 3 )\n"

        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.comp_shop.greet_user()
            self.assertEqual(captured_output.getvalue(), expected_output)

    def test_exit_option(self):
        expected_output_one = "You have entered the Computer Store."
        expected_output_two = "Exiting the shop..."
        
        # Test case for response "n"
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.comp_shop.exit_option("n")
            self.assertEqual(captured_output.getvalue().strip(), expected_output_one)
        
        # Test case for response "y"
        with self.assertRaises(SystemExit) as context_manager:
            with patch("sys.stdout", new=StringIO()) as captured_output:
                self.comp_shop.exit_option("y")
                self.assertEqual(captured_output.getvalue().strip(), expected_output_two)
        self.assertEqual(context_manager.exception.code, None)

        # Test case for other e.g. "x"
        with self.assertRaises(ValueError) as error_context:
            with patch("sys.stdout", new=StringIO()) as captured_output:
                self.comp_shop.exit_option("x")
            self.assertEqual(str(error_context.exception), "Value must be 'y' or 'n'")

    def test_add_money(self):
        expected_output_one = "Your balance is now £ 150.0"
        expected_output_two = "Invalid input. Must be in numerical format with no special characters"

        #Test case for valid input

        with patch("sys.stdout", new = StringIO()) as captured_output:
            self.new_user.add_money("50")
            self.assertEqual(captured_output.getvalue().strip(), expected_output_one)

        #Test case for invalid input

        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.new_user.add_money("x")
            self.assertEqual(captured_output.getvalue().strip(), expected_output_two)

    def test_get_balance(self):
        expected_output = f"Your balance is £ 100"
        with patch("sys.stdout", new = StringIO()) as captured_output:
            self.new_user.get_balance()
            self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_view_basket(self):
        expected_output = "Your basket is empty"
        with patch("sys.stdout", new = StringIO()) as captured_output:
            self.new_user.view_basket()
            self.assertEqual(captured_output.getvalue().strip(), expected_output)

    #To test the custom error: though I have seen this work in terminal
    def test_add_item(self):
        self.new_user.add_item("xbox")
        self.new_user.add_item("xbox")
        with self.assertRaises(FundsError) as error_context:
            self.new_user.add_item("xbox")
        self.assertEqual(str(error_context.exception), "3 attempts of purchases with insufficient funds.")





#6 tests will run, all will pass

if __name__ == "__main__":
    unittest.main()
