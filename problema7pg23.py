zi=["Luni","Marti","Miercuri","Joi","Vineri","Simbata","Duminica"]
venit=[120,340,560,200,180,230,450]
venit_sapt=sum(venit)
media_venit=round(venit_sapt/7,2)
cel_mai_mare_venit=max(venit)
pozitia_cmmv=venit.index(cel_mai_mare_venit)
ziua_cu_cmmv=zi[pozitia_cmmv]
cel_mai_mic_venit=min(venit)
pozitia_cmmicv=venit.index(cel_mai_mic_venit)
ziua_cu_cmmicv=zi[pozitia_cmmicv]
print("Raspunsul a:", venit_sapt)
print("Raspunsul b:", media_venit)
print("Raspunsul c:", ziua_cu_cmmv)
print("Raspunsul d:", ziua_cu_cmmicv)