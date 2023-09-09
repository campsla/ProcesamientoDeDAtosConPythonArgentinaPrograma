sueldosAnuales =[300,300,300,300,300,300,500,500,500,500,700,700]
sueldoPromedio=sum(sueldosAnuales)/len(sueldosAnuales)

tipoSalario = ""
if  sueldoPromedio< 300:
    tipoSalario = "Sueldo bajo"
elif sueldoPromedio <= 900:
    tipoSalario = "Sueldo normal"
else:
    tipoSalario = "Sueldo mejor de lo normal"

print(f"El sueldo promedio de Juan es {sueldoPromedio:.2f}")

print(f"Juan está ganando un {tipoSalario}")
    