import os
from menu.registerExpenseMenu import register_expense_menu
from menu.listExpensesMenu import list_expenses_menu
from menu.calculateTotalMenu import calculate_total_menu
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menú Principal del Simulador de Gasto Diario")
        print("=" * 45)
        print("1. Registrar nuevo gasto")
        print("2. Listar gastos")
        print("3. Calcular total de gastos")
        print("4. Generar reporte de gastos")
        print("5. Salir")
        print("=" * 45)
        
        option = input("Seleccione una opción: ")

        if option == '1':
            register_expense_menu()
        elif option == '2':
            list_expenses_menu()
        elif option == '3':
            calculate_total_menu()
        elif option == '4':
             print("¿Desea salir del programa? (S/N): ", end="")
             if input().lower() == 's':
                break

if __name__ == "__main__":
    main()
