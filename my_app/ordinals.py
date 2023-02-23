import regex

from .patterns import I18N_STARTING_ORDINAL_PATTERNS


def remove_ordinal_matches(text: str, lang: str = "default") -> str:
    """
    Remove ordinal matches from the given text.

    Args:
        text (str): The text to strip ordinal matches from.
        lang (str, optional): The language pattern to use. Defaults to "default".

    Returns:
        str: The text with ordinal matches removed, if any were found. Otherwise, the original text.

    Raises:
        KeyError: If the specified language pattern is not found in the 'I18N_STARTING_ORDINAL_PATTERNS' dictionary.
    """
    try:
        ordinal_pattern = I18N_STARTING_ORDINAL_PATTERNS[lang]
    except KeyError:
        raise KeyError(
            f"Language pattern '{lang}' not found in I18N_STARTING_ORDINAL_PATTERNS dictionary."
        )

    # remove ordinal matches using regular expression
    return regex.sub(ordinal_pattern, "", text)
