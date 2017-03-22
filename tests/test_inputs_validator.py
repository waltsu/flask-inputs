import unittest

from flask_inputs import Inputs
from wtforms.validators import DataRequired

from flask_inputs.validators import InputsValidator


class NameInputs(Inputs):
    raw = {
        'first_name': [
            DataRequired('First name is required.')
        ],
        'last_name': [
            DataRequired('Last name is required.')
        ]
    }


class UserInputs(Inputs):
    raw = {
        'name': [
            InputsValidator(validator_class=NameInputs)
        ],
        'address': [
            DataRequired('Address is required.')
        ]
    }


class InputsValidatorTest(unittest.TestCase):
    def test_valid(self):
        valid_input = {'name': {'first_name': 'Valtteri', 'last_name': 'Virtanen'}, 'address': 'My street 2'}
        inputs = UserInputs(valid_input)

        self.assertTrue(inputs.validate())

    def test_invalid_child(self):
        invalid_input = {'name': {'last_name': 'Virtanen'}, 'address': 'My street 2'}
        inputs = UserInputs(invalid_input)

        self.assertFalse(inputs.validate())
        self.assertIn('First name is required.', inputs.errors['name'][0]['first_name'])

    def test_invalid_parent(self):
        invalid_input = {'name': {'first_name': 'Valtteri', 'last_name': 'Virtanen'}}
        inputs = UserInputs(invalid_input)

        self.assertFalse(inputs.validate())
        self.assertIn('Address is required.', inputs.errors['address'])

    def test_both_invalid(self):
        invalid_input = {}
        inputs = UserInputs(invalid_input)

        self.assertFalse(inputs.validate())
        self.assertIn('Address is required.', inputs.errors['address'])
        self.assertIn('First name is required.', inputs.errors['name'][0]['first_name'])
        self.assertIn('Last name is required.', inputs.errors['name'][0]['last_name'])
