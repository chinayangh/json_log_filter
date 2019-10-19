# -*- coding: utf-8 -*-
# !/usr/bin/python
import json

with open("c:/users/lenovo/desktop/log.json", 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    a = load_dict["hits"]
    # print(type(a))
    # print(a)
    # print(a.keys())
    b = (a["hits"])
    # print(type(b))
    # print(type(b[3]))
    # print(b[3].keys())
    print('{:20}|{:^20}|{}'.format('Hostname', 'IP', 'Message'))
    for i in b:
        # print(i)
        # print(b[i]["_source"]["hostname"])
        # print(b[i]["_source"]["ip"])
        # print(b[i]["_source"]["message"])
        # print(b[b.index(i)]["_source"]["hostname"])
        # print(b[b.index(i)]["_source"]["ip"])
        # print(b[b.index(i)]["_source"]["message"])
        hst, ip, msg = (i["_source"]["hostname"], i["_source"]["ip"], i["_source"]["message"])
        # print(i["_source"]["hostname"])
        # print(i["_source"]["ip"])
        # print(i["_source"]["message"])
        # print(hst, ip, msg)
        # print('{:20}|{:^20}|{}'.format('Hostname', 'IP', 'Message'))
        # print('{:20}|{:^20}|{:15}'.format(hst, ip, msg))
        # print('{:20}|{:20}|{:15}'.format(hst, ip, msg))
        print('{:20}|{:20}|{}'.format(hst, ip, msg))
        with open("c:/users/lenovo/desktop/data.txt", 'a') as data_f:
            # data_f.write('{:20}|{:20}|{}'.format(hst, ip, msg))
            data_f.write('{:20}|{:20}|{}\n'.format(hst, ip, msg))
