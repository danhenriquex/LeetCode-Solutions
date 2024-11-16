def seven_segmentify(time_: str) -> str:
    """
    Given a time in the format HH:MM, return the time in the format HH:MM using seven-segment display.
    For values up to 9, the hour will not have a leading zero.
    """
    DIGIT_MAP = {
        "0": [" _ ", "| |", "|_|"],
        "1": ["   ", "  |", "  |"],
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

    # Criar uma lista para armazenar as três linhas do display
    rows = ["", "", ""]

    # Para cada caractere no tempo, adicioná-lo às linhas correspondentes
    for char in time_:
        for i in range(3):
            rows[i] += (
                DIGIT_MAP[char][i] + " "
            )  # Adiciona um único espaço entre os caracteres

    # Remover o espaço extra no final de cada linha
    rows = [row.rstrip() for row in rows]

    # Combinar as linhas em uma única string
    final_string = "\n".join(rows)
    return final_string


# Testes
print(seven_segmentify("08:45"))
print(seven_segmentify("9:03"))
print(seven_segmentify("12:37"))
