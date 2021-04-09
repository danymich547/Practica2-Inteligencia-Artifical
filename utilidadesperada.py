import math

print("\n\nINSERTE DATOS DE LA PRIMERA OPCION\n")
val1 = float(input("Cantidad a ganar:\t"))
pbd1 = float(input("Probabilidad de ganar:\t"))
val2 = float(input("Cantidad a perder:\t"))
pbd2 = float(input("Probabilidad de perder:\t"))

print("\n\nINSERTE DATOS DE LA SEGUNDA OPCION\n")
valA = float(input("Cantidad a ganar:\t"))
pbdA = float(input("Probabilidad de ganar:\t"))
valB = float(input("Cantidad a perder:\t"))
pbdB = float(input("Probabilidad de perder:\t"))

print("\nLa primera opcion es:\nGanar ", val1," con ", pbd1, " de probabilidad o perder ", val2, " con ", pbd2, " de probabilidad \n")
print("\nLa segunda opcion es:\nGanar ", valA," con ", pbdA, " de probabilidad o perder ", valB, " con ", pbdB, " de probabilidad \n")

#Para obtener el resultado de la utilidad esperada se ocupa la siguiente formula
#UE=P1*Uxi + P2*Ux2
#Para obtener el valor de la utilidad se debe realizar lo siguiente: U=1/3(x)**2

rzc = (val1**2)
rzc1 =(val2**2)
UE1 = round( ((pbd1)*(pow (rzc,1/3))) + ((pbd2)*(pow (rzc1,1/3))) , 3)
print("El resultado de la utilidad esperada de la primera opcion es:",UE1)


raizc= (valA**2)
raizc1 =(valB**2)
UE2 = round(((pbdA)*(pow (raizc,1/3))) + ((pbdB)*(pow (raizc1,1/3))),3)
print("El resultado de utilidad esperada de la segunda opcion es: ", UE2)
round (UE2,2)

if(UE1>UE2):
	print("\n MEJOR RESULTADO CON GRAN UTILIDAD ES: PRIMERA OPCION :3")
else:
	print("\n MEJOR RESULTADO con GRAN UTILIDAD ES: SEGUNDA OPCION :3")
