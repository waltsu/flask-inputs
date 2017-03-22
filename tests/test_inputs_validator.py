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
