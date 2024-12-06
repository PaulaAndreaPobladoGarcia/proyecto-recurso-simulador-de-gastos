from logic.expenseLogic import calculate_total

def calculate_total_menu():
    print("=============================================")
    print("         Calcular Total de Gastos            ")
    print("=============================================")
    print("1. Calcular total diario")
    print("2. Calcular total semanal")
    print("3. Calcular total mensual")
    print("4. Regresar al menú principal")

    option = input("Seleccione una opción: ")

    if option == '1':
        total = calculate_total("diario")
        print(f"El total diario es: {total}")
    elif option == '2':
        total = calculate_total("semanal")
        print(f"El total semanal es: {total}")
    elif option == '3':
        total = calculate_total("mensual")
        print(f"El total mensual es: {total}")
    
    input("Presiona Enter para continuar...")
