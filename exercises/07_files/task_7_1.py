# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
file = open('exercises/07_files/ospf.txt', 'r')
for line in file:

    data = line.replace(',', ' ').replace('[', '').replace(']', '').split()
    # print(data)
    template = f"""
    Prefix                {data[1]}
    AD/Metric             {data[2]}
    Next-Hop              {data[4]}
    Last update           {data[5]}
    Outbound Interface    {data[6]}
    """
    print(template)
file.close()