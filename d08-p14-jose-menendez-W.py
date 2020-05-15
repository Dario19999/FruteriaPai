def menuOpc(colorLib, system,selected = 1):
    if(selected == 1):
        print(colorLib.Cursor.POS(50, 12)+colorLib.Fore.RED+colorLib.Back.WHITE+"      [1] Registro      ")
    else:
        print(colorLib.Cursor.POS(50, 12)+colorLib.Fore.YELLOW+"      [1] Registro      ")
    if(selected == 2):
        print(colorLib.Cursor.POS(50, 14)+colorLib.Fore.RED+colorLib.Back.WHITE+"      [2] Bajas         ")
    else:
        print(colorLib.Cursor.POS(50, 14)+colorLib.Fore.YELLOW+"      [2] Bajas          ")
    if(selected == 3):
        print(colorLib.Cursor.POS(50, 16)+colorLib.Fore.RED+colorLib.Back.WHITE+"      [3] Ventas        ")
    else:
        print(colorLib.Cursor.POS(50, 16)+colorLib.Fore.YELLOW+"      [3] Ventas        ")
    if(selected == 4):
        print(colorLib.Cursor.POS(50, 18)+colorLib.Fore.RED+colorLib.Back.WHITE+"      [4] Salir         ")
    else:
        print(colorLib.Cursor.POS(50, 18)+colorLib.Fore.YELLOW+"      [4] Salir         ")
    print(colorLib.Cursor.POS(28,28))

def menuInfo(colorLib, system):
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
    print(colorLib.Cursor.POS(10,16)+colorLib.Fore.GREEN+"XXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(colorLib.Cursor.POS(10,17)+colorLib.Fore.GREEN+"XXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(colorLib.Cursor.POS(8,18)+colorLib.Fore.GREEN+"x---------------------------x")

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
        
def menu():
    import colorama
    import os, sys, subprocess
    from msvcrt import getch
    system = os
    colorLib = colorama
    colorLib.init(autoreset=True)
    
    os.system('cls')
    frameColor = colorLib.Fore.GREEN
    menuFrameColor = colorLib.Fore.YELLOW
    
    #Se imprime la intefaz del menu
    frame(colorLib,system,frameColor)
    menuFrame(colorLib, system, menuFrameColor)
    menuInfo(colorLib, system)
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
            frameColor = colorLib.Fore.RED
            frame(colorLib,system,frameColor)
            innerFrameColor = colorLib.Fore.RED
            innerFrame(colorLib, system, innerFrameColor)
            
            # subprocess.run('', shell = True)
            # print(colorLib.Cursor.POS(46, 12)+colorLib.Fore.GREEN+'-> \0337')
            # name = str(input('\0338'))

        #BAJAS
        if((opc == 13) & (step == 2)) | (opc == 50):
            os.system('cls')
            frameColor = colorLib.Fore.CYAN
            frame(colorLib,system,frameColor)
            innerFrameColor = colorLib.Fore.CYAN
            innerFrame(colorLib, system, innerFrameColor)
            
            # step = 0
            # selectFile(txtFiles,step)
            
            # while(True):
            #     opc = ord(getch())
            #     if(opc == 80):
            #         if(step == len(txtFiles)-1):
            #             step = 0
            #         else:
            #             step += 1
            #         # selectFile(txtFiles,step)
            #     elif(opc == 72):
            #         if(step == 0):
            #             step = len(txtFiles)-1   
            #         else:
            #             step -= 1
            #         # selectFile(txtFiles,step)
            #     elif(opc == 13):
            #         # editFile(txtFiles[step], txtFiles)
            #     # elif(opc == 27):
            #     #     menu()
            
        #VENTAS
        if((opc == 13) & (step == 3)) | (opc == 51):
            os.system('cls')
            frameColor = colorLib.Fore.YELLOW
            frame(colorLib,system,frameColor)
            innerFrameColor = colorLib.Fore.YELLOW
            innerFrame(colorLib, system, innerFrameColor)
            
        #SALIR
        if((opc == 13) & (step == 4)) | (opc == 52):
            os.system('cls')
            print("Ha salido del programa...")
            os.system('PAUSE')
            exit()
menu()