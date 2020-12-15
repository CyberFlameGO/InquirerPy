import os
import unittest
from unittest.mock import patch

from InquirerPy.exceptions import InvalidArgument
from InquirerPy.utils import calculate_height, get_style


class TestUtils(unittest.TestCase):
    @patch("InquirerPy.utils.shutil.get_terminal_size")
    def test_prompt_height(self, mocked_terminal_size):
        mocked_terminal_size.return_value = (24, 80)
        height, max_height = calculate_height(None, None)
        self.assertEqual(height, None)
        self.assertEqual(max_height, 79)

        height, max_height = calculate_height("50%", None)
        self.assertEqual(height, 39)
        self.assertEqual(max_height, 79)

        calculate_height("50%", "80")

        self.assertRaises(InvalidArgument, calculate_height, "50%", "40%")
        self.assertRaises(InvalidArgument, calculate_height, "50", "40%")
        self.assertRaises(InvalidArgument, calculate_height, "adsfa", "40%")
        self.assertRaises(InvalidArgument, calculate_height, "50%", "asfasdds")

        height, max_height = calculate_height(None, "80%")
        self.assertEqual(height, None)
        self.assertEqual(max_height, 63)

    def test_style(self):
        style = get_style()
        self.assertEqual(
            style,
            {
                "questionmark": "#e5c07b",
                "answer": "#61afef",
                "input": "#98c379",
                "question": "",
                "instruction": "",
                "pointer": "#61afef",
                "checkbox": "#98c379",
                "separator": "",
                "skipped": "#5c6370",
                "fuzzy_prompt": "#c678dd",
                "fuzzy_info": "#98c379",
                "fuzzy_marker": "#e5c07b",
                "fuzzy_border": "#4b5263",
                "fuzzy_match": "#c678dd",
            },
        )

        os.environ["INQUIRERPY_STYLE_QUESTIONMARK"] = "#000000"
        os.environ["INQUIRERPY_STYLE_ANSWER"] = "#111111"
        os.environ["INQUIRERPY_STYLE_QUESTION"] = "#222222"
        os.environ["INQUIRERPY_STYLE_INSTRUCTION"] = "#333333"
        os.environ["INQUIRERPY_STYLE_INPUT"] = "#444444"
        os.environ["INQUIRERPY_STYLE_POINTER"] = "#555555"
        os.environ["INQUIRERPY_STYLE_CHECKBOX"] = "#66666"
        os.environ["INQUIRERPY_STYLE_SEPARATOR"] = "#777777"
        os.environ["INQUIRERPY_STYLE_SKIPPED"] = "#888888"
        os.environ["INQUIRERPY_STYLE_FUZZY_PROMPT"] = "#999999"
        os.environ["INQUIRERPY_STYLE_FUZZY_INFO"] = "#aaaaaa"
        os.environ["INQUIRERPY_STYLE_FUZZY_MARKER"] = "#bbbbbb"
        os.environ["INQUIRERPY_STYLE_FUZZY_BORDER"] = "#cccccc"
        os.environ["INQUIRERPY_STYLE_FUZZY_MATCH"] = "#dddddd"
        style = get_style()
        self.assertEqual(
            style,
            {
                "questionmark": "#000000",
                "answer": "#111111",
                "input": "#444444",
                "question": "#222222",
                "instruction": "#333333",
                "pointer": "#555555",
                "checkbox": "#66666",
                "separator": "#777777",
                "skipped": "#888888",
                "fuzzy_prompt": "#999999",
                "fuzzy_info": "#aaaaaa",
                "fuzzy_marker": "#bbbbbb",
                "fuzzy_match": "#dddddd",
                "fuzzy_border": "#cccccc",
            },
        )