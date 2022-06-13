#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os


list_dir = os.listdir()  # список файлов и папок в директории, где запущена программа
sorted_list_dir = (sorted(list_dir))
print(list_dir)

for files in list_dir:
    print(files)

for files in sorted_list_dir:
    print(files)
