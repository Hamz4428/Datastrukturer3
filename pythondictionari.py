minDict = {"Navn":"","Adresse":"","Postnummer":"", "Poststed":"","Alder":0}
#lages variabel der valuen til keyene i dictionarien blir satt. 
minDict["Navn"] = "Per Spellmann"
minDict["Adresse"] = "Lia 12"
minDict["Postnummer"] = "2000"
minDict["Poststed"] = "Lillestrøm"
minDict["Alder"] = 42
minDict["Kompetanse"] = "Python", "C#", "Database"
#valuen i dictionarien printes ut med en string som passer
print("Navn        : ",minDict["Navn"])
print("Adresse     : ",minDict["Adresse"])
print("Postnummer  : ",minDict["Postnummer"])
print("Poststed    : ",minDict["Poststed"])
print("Alder       : ",minDict["Alder"])
#setter telleren til 1 
teller = 1
#for loop som printer ut til skjerm keyen Kompetanse og valuene dens valuene går opp med 1 etter hver som printes ut og dette skrives også ut
for komp in minDict["Kompetanse"]:
    print(f"Kompeatanse {teller} : ",komp)
    teller +=1


#eksempel2 

#dictionari med ulike valuer 
elever = {
    "Elev1": {
        "Navn":"Per Spellmann",
        "Adresse":"Lia 12",
        "Postnummer":"2000",
        "Poststed":"Lillestrøm",
        "Alder":42,
        "Kompetanse": ["Python", "C#", "Database"]}}
#dictionari med ulike valuer
elever["Elev2"] = {}
elever["Elev2"]["Navn"] = "Kari Spellmann"
elever["Elev2"]["Adresse"] = "Lia 21"
elever["Elev2"]["Postnummer"] = "2013"
elever["Elev2"]["Poststed"] = "Skjetten"
elever["Elev2"]["Alder"] = "35"
elever["Elev2"]["Kompetanse"] = ["SQl","XML","JSON"]
# for loop som printer ut til skjerm i hver linje  en value samt en string som passer til valuen
for elev in elever:
    print("\nNavn          : ",elever[elev]["Navn"])
    print("Adresse       : ",elever[elev]["Adresse"])
    print("Postnummer    : ",elever[elev]["Postnummer"])
    print("Poststed      : ",elever[elev]["Poststed"])
    print("Alder         : ",elever[elev]["Alder"])
    teller = 1
    #for loop som printer ut til skjerm keyen Kompetanse og valuene dens valuene går opp med 1 etter hver som printes ut og dette skrives også ut
    for komp in elever[elev]["Kompetanse"]:
        print(f"Kompeatanse {teller} : ",komp)
        teller +=1
