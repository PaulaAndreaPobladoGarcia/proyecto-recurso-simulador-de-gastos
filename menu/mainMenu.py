import keyboard
def desing():
    while True:
        try:

         print(f"""     
        =============================================
                 Simulador de Gasto Diario
        =============================================
        Seleccione una opción:

        1. Registrar nuevo gasto
        2. Listar gastos
        3. Calcular total de gastos
        4. Generar reporte de gastos
        5. Salir
        =============================================
        """)
         options = int(input("\tPor favor, elige una opción (1-5): "))
         if (options >=1 and option <=5):
            return options
         else: 
            raise ValueError
        except ValueError as e:
           print ("\tUsuario eliga una oocion valida")
        