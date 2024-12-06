from logic.expenseLogic import generate_report

def generate_report_menu():
    print("=============================================")
    print("         Generar Reporte de Gastos           ")
    print("=============================================")
    print("1. Reporte diario")
    print("2. Reporte semanal")
    print("3. Reporte mensual")
    print("4. Regresar al menú principal")

    option = input("Seleccione una opción: ")

    if option in ['1', '2', '3']:
        report = generate_report(option)
        print("Reporte generado:")
        print(report)
    elif option == '4':
        return
    
    input("Presiona Enter para continuar...")
