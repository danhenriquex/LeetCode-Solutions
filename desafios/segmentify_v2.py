def seven_segmentify(time_: str) -> str:
    """
    Convert a time string in the format HH:MM into a seven-segment display format.
    """
    DIGIT_MAP = {
        "0": [" _ ", "| |", "|_|"],
        "1": ["   ", "  |", "  |"],  # Ajuste no mapeamento do "1"
        "2": [" _ ", " _|", "|_ "],
        "3": [" _ ", " _|", " _|"],
        "4": ["   ", "|_|", "  |"],
        "5": [" _ ", "|_ ", " _|"],
        "6": [" _ ", "|_ ", "|_|"],
        "7": [" _ ", "  |", "  |"],
        "8": [" _ ", "|_|", "|_|"],
        "9": [" _ ", "|_|", " _|"],
        ":": ["   ", " . ", " . "],
    }

    # Remover zero à esquerda na hora, se existir
    hours, minutes = time_.split(":")
    if hours.startswith("0"):
        hours = hours[1:]  # Remove o zero à esquerda

    # Recompõe o tempo sem o zero à esquerda (se necessário)
    time_ = f"{hours}:{minutes}"

    # Initialize rows for the seven-segment display
    rows = [""] * 3  # Three rows to build the ASCII display

    for char in time_:
        for i in range(3):
            # Append the respective row of the character and a space for separation
            rows[i] += DIGIT_MAP[char][i]

    # Adiciona espaços à esquerda para alinhamento adequado
    # O número 4 serve para ajustar o alinhamento do relógio
    formatted_rows = [row.rjust(1) for row in rows]

    # Return the joined rows with newline separation
    return "\n".join(formatted_rows)


# Testes
print(seven_segmentify("08:45"))
print(seven_segmentify("13:24"))
print(seven_segmentify("00:00"))
print(seven_segmentify("21:49"))


import unittest


class Testseven_segmentify(unittest.TestCase):
    def test_13_24(self):
        "should work on 13:24"
        self.assertEqual(
            seven_segmentify("13:24"), "    _     _  \n  | _| .  _||_|\n  | _| . |_   |"
        )

    # def test_08_56(self):
    #     "should work on 08:56"
    #     self.assertEqual(
    #         seven_segmentify("08:56"),
    #         "    _     _  _ \n   |_| . |_ |_ \n   |_| .  _||_|",
    #     )


# Execute the tests
unittest.main(argv=[""], verbosity=2, exit=False)
