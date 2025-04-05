while True:
    print("\n--- Calculadora Sencilla ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")
    match opcion:
        case "4":
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
                continue
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
            

    if opcion == "5":
        print("¡Hasta luego!")
        break

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingresa números.")
        continue

