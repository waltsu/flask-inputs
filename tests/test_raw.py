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
        test_input = {'name': 'Valtteri', 'email': 'valtteri@test.com'}
        inputs = RawInputs(test_input)

        self.assertTrue(inputs.validate())
