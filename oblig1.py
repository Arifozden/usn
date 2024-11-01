#Oppgave

#Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil.

#Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. Du kan her for enkelhets skyld se bort fra kostnader som renter på billån og verditap (du har da egentlig antatt at slike kostnader er like for elbil og bensinbil).

#Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)

#    Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
#    Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
#    Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
#    Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
#    Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

km_per_år = 10000 #Antall kjørte km/år

forsikring_elbil = 5000 #Forsikring for elbil
forsikring_bensinbil = 7500 #Forsikring for bensinbil

trafikkforsikringsavgift = 8.38*365 #Trafikkforsikringsavgift per år  (1 år = 365 dager)

strømpris = 2.00 #Strømpris per kWh
strømforbruk = 0.2 #Strømforbruk per km
drivstoffkostnad_elbil = strømpris * strømforbruk * km_per_år #Drivstoffkostnad for elbil

bensinpris = 1.0 #Bensinpris per km
drivstoffkostnad_bensinbil = bensinpris * km_per_år #Drivstoffkostnad for bensinbil

bomavgift_elbil = 0.1 * km_per_år #Bomavgift for elbil
bomavgift_bensinbil = 0.3 * km_per_år #Bomavgift for bensinbil

elbil_kostnad = forsikring_elbil + trafikkforsikringsavgift + drivstoffkostnad_elbil + bomavgift_elbil #Totalkostnad for elbil

bensinbil_kostnad = forsikring_bensinbil + trafikkforsikringsavgift + drivstoffkostnad_bensinbil + bomavgift_bensinbil #Totalkostnad for bensinbil

kostnadsdifferanse = elbil_kostnad - bensinbil_kostnad #Årlig kostnadsdifferanse

print("Total årlige kostnader for elbil og bensinbil for ", km_per_år, " km per år")
print("Årlig totalkostnad for elbil: ", elbil_kostnad)
print("Årlig totalkostnad for bensinbil: ", bensinbil_kostnad)
print("Årlig kostnadsdifferanse: ", kostnadsdifferanse)
