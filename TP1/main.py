cadena_binaria_rx = "1111010100000001"
resultado = 0

# Recorremos de 4 en 4
for i in range(0, len(cadena_binaria_rx), 4):
    nibble = cadena_binaria_rx[i:i+4]      # Tomamos el nibble
    valor = int(nibble,base=2)              # Convertimos de base 2 a entero
    resultado ^= valor                  # Aplicamos XOR acumulativo

# Si querés el resultado final de nuevo en binario (rellenando con ceros a la izquierda)
print(f"Resultado final (entero): {resultado}")
print(f"Resultado final (binario): {bin(resultado)[2:].zfill(4)}")
