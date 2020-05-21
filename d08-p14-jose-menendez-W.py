def menuOpc(colorLib, system,selected = 1):
    if(selected == 1):
        print(colorLib.Cursor.POS(50, 12)+colorLib.Fore.GREEN+colorLib.Back.WHITE+"      [1] Registro      ")
    else:
        print(colorLib.Cursor.POS(50, 12)+colorLib.Fore.YELLOW+"      [1] Registro      ")
    if(selected == 2):
        print(colorLib.Cursor.POS(50, 14)+colorLib.Fore.GREEN+colorLib.Back.WHITE+"      [2] Bajas         ")
    else:
        print(colorLib.Cursor.POS(50, 14)+colorLib.Fore.YELLOW+"      [2] Bajas          ")
    if(selected == 3):
        print(colorLib.Cursor.POS(50, 16)+colorLib.Fore.GREEN+colorLib.Back.WHITE+"      [3] Ventas        ")
    else:
        print(colorLib.Cursor.POS(50, 16)+colorLib.Fore.YELLOW+"      [3] Ventas        ")
    if(selected == 4):
        print(colorLib.Cursor.POS(50, 18)+colorLib.Fore.GREEN+colorLib.Back.WHITE+"      [4] Salir         ")
    else:
        print(colorLib.Cursor.POS(50, 18)+colorLib.Fore.YELLOW+"      [4] Salir         ")
    print(colorLib.Cursor.POS(28,28))
    
def registrationOpc(colorLib, system,selected = 1):
    if(selected == 1):
        print(colorLib.Cursor.POS(50, 14)+colorLib.Fore.CYAN+colorLib.Back.WHITE+"      [1] Fruteria        ")
    else:
        print(colorLib.Cursor.POS(50, 14)+colorLib.Fore.RED+"      [1] Fruteria        ")
    if(selected == 2):
        print(colorLib.Cursor.POS(50, 16)+colorLib.Fore.CYAN+colorLib.Back.WHITE+"      [2] Empleado        ")
    else:
        print(colorLib.Cursor.POS(50, 16)+colorLib.Fore.RED+"      [2] Empleado          ")
    if(selected == 3):
        print(colorLib.Cursor.POS(50, 18)+colorLib.Fore.CYAN+colorLib.Back.WHITE+"      [3] Producto        ")
    else:
        print(colorLib.Cursor.POS(50, 18)+colorLib.Fore.RED+"      [3] Producto        ")
    if(selected == 4):
        print(colorLib.Cursor.POS(50, 20)+colorLib.Fore.CYAN+colorLib.Back.WHITE+"      [ESC] Ir al menu    ")
    else:
        print(colorLib.Cursor.POS(50, 20)+colorLib.Fore.RED+"      [ESC] Ir al Menu       ")
    print(colorLib.Cursor.POS(28,28))

def menuInfo(colorLib):
    print(colorLib.Cursor.POS(50,3)+colorLib.Fore.YELLOW+"___  ___                 ")
    print(colorLib.Cursor.POS(50,4)+colorLib.Fore.YELLOW+"|  \/  |                 ")
    print(colorLib.Cursor.POS(50,5)+colorLib.Fore.YELLOW+"| .  . | ___ _ __  _   _ ")
    print(colorLib.Cursor.POS(50,6)+colorLib.Fore.YELLOW+"| |\/| |/ _ \ '_ \| | | |")
    print(colorLib.Cursor.POS(50,7)+colorLib.Fore.YELLOW+"| |  | |  __/ | | | |_| |")
    print(colorLib.Cursor.POS(50,8)+colorLib.Fore.YELLOW+"\_|  |_/\___|_| |_|\__,_|")
    
    print(colorLib.Cursor.POS(85,13)+colorLib.Fore.GREEN+"[FLECHA-ARRIBA] Mover Arriba")
    print(colorLib.Cursor.POS(85,14)+colorLib.Fore.GREEN+"[FLECHA-ABAJO] Mover Abajo")
    print(colorLib.Cursor.POS(85,15)+colorLib.Fore.GREEN+"[ENTER] Seleccionar")
    print(colorLib.Cursor.POS(37,23)+colorLib.Fore.GREEN+"[Puede seleccionar pulsando el numero de la opcion]")
    
    print(colorLib.Cursor.POS(8,12)+colorLib.Fore.GREEN+"x---------------------------x")
    print(colorLib.Cursor.POS(16,13)+colorLib.Fore.GREEN+"practica 14")
    print(colorLib.Cursor.POS(10,14)+colorLib.Fore.GREEN+"menendez gomez jose dario")
    print(colorLib.Cursor.POS(9,15)+colorLib.Fore.GREEN+"chavez romo jonathan eduardo")
    print(colorLib.Cursor.POS(7,16)+colorLib.Fore.GREEN+"espinoza torres daniel alejandro")
    print(colorLib.Cursor.POS(10,17)+colorLib.Fore.GREEN+"herrera vazquez oscar ivan")
    print(colorLib.Cursor.POS(16,18)+colorLib.Fore.GREEN+"Seccion: D08")
    print(colorLib.Cursor.POS(7,19)+colorLib.Fore.GREEN+"Lunes y Miercoles 13:00 - 14:55")
    print(colorLib.Cursor.POS(8,20)+colorLib.Fore.GREEN+"x---------------------------x")

def registrationSign(colorLib):
    print(colorLib.Cursor.POS(8,4)+colorLib.Fore.CYAN+"______           _     _             ")
    print(colorLib.Cursor.POS(8,5)+colorLib.Fore.CYAN+"| ___ \         (_)   | |            ")
    print(colorLib.Cursor.POS(8,6)+colorLib.Fore.CYAN+"| |_/ /___  __ _ _ ___| |_ _ __ ___  ")
    print(colorLib.Cursor.POS(8,7)+colorLib.Fore.CYAN+"|    // _ \/ _` | / __| __| '__/ _ \ ")
    print(colorLib.Cursor.POS(8,8)+colorLib.Fore.CYAN+"| |\ \  __/ (_| | \__ \ |_| | | (_) |")
    print(colorLib.Cursor.POS(8,9)+colorLib.Fore.CYAN+"\_| \_\___|\__, |_|___/\__|_|  \___/ ")
    print(colorLib.Cursor.POS(8,10)+colorLib.Fore.CYAN+"            __/ |                    ")
    print(colorLib.Cursor.POS(8,11)+colorLib.Fore.CYAN+"           |___/                     ")

def salesSign(colorLib):
    print(colorLib.Cursor.POS(47,4)+colorLib.Fore.GREEN+" _   _            _             ")
    print(colorLib.Cursor.POS(47,5)+colorLib.Fore.GREEN+"| | | |          | |            ")
    print(colorLib.Cursor.POS(47,6)+colorLib.Fore.GREEN+"| | | | ___ _ __ | |_ __ _ ___  ")
    print(colorLib.Cursor.POS(47,7)+colorLib.Fore.GREEN+"| | | |/ _ \ '_ \| __/ _` / __| ")
    print(colorLib.Cursor.POS(47,8)+colorLib.Fore.GREEN+"\ \_/ /  __/ | | | || (_| \__ \ ")
    print(colorLib.Cursor.POS(47,9)+colorLib.Fore.GREEN+" \___/ \___|_| |_|\__\__,_|___/ ")
                               
def deleteSign(colorLib):
    print(colorLib.Cursor.POS(47,4)+colorLib.Fore.RED+"______       _            ")
    print(colorLib.Cursor.POS(47,5)+colorLib.Fore.RED+"| ___ \     (_)           ")
    print(colorLib.Cursor.POS(47,6)+colorLib.Fore.RED+"| |_/ / __ _ _  __ _ ___  ")
    print(colorLib.Cursor.POS(47,7)+colorLib.Fore.RED+"| ___ \/ _` | |/ _` / __| ")
    print(colorLib.Cursor.POS(47,8)+colorLib.Fore.RED+"| |_/ / (_| | | (_| \__ \ ")
    print(colorLib.Cursor.POS(47,9)+colorLib.Fore.RED+"\____/ \__,_| |\__,_|___/ ")
    print(colorLib.Cursor.POS(47,10)+colorLib.Fore.RED+"           _/ |           ")
    print(colorLib.Cursor.POS(47,11)+colorLib.Fore.RED+"          |__/            ")

def frame(colorLib, system, color):
    system.system('cls')
    
    for superiorL in range(116):
        if(superiorL == 0):
            print(colorLib.Cursor.POS(3,2)+color+"╔", end="")
        elif(superiorL == 115):
            print(colorLib.Cursor.POS(118,2)+color+"╗")
        else:
            print(color+"═", end="")
            
    for leftL in range(25):
        print(colorLib.Cursor.POS(3,3+leftL)+color+"║")

    for inferiorL in range(116):
        if(inferiorL == 0):
            print(colorLib.Cursor.POS(3,28)+color+"╚", end="")
        elif(inferiorL == 115):
            print(colorLib.Cursor.POS(118,28)+color+"╝")
        else:
            print(color+"═", end="")
            
    for rightL in range(25):
        print(colorLib.Cursor.POS(118,3+rightL)+color+"║")
        
def innerFrame(colorLib, system, color):
    for superiorL in range(112):
        if(superiorL == 0):
            print(colorLib.Cursor.POS(5,3)+color+"╔", end="")
        elif(superiorL == 111):
            print(colorLib.Cursor.POS(116,3)+color+"╗")
        else:
            print(color+"═", end="")
            
    for leftL in range(23):
        print(colorLib.Cursor.POS(5,4+leftL)+color+"║")

    for inferiorL in range(112):
        if(inferiorL == 0):
            print(colorLib.Cursor.POS(5,27)+color+"╚", end="")
        elif(inferiorL == 111):
            print(colorLib.Cursor.POS(116,27)+color+"╝")
        else:
            print(color+"═", end="")
            
    for rightL in range(23):
        print(colorLib.Cursor.POS(116,4+rightL)+color+"║")
    
    print(colorLib.Cursor.POS(28,28))
    
def menuFrame(colorLib, system, menuFrameColor):
    for superiorL in range(36):
        if(superiorL == 0):
            print(colorLib.Cursor.POS(44,10)+menuFrameColor+"╔", end="")
        elif(superiorL == 35):
            print(colorLib.Cursor.POS(79,10)+menuFrameColor+"╗")
        else:
            print(colorLib.Cursor.POS(44+superiorL,10)+menuFrameColor+"═", end="")
            
    for leftL in range(10):
        print(colorLib.Cursor.POS(44,11+leftL)+menuFrameColor+"║")

    for inferiorL in range(36):
        if(inferiorL == 0):
            print(colorLib.Cursor.POS(44,21)+menuFrameColor+"╚", end="")
        elif(inferiorL == 35):
            print(colorLib.Cursor.POS(79,21)+menuFrameColor+"╝")
        else:
            print(colorLib.Cursor.POS(44+inferiorL,21)+menuFrameColor+"═", end="")
            
    for rightL in range(10):
        print(colorLib.Cursor.POS(79,11+rightL)+menuFrameColor+"║")
        
def printRegMenu(colorLib,system):
    frameColor = colorLib.Fore.RED
    frame(colorLib,system,frameColor)
    innerFrameColor = colorLib.Fore.RED
    innerFrame(colorLib, system, innerFrameColor)
    registrationSign(colorLib)
    
def printDelMenu(colorLib,system):
    frameColor = colorLib.Fore.CYAN
    frame(colorLib,system,frameColor)
    innerFrameColor = colorLib.Fore.CYAN
    innerFrame(colorLib, system, innerFrameColor)
    deleteSign(colorLib)
    
def printSalesMenu(colorLib,system):
    frameColor = colorLib.Fore.YELLOW
    frame(colorLib,system,frameColor)
    innerFrameColor = colorLib.Fore.YELLOW
    innerFrame(colorLib, system, innerFrameColor)
    salesSign(colorLib)

def getStores():
    import ast
    
    f = open("d08-p14-jose-menendez-W.txt", mode = "r")
    reg = f.readlines()
    f.close()
    
    count = 1
    stores = []
    
    for store in range(len(reg)):
        for line in reg:
            storeId = "t{}".format(str(count))
            if(line.find(storeId) != -1):
                store = ast.literal_eval(line)
                stores.append(store)
        count+=1
        
    return stores

def getEmployees():
    import ast
    
    f = open("d08-p14-jose-menendez-W.txt", mode = "r")
    reg = f.readlines()
    f.close()
    
    count = 1
    employees = []
    
    for employee in range(len(reg)):
        for line in reg:
            employeeId = "e{}".format(str(count))
            if(line.find(employeeId) != -1):
                employee = ast.literal_eval(line)
                employees.append(employee)
        count += 1
        
    return employees

def getProducts():
    import ast
    
    f = open("d08-p14-jose-menendez-W.txt", mode = "r")
    reg = f.readlines()
    f.close()
    
    count = 1
    products = []
    
    for product in range(len(reg)):
        for line in reg:
            productId = "p{}".format(str(count))
            if(line.find(productId) != -1):
                product = ast.literal_eval(line)
                products.append(product)
        count+=1
        
    return products

def storeRegistration(name, phone, mail, colorLib, system):

    stores = getStores()
    
    if(len(stores) == 0):
        storeId = "t{}".format(1)
    else:
        storeId = "t{}".format(len(stores)+1)
            
    fields = ["id:", "nombre:", "telefono:", "correo:"]
    store = dict(zip(fields, [storeId, name, phone, mail]))

    f = open("d08-p14-jose-menendez-W.txt", mode = "a")
    
    f.write(str(store)+"\n")
    f.close()
    
    system.system('cls')
    printRegMenu(colorLib,system)
    print(colorLib.Cursor.POS(52,12)+colorLib.Fore.CYAN+"Fruteria '"+ name +"' registrada con exito")
    print(colorLib.Cursor.POS(52,14)+colorLib.Fore.RED+"Presione ESC para regresar al menu")
    print(colorLib.Cursor.POS(52,15)+colorLib.Fore.RED+"Presione 1 para registrar otra fruteria")

def employeeRegistration(name, salary, colorLib, system):
    
    employees = getEmployees()
    
    if(len(employees) == 0):
        employeeId = "e{}".format(1)
    else:
        employeeId = "e{}".format(len(employees)+1)

    fields = ["id:", "nombre:", "salario:"]
    employee = dict(zip(fields, [employeeId, name, salary]))
    
    f = open("d08-p14-jose-menendez-W.txt", mode = "a")
    
    f.write(str(employee)+"\n")
    f.close()

    system.system('cls')
    printRegMenu(colorLib,system)
    print(colorLib.Cursor.POS(52,12)+colorLib.Fore.CYAN+"El empleado '"+ name +"' registrado con exito")
    print(colorLib.Cursor.POS(52,14)+colorLib.Fore.RED+"Presione ESC para regresar al menu")
    print(colorLib.Cursor.POS(52,15)+colorLib.Fore.RED+"Presione 2 para registrar otro empleado")
    
def productRegistration(name, price, stock, colorLib, system):
    products = getProducts()
    
    if(len(products) == 0):
        productId = "p{}".format(1)
    else:
        productId = "p{}".format(len(products)+1)

    fields = ["id:", "nombre:", "precio:", "cantidad:"]
    product = dict(zip(fields, [productId, name, price, stock]))
    
    f = open("d08-p14-jose-menendez-W.txt", mode = "a")
    
    f.write(str(product)+"\n")
    f.close()

    system.system('cls')
    printRegMenu(colorLib,system)
    print(colorLib.Cursor.POS(52,12)+colorLib.Fore.CYAN+"El producto '"+ name +"' registrado con exito")
    print(colorLib.Cursor.POS(52,14)+colorLib.Fore.RED+"Presione ESC para regresar al menu")
    print(colorLib.Cursor.POS(52,15)+colorLib.Fore.RED+"Presione 3 para registrar otro producto")

def regSelection(colorLib, system, inp, sub):
    step = 1
    while(True):
        opc = ord(inp())
        
        if(opc == 80):
            if(step == 4):
                step = 1
            else:
                step += 1
            registrationOpc(colorLib, system, step)
        elif(opc == 72):
            if(step == 1):
                step = 4
            else:
                step -= 1
            registrationOpc(colorLib, system, step)
        
        if((opc == 13) & (step == 1)) | (opc == 49):
            
            system.system('cls')
            printRegMenu(colorLib,system)                 
            
            print(colorLib.Cursor.POS(52,12)+colorLib.Fore.CYAN+"Registro de Fruteria")
            sub.run('', shell = True)
            
            print(colorLib.Cursor.POS(52,14)+colorLib.Fore.CYAN+"Ingrese el nombre de la fruteria:")
            print(colorLib.Cursor.POS(52,15)+colorLib.Fore.RED+'-> \0337')
            name = str(input('\0338'))
            
            try:
                print(colorLib.Cursor.POS(52,16)+colorLib.Fore.CYAN+"Ingrese el telefono de la fruteria:")
                print(colorLib.Cursor.POS(52,17)+colorLib.Fore.RED+'-> \0337')
                phone = int(input('\0338'))                   
            except:
                print(colorLib.Cursor.POS(52,16)+colorLib.Fore.CYAN+"Ingrese el telefono de la fruteria (solo numeros):")
                print(colorLib.Cursor.POS(52,17)+colorLib.Fore.RED+'-> \0337')
                phone = int(input('\0338')) 
                
            print(colorLib.Cursor.POS(52,18)+colorLib.Fore.CYAN+"Ingrese el correo de la fruteria:")
            print(colorLib.Cursor.POS(52,19)+colorLib.Fore.RED+'-> \0337')
            mail = str(input('\0338'))
            
            while(mail.find("@") == -1 ) | (mail.endswith(".com") == False):
                print(colorLib.Cursor.POS(52,18)+colorLib.Fore.RED+"El correo ingresado no es valido (falta '@' o '.com')")
                print(colorLib.Cursor.POS(52,19)+colorLib.Fore.CYAN+"Ingrese un correo valido:")
                print(colorLib.Cursor.POS(52,20)+colorLib.Fore.RED+'-> \0337')
                mail = str(input('\0338'))
            
            storeRegistration(name, phone, mail, colorLib, system)

        if((opc == 13) & (step == 2)) | (opc == 50):
            system.system('cls')
            printRegMenu(colorLib,system)                 
            
            print(colorLib.Cursor.POS(52,12)+colorLib.Fore.CYAN+"Registro de Empleado")
            sub.run('', shell = True)
            
            print(colorLib.Cursor.POS(52,14)+colorLib.Fore.CYAN+"Ingrese el nombre del empleado:")
            print(colorLib.Cursor.POS(52,15)+colorLib.Fore.RED+'-> \0337')
            name = str(input('\0338'))

            try:
                print(colorLib.Cursor.POS(52,16)+colorLib.Fore.CYAN+"Ingrese el salario del empleado:")
                print(colorLib.Cursor.POS(52,17)+colorLib.Fore.RED+'-> $\0337')
                salary = int(input('\0338'))
            except:
                print(colorLib.Cursor.POS(52,16)+colorLib.Fore.CYAN+"Ingrese el salario del empleado (solo numeros):")
                print(colorLib.Cursor.POS(52,17)+colorLib.Fore.RED+'-> $\0337')
                salary = int(input('\0338'))
            
            employeeRegistration(name, salary, colorLib, system)
        
        if((opc == 13) & (step == 3)) | (opc == 51):
            system.system('cls')
            printRegMenu(colorLib,system)                 
            
            print(colorLib.Cursor.POS(52,12)+colorLib.Fore.CYAN+"Registro de Producto")
            sub.run('', shell = True) 
            
            print(colorLib.Cursor.POS(52,14)+colorLib.Fore.CYAN+"Ingrese el nombre del producto:")
            print(colorLib.Cursor.POS(52,15)+colorLib.Fore.RED+'-> \0337')
            name = str(input('\0338'))
            
            try:
                print(colorLib.Cursor.POS(52,16)+colorLib.Fore.CYAN+"Ingrese el precio del producto:")
                print(colorLib.Cursor.POS(52,17)+colorLib.Fore.RED+'-> $\0337')
                price = int(input('\0338'))
            except:
                print(colorLib.Cursor.POS(52,16)+colorLib.Fore.CYAN+"Ingrese el precio del producto (solo numeros):")
                print(colorLib.Cursor.POS(52,17)+colorLib.Fore.RED+'-> $\0337')
                price = int(input('\0338'))
            
            try:
                print(colorLib.Cursor.POS(52,18)+colorLib.Fore.CYAN+"Ingrese el stock (cantidad) del producto:")
                print(colorLib.Cursor.POS(52,19)+colorLib.Fore.RED+'-> $\0337')
                stock = int(input('\0338'))
            except:
                print(colorLib.Cursor.POS(52,18)+colorLib.Fore.CYAN+"Ingrese el stock del producto (solo numeros):")
                print(colorLib.Cursor.POS(52,19)+colorLib.Fore.RED+'-> $\0337')
                stock = int(input('\0338'))
                
            productRegistration(name, price, stock, colorLib, system)
        if((opc == 13) & (step == 4)) | (opc == 27):
            menu()

def menu():
    import colorama
    import os, sys, subprocess
    from msvcrt import getch
    system = os
    colorLib = colorama
    colorLib.init(autoreset=True)
    inp = getch
    sub = subprocess
    os.system('cls')
    frameColor = colorLib.Fore.GREEN
    menuFrameColor = colorLib.Fore.YELLOW
    
    #Se imprime la intefaz del menu
    frame(colorLib,system,frameColor)
    menuFrame(colorLib, system, menuFrameColor)
    menuInfo(colorLib)
    menuOpc(colorLib, system)
    
    step = 1
    
    while(True):
        opc = ord(getch())
        if(opc == 80):
            if(step == 4):
                step = 1
            else:
                step += 1
            menuOpc(colorLib, system,step)
        elif(opc == 72):
            if(step == 1):
                step = 4     
            else:
                step -= 1
            menuOpc(colorLib, system,step)
        
        #REGISTRO
        if((opc == 13) & (step == 1)) | (opc == 49):
            printRegMenu(colorLib,system)
              
            print(colorLib.Cursor.POS(52,12)+colorLib.Fore.CYAN+"¿Que desea registrar?")
            
            registrationOpc(colorLib, system)
            regSelection(colorLib, system, inp, sub)
        
        #BAJAS
        if((opc == 13) & (step == 2)) | (opc == 50):
            os.system('cls')
            printDelMenu(colorLib,system)
            
            
        #VENTAS
        if((opc == 13) & (step == 3)) | (opc == 51):
            os.system('cls')
            printSalesMenu(colorLib,system)
            
        #SALIR
        if((opc == 13) & (step == 4)) | (opc == 52):
            os.system('cls')
            print("Ha salido del programa...")
            os.system('PAUSE')
            exit()
menu()