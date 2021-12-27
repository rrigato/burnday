from copy import deepcopy

import json
import unittest

class TestBurndaySkill(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("tests/events/burnday_skill_invoke.json", "r") as lambda_event:
            cls.lambda_event = json.load(lambda_event)

    def test_burnday_get(self):
        """TODO - implementation based on alexa skills kit"""
        from handlers.burnday_skill import lambda_handler


