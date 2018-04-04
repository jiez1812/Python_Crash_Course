import unittest
from survey import AnonymousSurvey

class TestAnomyousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is store properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses('English')

        self.assertIn('English', my_survey.store_responses)

unittest.main()