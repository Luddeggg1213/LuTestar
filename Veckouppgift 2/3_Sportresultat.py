
print("Matchen är över, nu ska vi räkna ut resultatet!")
Tottenham = input ("Hur många mål gjorde Tottenhamn?")
Liverpool = input("Hur många mål gjorde Liverpool?")

skillnad = abs((int(Tottenham) - int(Liverpool)))

if str(Tottenham) > str(Liverpool):
    print ("Tottenham vann med " + str(skillnad) + " mål!")
elif str(Tottenham) < str(Liverpool):
    print("Livepool vann med " + str(skillnad) + " mål!")
elif str(Tottenham) == str(Liverpool):
    print("Det blev oavgjort")



