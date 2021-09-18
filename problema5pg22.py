x=[1,2,3,4,5]
y=x
produsul_comp_x=1
suma_prim_3_comp_x=x[0]+x[1]+x[2]
suma_toate_comp_y=sum(y)
val_absol_y=abs(y[3])
sum_prim_comp_x_y=x[0]+y[0]
for i in range(len(x)):
    produsul_comp_x*=x[i]
print("Raspunsul c:", produsul_comp_x)   
print("Raspunsul a:",suma_prim_3_comp_x)
print("Raspunsul b:",suma_toate_comp_y)
print("Raspunsul d:",val_absol_y)
print("Raspunsul e:",sum_prim_comp_x_y)
