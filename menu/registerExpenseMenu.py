from storage.database import load_data, save_data
from tabulate import tabulate
def register_expense_menu():
    print("=============================================")
    print("            Registrar Nuevo Gasto            ")
    print("=============================================")
    
    monto = float(input("Ingrese el monto del gasto: "))
    categoria = input("Ingrese la categoría (comida, transporte, etc.): ")
    descripcion = input("Ingrese la descripción (opcional): ")

    
    data = load_data()

    
    data['gastos'].append({
        "monto": monto,
        "categoria": categoria,
        "descripcion": descripcion,
        "fecha": "2024-12-06"  
    })

    
    save_data(data)

    print("¡Gasto registrado con éxito!")
    input("Presiona Enter para continuar...")
