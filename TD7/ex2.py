import csv
import pandas as pd

def resultat(etudiant):
    #etudiant correspond à une ligne du data frame
    #etudiant.Nom, etudiant.median, ...
    if (pd.isnull(etudiant.TP)  or pd.isnull(etudiant.final)) :
        return "_ABS"
    if (etudiant.final<6 or etudiant.Moyenne<10):
        return "F"
    if (etudiant.Moyenne<11):
        return "E"
    if (etudiant.Moyenne<13):
        return "D"
    if (etudiant.Moyenne<15):
        return "C"
    if (etudiant.Moyenne<17):
        return "B"
    else :
        return "A"

def exo2():
    data=pd.read_csv("notes.csv", delimiter=';')
    print(data)
    data['Moyenne']=data['TP']*0.25 + data['median']*0.35 + data['final']*0.40
    print(data)
    data['Resultat']=data.apply(resultat, axis=1)
    print(data)
    data.sort_values(by=["Moyenne", "final"], ascending=False,inplace=True ) #en cas egalite moyenne, classé par final
    print(data)
    data.to_csv("juryINF2.csv")



if __name__ == '__main__':
    exo2()
