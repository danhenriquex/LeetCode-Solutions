def seven_segmentify(time_: str) -> str:

    number_dict = {
        "0": "abcedf",
        "1": "bc",
        "2": "abged",
        "3": "abgcd",
        "4": "fgbc",
        "5": "afgcd",
        "6": "afgcde",
        "7": "abc",
        "8": "abcdefg",
        "9": "abcfgd",
        ":": "dot",
    }

    hours, minutes = time_.split(":")
    if hours.startswith("0"):
        hours = hours[1:]

    time_ = f"{hours}:{minutes}"

    def get_line(segments, pos):
        if pos == 0:
            return (
                " _ " if "a" in segments else "  "
            )  # Corrigido para ter espaçamento adequado antes do "_"
        if pos == 1:
            left = " " if "f" not in segments else "|"
            right = " " if "b" not in segments else "|"
            return f"{left} {right}" if "d" not in segments else f"{left}_{right}"
        if pos == 2:
            left = " " if "e" not in segments else "|"
            right = " " if "c" not in segments else "|"
            return f"{left} {right}" if "d" not in segments else f"{left}_{right}"

    def get_colon_line(pos):
        if pos == 1 or pos == 2:
            return " . "  # Corrigido o espaçamento do ponto
        return "   "

    lines = [""] * 3
    for char in time_:
        if char == ":":
            for i in range(3):
                lines[i] += get_colon_line(i)
        else:
            segments = number_dict[char]
            for i in range(3):
                lines[i] += get_line(segments, i)

    return "\n".join(line.rstrip() for line in lines)


# Testando
print(seven_segmentify("00:00"))
