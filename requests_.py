import requests

import datetime


def list_sensors():
    url = 'http://127.0.0.1:8000/sensors/'

    result = requests.get(url=url)

    if result.status_code == 200:

        list_id = [id_['id'] for id_ in result.json()]

        if len(result.json()) > 0:
            print('\tСПИСОК ДАТЧИКОВ')
            for dict_ in result.json():
                for key, val in dict_.items():
                    if key == 'id':
                        print(f'\t\tНомер датчика {val}')
                    elif key == 'name':
                        print(f'\t\tНазвание датчика: {val}')
                    elif key == 'description':
                        if dict_['description'] == '':
                            print(f'\t\tМестонахождение: Местонахождение не указано')
                        else:
                            print(f'\t\tМестонахождение: {val}')
                    elif key == 'sensor':
                        if len(val) > 0:
                            list_value_temperature = []
                            list_date_temperature = []
                            for i in val:
                                url = f'http://127.0.0.1:8000/measurement_view/{i}'
                                result = requests.get(url=url)
                                list_value_temperature.append(result.json()['temperature_value'])
                                list_date_temperature.append(result.json()['date'])
                            my_dict = {list_date_temperature[i]: list_value_temperature[i] for i in
                                       range(len(list_value_temperature))}
                            print('\t\t Значения температур: ')
                            for date_, value in my_dict.items():
                                date_ = date_[:10] + " " + date_[11:19]
                                date_ = datetime.datetime.strptime(date_, "%Y-%m-%d %H:%M:%S")

                                date_ = date_.strftime('%d %B %Y %H:%M:%S')

                                print(f"\t\t\t Дата: {date_}, Температура: {value}")

                print('________________')
            return list_id
        else:
            print('\t\tДатчиков в базе данных нет. Сначало их нужно добавить'.upper())


def create_sensor():
    url = 'http://127.0.0.1:8000/sensor_create/'

    while True:
        name_sensor = input('Введите название датчика: ').strip()
        desc = input('Введите месторасположение датчика: ').strip()

        data = {
            'name': name_sensor,
            'description': desc,
        }
        res = requests.post(url=url, data=data)
        if res.status_code == 201:
            print('______________')
            print(f'\t\tДатчик {name_sensor} с месторасположением {desc} успешно создан'.upper())
            print('______________')
            break
        else:
            print('Что-то пошло не так, ')


def update_sensor():
    my_list = list_sensors()
    print('\t Обновление данных о датчике')
    while True:
        try:
            number_sensor = int(input('Для изменения названия датчика введите его номер: '))
            if not my_list is None:
                if number_sensor in my_list:
                    name_sensor = input(f'Введите новое название для датчика с id {number_sensor}: ').title().strip()
                    desc_sensor = input(f'Введите новое название для датчика с id {number_sensor}: ').title().strip()
                    if len(name_sensor) > 0:
                        URL = f'http://127.0.0.1:8000/sensor_update/{number_sensor}'
                        data = {
                            'id': number_sensor,
                            'name': name_sensor,
                            'description': desc_sensor,
                        }
                        result = requests.put(url=URL, data=data)
                        if result.status_code == 200:
                            print("__________________")
                            print(f'\t\tДатчик с id {number_sensor} изменен'.upper())
                            print("__________________")
                            break
                        else:
                            print('Что то пошло не так')
                    else:
                        print('Название датчика должно содержать хотя бы один символ')

                else:
                    print(
                        f'Введенного номера датчика ({number_sensor}) нет в списке датчиков: {", ".join(map(str, my_list))}')


        except ValueError:
            print('Ожидаем только число')


def add_measurement():
    list_id = list_sensors()
    if not list_id is None:
        print('Добавление измерений температуры.'.upper())
        while True:
            try:
                number_id = int(input('Введите номер датчика: '))
                if number_id in list_id:
                    while True:
                        try:
                            temperature_value = int(input(f'Введите значение температуры для датчика # {number_id}: '))
                            break
                        except ValueError:
                            print('Ожидается только число.')
                    url = 'http://127.0.0.1:8000/measurement_add/'
                    data = {
                        'sensor': number_id,
                        'temperature_value': temperature_value,
                        'date': datetime.datetime.now()
                    }
                    res = requests.post(url=url, data=data)
                    if res.status_code == 201:
                        print(
                            f'\t\tЗначение температуры ({temperature_value}) для датчика с номером {number_id} успешно добавлено'.upper())
                        break
                    else:
                        print('Что - то пошло не так')

                else:
                    print(f'Введенного датчика ({number_id}) нет в списке датчиков ({", ".join(map(str, list_id))})')

            except ValueError:
                print('Ожидается только число.')


def main():
    my_dict = {
        'a_s': 'Добавить датчик',
        'l_s': 'Посмотреть список датчиков',
        'u_s': 'Обновить инфо о датчике',
        'a_m': 'Добавить измерение температуры',
        'q': 'Выход',
    }
    while True:

        for k, v in my_dict.items():
            print(f'Команда {k}: Действие - {v}')

        command = input('Введите команду: ').strip().lower()
        if command in my_dict.keys():
            if command == 'a_s':
                create_sensor()
            elif command == 'l_s':
                list_sensors()
            elif command == 'u_s':
                update_sensor()
            elif command == 'a_m':
                add_measurement()
            else:
                print('Вы вышли из скрипта добавления ИНФО о датчиках.')
                break
        else:
            print(f'Вы ввели ({command}) не правильную команду.')


main()
