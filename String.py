#STRING
#først lages det variabel med en string verdi deretter printes dette variablen ut med en annen string 
# så printes hver bokstav i stringen på seperate linjer og de har fått tildelt ett nummer hver som sier posisjonen dems i stringen dette blir gjort ved en for loop og en variabel med verdi 1 
melding = "Hallo Verden!"

print("String inneholder: ",melding)
teller = 1
for bokstav in melding:
    print("Plassholder",teller,"i string er:",bokstav)
    teller+=1
