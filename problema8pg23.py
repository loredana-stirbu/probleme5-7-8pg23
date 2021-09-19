ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
t=[0,-1,-2,-2,0,3,5,7,9,12,12,13,13,13,14,16,16,15,14,12,10,7,4,1]
temp_med=round(sum(t)/24,2)
maxi_temp=max(t)
mini_temp=min(t)
ora_maxt=[]
ora_mint=[]
for i in range(len(ora)):
    if t[i]==maxi_temp:
        ora_maxt.append(ora[i])
for i in range(len(ora)):
    if t[i]==mini_temp:
        ora_mint.append(ora[i])

print("Raspunsul a:", temp_med)
print("Raspunsul b:", maxi_temp, mini_temp)
print("Raspunsul c:", ora_maxt)
print("Raspunsul d:", ora_mint)