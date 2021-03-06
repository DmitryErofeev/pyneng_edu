# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
addr = input('Введите IP-адрес в формате "10.0.1.1": ')
octs = addr.split('.')

valip_ip = len(octs) == 4

for i in octs:
   valip_ip = i.isdigit() and 0 <= int(i) <=255 and valip_ip

if valip_ip:
   if addr == '255.255.255.255':
      print('local broadcast')
   elif addr == '0.0.0.0':
      print('unassigned')
   elif 1 <= int(octs[0]) <=223:
      print('unicast')
   elif 224 <= int(octs[0]) <=239:
      print('multicast')
   else:
      print('unused')
else:
   print('Неправильный IP-адрес')