#!/usr/bin/env bash

import openpyxl as xl

total = 0
affiliation_data = {}

wb = xl.load_workbook('data.xlsx')

for row in wb["LOCATIONS"]:

    for item in row:

        item = str(item.value).strip()

        if item != 'None':
            total += 1

            if item in affiliation_data:
                affiliation_data[item] += 1
            else:
                affiliation_data[item] = 1


title_cache = []
mega_cache = []

for row in wb["AAAIPressList"]:

    row_values = [str(item.value).strip().lower() for item in row]

    title_cache.append(row_values[2])
    mega_cache.append(row_values[2] + ' ' + row_values[3])

with open('title_cache.txt', 'wb') as f:
    f.write(' '.join(title_cache).encode("utf-8"))

with open('mega_cache.txt', 'wb') as f:
    f.write(' '.join(mega_cache).encode("utf-8"))    