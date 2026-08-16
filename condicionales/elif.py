ingreso_mensual = 1200
gasto_mensual = 500

#if anidados y else if (elif)

if ingreso_mensual >= 1200:
    if ingreso_mensual - gasto_mensual >= 500:
        print("Estas gastando bien tu sueldo, dinero actual:", {ingreso_mensual}, "dolares")
    elif ingreso_mensual - gasto_mensual < 0:
        print("estas gastando demasiado / deficit") 
    else:
        print("Estas gastando mas de lo que ganas / Deficit")
    
    
#if ingreso_mensual >= 1000:
   # print("Estas bien economicamente ganando:", {ingreso_mensual}, "$ en chile")
    
#elif ingreso_mensual > 500:
    #print("Estas relativamente estable economicamente en chile") 

#else:
    #print("No estas bien economicamente en chile")


