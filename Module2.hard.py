# Дополнительное практическое задание по модулю 2
def shifr_calc(number):
    '''Вычисляет пары цифр в диапозоне от 1 до 20 сумме которых кратно число number'''
    shifr = []
    for i in range(1, 20):
        for k in range(i+1, 20):
            if number % (i + k) == 0:
                shifr.append(i)
                shifr.append(k)
            else:
                continue
    return shifr

number = int(input('Введите число: ')) # Получаем число от пользоваетля
shifr = shifr_calc(number) # Вычисляем шифр
print('Шифр: ')
print(*shifr, sep = '')
