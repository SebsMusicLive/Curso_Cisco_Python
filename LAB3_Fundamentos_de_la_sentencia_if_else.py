# Se acepta el valor
ingreso = float(input("Ingresa el valor de tus ingresos\n"))

# Condicional
if(ingreso<=85528): impuesto = (ingreso*0.18)-556.2
else: impuesto = 14839.2+((ingreso-85528)*0.32)

if(impuesto < 0): impuesto = .0

#Imprime resultado
print("El impuesto es:",float(round(impuesto)),"pesos")