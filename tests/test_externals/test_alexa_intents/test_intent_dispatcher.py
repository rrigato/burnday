from copy import deepcopy

import unittest

class TestIntentDispatcher(unittest.TestCase):


    def test_get_alexa_lambda_handler(self):
        """get_alexa_lambda_handler returns a lambda handler function"""
        from externals.alexa_intents.intent_dispatcher import get_alexa_lambda_handler
        from inspect import isfunction


        alexa_lambda_handler = get_alexa_lambda_handler()


        self.assertTrue(isfunction(alexa_lambda_handler))

