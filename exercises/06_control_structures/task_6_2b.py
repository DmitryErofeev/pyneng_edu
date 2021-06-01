# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


while True:
    addr = input('Введите IP-адрес в формате "10.0.1.1": ')
    octs = addr.split('.')

    valip_ip = len(octs) == 4

    for i in octs:
        valip_ip = i.isdigit() and 0 <= int(i) <=255 and valip_ip

    if valip_ip:
        break
    print('Неправильный IP-адрес')


if valip_ip:
    if addr == '255.255.255.255':
        print('local broadcast')
        correct = True
    elif addr == '0.0.0.0':
        print('unassigned')
        correct = True
    elif 1 <= int(octs[0]) <=223:
        print('unicast')
        correct = True
    elif 224 <= int(octs[0]) <=239:
        print('multicast')
        correct = True
    else:
        print('unused')
        correct = True
