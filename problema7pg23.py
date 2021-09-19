zi=["Luni","Marti","Miercuri","Joi","Vineri","Simbata","Duminica"]
venit=[120,340,560,200,180,120,450]
venit_sapt=sum(venit)
media_venit=round(venit_sapt/7,2)
cel_mai_mare_venit=max(venit)
cel_mai_mic_venit=min(venit)
zi_cmmv=[]
zi_cmmicv=[]
for i in range(len(zi)):
    if venit[i]==cel_mai_mare_venit:
        zi_cmmv.append(zi[i])
for i in range(len(zi)):
    if venit[i]==cel_mai_mic_venit:
        zi_cmmicv.append(zi[i])

print("Raspunsul a:", venit_sapt)
print("Raspunsul b:", media_venit)
print("Raspunsul c:", zi_cmmv)
print("Raspunsul d:", zi_cmmicv)micv)
