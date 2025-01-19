is_member = False
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt: ")
price = float(price)
if price > level1 and price < level2: #Lägger till ett spann med övre gräns så att det som överstiger nästa rabattnivå går vidare och inte är kvar på 10 %
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
elif price >= level2: #lägger till så att det är denna nivå, eller den lägre rabattnivån
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
if price > level1:
    print("Efter rabatter blir priset...." + str(final_price)) #gör om priset till sträng
elif price < level1:
    print("Priset blir " + str(price)) #lägger till så att om priset understiger rabatten så får man bara info om pris

