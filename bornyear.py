year_born = 1799
year_input = ""
while not year_input.isdigit():
    year_input = input("В каком году родился А.С. Пушкин? ")

year_input = int(year_input)

if year_input == year_born:
    print("Верно")
else:
    print("Неверно")