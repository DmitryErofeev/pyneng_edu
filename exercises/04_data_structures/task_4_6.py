# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
data_list = ospf_route.split()
prefix = data_list[0]
ad_metric = data_list[1]
next_hop = data_list[3]
last_update = data_list[4]
out_int = data_list[5]

template = '''
{:25} {}
{:25} {}
{:25} {}
{:25} {}
{:25} {}
'''
print(template.format(
        'Prefix', prefix,
        "AD/Metric", ad_metric[1:-2],
        "Next-Hop", next_hop[0:-1],
        "Last update", last_update[0:-1],
        "Outbound Interface", out_int,
))

