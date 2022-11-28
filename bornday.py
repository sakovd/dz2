year_born = 1799
day_born = 6
year_input = ""
while not year_input.isdigit():
    year_input = input("В каком году родился А.С. Пушкин? ")

year_input = int(year_input)

if year_input == year_born:
    day_input =""
    while not day_input.isdigit():
        day_input = input("В какой день родился А.С. Пушкин? ")
    day_input=int(day_input)
    if day_input == day_born:
        print("Верно")
    else:
        print("Неверный день рождения")

else:
    print("Неверный год рождения")