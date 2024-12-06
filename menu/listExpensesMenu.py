from storage.database import load_data
from tabulate import tabulate

def list_expenses_menu():
    print("=============================================")
    print("                Listar Gastos                ")
    print("=============================================")
    print("1. Ver todos los gastos")
    print("2. Filtrar por categoría")
    print("3. Filtrar por rango de fechas")
    print("4. Regresar al menú principal")

    option = input("Seleccione una opción: ")

    data = load_data()

    if option == '1':
        # Mostrar todos los gastos
        print(tabulate(data['gastos'], headers="keys", tablefmt="pretty"))
    elif option == '2':
        # Filtrar por categoría
        categoria = input("Ingrese la categoría para filtrar: ")
        filtered = [gasto for gasto in data['gastos'] if gasto['categoria'] == categoria]
        print(tabulate(filtered, headers="keys", tablefmt="pretty"))
    elif option == '3':
        # Filtrar por fechas (esto requiere implementar fechas dinámicas)
        print("Filtrar por fechas no está implementado aún.")
    
    input("Presiona Enter para continuar...")
