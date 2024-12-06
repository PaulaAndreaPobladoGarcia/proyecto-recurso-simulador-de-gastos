import os
from menu.registerExpenseMenu import register_expense_menu

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
       

if __name__ == "__main__":
    main()
