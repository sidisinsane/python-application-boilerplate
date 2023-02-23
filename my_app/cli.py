import argparse

from .ordinals import remove_ordinal_matches


def cli():
    """Command line interface for removing ordinal numbers from text."""

    parser = argparse.ArgumentParser(description="Remove ordinal numbers from text.")
    parser.add_argument(
        "-t",
        "--text",
        type=str,
        required=True,
        help="The text to remove ordinal numbers from.",
    )
    parser.add_argument(
        "-l",
        "--lang",
        type=str,
        default="default",
        help="The language code to use for identifying ordinal numbers. Defaults to 'default'.",
    )
    args = parser.parse_args()

    """
    Returns the input text with any ordinal numbers removed.

    Args:
        text (str): The text to remove ordinal numbers from.
        lang (str): The language code to use for identifying ordinal numbers.

    Returns:
        str: The input text with ordinal numbers removed.
    """
    return remove_ordinal_matches(args.text, args.lang)
