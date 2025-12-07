dis = 1.44 * 1024 * 1024
page = 100
line = 50
symbol = 25
mass_symbol = 4

mass_book = dis//(mass_symbol * symbol * line * page)
# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", int(mass_book))
