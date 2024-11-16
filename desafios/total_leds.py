def calcula_total_leds(altura: int, largura: int) -> int:
    total_leds = (largura + 1) * (altura + 1)

    print("Resultado: ", total_leds)

    return total_leds


if __name__ == "__main__":
    calcula_total_leds(4, 2)
    calcula_total_leds(2, 3)
    calcula_total_leds(2, 4)
