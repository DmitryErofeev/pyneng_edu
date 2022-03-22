# -*- coding: utf-8 -*-
"""
sw1#sh mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
 100    01bb.c580.7000    DYNAMIC     Gi0/1
 200    0a4b.c380.7c00    DYNAMIC     Gi0/2
 300    a2ab.c5a0.700e    DYNAMIC     Gi0/3
 10     0a1b.1c80.7000    DYNAMIC     Gi0/4
 500    02b1.3c80.7b00    DYNAMIC     Gi0/5
 200    1a4b.c580.7000    DYNAMIC     Gi0/6
 300    0a1b.5c80.70f0    DYNAMIC     Gi0/7
 10     01ab.c5d0.70d0    DYNAMIC     Gi0/8
 1000   0a4b.c380.7d00    DYNAMIC     Gi0/9


Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan_number = input("Введите номер влана: ")



with open("/home/nnm/pyneng_edu/exercises/07_files/CAM_table.txt") as f:
    for line in f:
        word = line.split()
        if word and word[0].isdigit() and word[0] == vlan_number:
            vlan, mac, _, port = word
            print(f"{vlan:9}{mac:20}{port}")

