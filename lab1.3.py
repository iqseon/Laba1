def get_price(price):
    for i in range(1, 11):
        print(f'Цена за {i} кг апельсин равна {i * price} $')

    count = 1
    while True:
        print(f'Цена за {count} кг апельсин равна {count * price} $')
        count += 1
        if count == 11:
            break


get_price(50)
print()