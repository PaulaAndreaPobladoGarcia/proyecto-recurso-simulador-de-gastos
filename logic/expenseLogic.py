from storage.database import load_data

def calculate_total(period):
    data = load_data()

    total = 0
    for gasto in data['gastos']:
        total += gasto['monto']

    return total

def generate_report(period):
    data = load_data()
    
   
    if period == '1':  # Diario
        return "Reporte Diario: " + str(data['gastos'])  
    elif period == '2':  # Semanal
        return "Reporte Semanal"
    elif period == '3':  # Mensual
        return "Reporte Mensual"
