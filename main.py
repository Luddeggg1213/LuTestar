# Övning 1
print("Hello World")
print("This program was made by Ludvig")

# Övning 2
x = 100
y = 200

#Felet är att konverteringen saknades. Jag löste med att ange kommatecken, mina kompisar löste det med att ange str(variabel) med print(f
print ("Det blir ", + y - x, " kronor över.")
# Hälften av vad? Nedanstående är alltså hälften av 100 och 200 minus det som blir 200-50 = 150 tolkar jag det som och skrev därmed som kod. De andra i gruppen tolkade som att det skulle vara hälften av allt, dvs 200-100 = 100 och sedan hälften som är 50.
z = 200 - 100 / 2

print("Hälften är: ", + z)

# Övning 3
# 3 1a)
x = input("Ange ett heltal här ")

y = input("Ange ett till heltal här ")

# 3 1b)
#Varför ett f nedan?
print(f"Summan av talen= {int(x) + int(y)} ")

# 3 2a)
jacka = 2000
rabattSumma = jacka * 0.5
slutSumma = jacka - rabattSumma

print("Jackan kostar: " + str(slutSumma) + " kronor med " + str(rabattSumma) + " % rabatt.")

# 3 2b)
jacka = 2000
rabatt = input("Vilken rabatt är det på jackan? ")
rabattSumma = jacka * (int(rabatt) / 100)
slutSumma = jacka - rabattSumma

print("Jackan kostar: " + str(slutSumma) + " kronor med " + str(rabatt) + " % rabatt.")


# 4 1a) neandstående får jag inte till så att det fungerar
v = input("Hur fort kommer du köra i km/h? ")
S = 470
tid = float(S) / float(v)

print("Det kommer ta " + str(tid) + " timmar")


# Övning 5
#Ej hunnit göra denna
