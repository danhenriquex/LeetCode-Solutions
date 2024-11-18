from typing import List


def possibilities(word: str) -> List[str]:
    # Dictionary with the signals of the Morse code
    morse_code = {
        ".": ["E"],
        "-": ["T"],
        "..": ["I"],
        ".-": ["A"],
        "-.": ["N"],
        "--": ["M"],
        "...": ["S"],
        "..-": ["U"],
        ".-.": ["R"],
        ".--": ["W"],
        "-..": ["D"],
        "-.-": ["K"],
        "--.": ["G"],
        "---": ["O"],
    }

    def expand_signals(signals: str) -> List[str]:
        """
        Recursively expands the signal string with '?' to generate all possible combinations.
        """
        if "?" not in signals:
            return [signals]  # Base case: no more placeholders
        # Replace the first '?' with '.' and '-', and recurse
        return expand_signals(signals.replace("?", ".", 1)) + expand_signals(
            signals.replace("?", "-", 1)
        )

    # Generate all possible combinations for the signals
    expanded_signals = expand_signals(word)

    # Collect possible characters for each valid Morse sequence
    possible_chars = []
    for signal in expanded_signals:
        if signal in morse_code:
            possible_chars.extend(morse_code[signal])

    return set(possible_chars)  # Sort and remove duplicates


# Test cases
print(possibilities("."))  # -> ["E"]
print(possibilities("-"))  # -> ["T"]
print(possibilities("-."))  # -> ["N"]
print(possibilities("..."))  # -> ["S"]
print(possibilities("..-"))  # -> ["U"]
print(possibilities("?"))  # -> ["E", "T"]
print(possibilities(".?"))  # -> ["I", "A"]
print(possibilities("?-?"))  # -> ["R", "W", "G", "O"]
