from datetime import datetime


def choose_plural(amount, declensions):
    if amount % 10 == 1 and amount != 11:
        return str(amount) + ' ' + str(declensions[0])
    if amount % 10 in [2, 3, 4] and amount % 100 not in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        return str(amount) + ' ' + str(declensions[1])

    return str(amount) + ' ' + str(declensions[2])


plural_dict = {0: ("день", "дня", "дней"), 1: ("час", "часа", "часов"), 2: ("минута", "минуты", "минут")}
start_course = datetime(year=2022, month=11, day=8, hour=12)
current_datetime = datetime.strptime(input(), "%d.%m.%Y %H:%M")
delta = start_course - current_datetime
print(start_course)
print(current_datetime)
if current_datetime >= start_course:
    print("Курсу уже вышел!")
else:
    if delta.days != 0:  # дней не 0
        if delta.seconds // 3600 != 0:  # часов не 0
            print(f'До выхода курса осталось: {choose_plural(delta.days, plural_dict[0])} '
                  f'и {choose_plural(delta.seconds // 3600, plural_dict[1])}')
        else:
            print(f'До выхода курса осталось: {choose_plural(delta.days, plural_dict[0])} ')
    else:
        if delta.seconds // 3600 != 0:  # часов не 0
            if (delta.seconds // 60) % 60 != 0:  # секунд не 0
                print(f'До выхода курса осталось: {choose_plural(delta.seconds // 3600, plural_dict[1])} '
                      f'и {choose_plural((delta.seconds // 60) % 60, plural_dict[2])}')
            else:
                print(f'До выхода курса осталось: {choose_plural(delta.seconds // 3600, plural_dict[1])} ')
        else:
            print(f'До выхода курса осталось: {choose_plural((delta.seconds // 60) % 60, plural_dict[2])}')
