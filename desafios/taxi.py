def comparar_empresas(tf1, vqr1, tf2, vqr2):
    # Convertendo as entradas para números
    tf1 = float(tf1)
    tf2 = float(tf2)
    vqr1 = float(vqr1)
    vqr2 = float(vqr2)

    # Caso em que as duas empresas têm o mesmo custo (tanto faz)
    if tf1 == tf2 and vqr1 == vqr2:
        return "tanto faz"

    # Caso em que a empresa 1 sempre é mais barata
    if tf1 < tf2 and vqr1 <= vqr2:
        return "empresa 1"

    # Caso em que a empresa 2 sempre é mais barata
    if tf2 < tf1 and vqr2 <= vqr1:
        return "empresa 2"

    # Verificar o ponto de cruzamento analiticamente
    if tf2 > tf1 and vqr1 > vqr2:
        ponto_de_cruzamento = (tf2 - tf1) / (vqr1 - vqr2)
        if ponto_de_cruzamento > 0:
            return f"empresa 1 quando distância < {ponto_de_cruzamento:.1f}, tanto faz quando distância = {ponto_de_cruzamento:.1f}, empresa 2 quando distância > {ponto_de_cruzamento:.1f}"

    # Se não houver ponto de cruzamento, verificamos quem é mais barato em qualquer situação
    if vqr1 < vqr2 and tf1 < tf2:
        return "empresa 1"
    elif vqr2 < vqr1 and tf2 < tf1:
        return "empresa 2"

    # Caso de empate geral
    return "tanto faz"


# caso em que tanto faz
print(comparar_empresas(2.5, 1.0, 5.0, 0.75))
# caso em que a empresa 1 é melhor
print(comparar_empresas(2.5, 1.0, 5.0, 0.5))
# caso em que a empresa 2 é melhor
print(comparar_empresas(5.0, 1.0, 2.5, 1.0))
