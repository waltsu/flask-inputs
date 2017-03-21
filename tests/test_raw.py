import unittest

from flask_inputs import Inputs
from wtforms.validators import DataRequired, Email


class RawInputs(Inputs):
    raw = {
        'name': [
            DataRequired('Name is required.')
        ],
        'email': [
            Email('Email must be valid.')
        ]
    }


class RawTest(unittest.TestCase):
    def test_valid(self):
        valid_input = {'name': 'Valtteri', 'email': 'valtteri@test.com'}
        inputs = RawInputs(valid_input)

        self.assertTrue(inputs.validate())

    def test_invalid(self):
        invalid_input = {'email': 'valtteri@test.com'}
        inputs = RawInputs(invalid_input)

        self.assertFalse(inputs.validate())
        self.assertIn('Name is required.', inputs.errors['name'])
