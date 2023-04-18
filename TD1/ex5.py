inf2 = {"etudiant_1" : 13 , "etudiant_2" : 17 , "etudiant_3" : 9 , "etudiant_4" : 15 ,
"etudiant_5" : 8 , "etudiant_6" : 14 , "etudiant_7" : 16 , "etudiant_8" : 12 ,
"etudiant_9" : 13 , "etudiant_10" : 15 , "etudiant_11" : 14 , "etudiant_112" : 9 ,
"etudiant_13" : 10 , "etudiant_14" : 12 , "etudiant_15" : 13 , "etudiant_16" : 7 ,
"etudiant_17" : 12 , "etudiant_18" : 15 , "etudiant_19" : 9 , "etudiant_20" : 17}


etudiant_admis={}
etudiant_non_admis={}

for etudiant, note in inf2.items():
    if note >= 10:
        etudiant_admis[etudiant]=note
    else :
        etudiant_non_admis[etudiant]=note
print(etudiant_admis)

somme=0
for note in inf2.values():
    somme+=note
print(f"Moyenne admis : {somme/len(etudiant_admis)}")

print(etudiant_non_admis)
print(f"Moyenne non admis : {sum(etudiant_non_admis.values())/len(etudiant_non_admis)}")
