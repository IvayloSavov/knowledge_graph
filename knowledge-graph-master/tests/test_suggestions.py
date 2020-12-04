import unittest
from suggestions import Suggestions


class SuggestionTest(unittest.TestCase):
    def test_parse_of_content(self):
        content = b'<?xml version="1.0"?><toplevel><CompleteSuggestion><suggestion data="hristiyan vs m\xfcsl\xfcman"/></CompleteSuggestion><CompleteSuggestion><suggestion data="islamiyet ve hristiyanl&#x131;k"/></CompleteSuggestion><CompleteSuggestion><suggestion data="yahudi vs hristiyan"/></CompleteSuggestion><CompleteSuggestion><suggestion data="m\xfcsl\xfcman vs hristiyan futbolcular"/></CompleteSuggestion></toplevel>'
        Suggestions.get_element_tree(content)


if __name__ == '__main__':
    unittest.main()
