height_limit = 130
height = input("Fyll i din längd: ")
if str(height) >= str(height_limit):
    print("Välkommen att åka Balder")
elif str(height) < str(height_limit):
    print("Du behäver växa till dig till minst 130 cm innan du får åka Balder")