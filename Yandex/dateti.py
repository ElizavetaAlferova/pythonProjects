weight = 75 # Вес
height = 175 # Рост
steps = 8462 # Количество пройденных за день шагов
hours = 2 # Время движения в часах
len_step_m = 0.65 # Длина одного шага в метрах
transfer_coeff = 1000 # Коэффициент перевода значения расстояния из метров в километры

dist = (len_step_m*steps)/transfer_coeff# Напишите формулу расчёта

mean_speed = dist / hours
minutes = hours * 60
congratulations=''
spent_calories = (0.035*weight + (mean_speed**2 / height) * 0.029*weight) * minutes
if dist>=6.5:
    congratulations='Отличный результат! Цель достигнута.'
elif dist>=3.9:
    congratulations = 'Неплохо! День был продуктивным.'
elif dist >=2:
    congratulations="Маловато, но завтра наверстаем!"
else:
    congratulations='Лежать тоже полезно. Главное — участие, а не победа!'
output = f'''
Сегодня вы прошли {steps} шагов.
Пройденная дистанция {dist:.2f} км.
Вы сожгли {spent_calories:.2f} ккл.
{congratulations}'''
print(output)