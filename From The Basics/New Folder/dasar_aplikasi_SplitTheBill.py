#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:26:13 2019

@author: zaki
"""
harga = int(input ('Masukkan harga : '))
jumlahOrang = int(input ('Masukkan jumlah orang : '))
pajakMakan = float(input ('Masukkan tax (dalam persen): '))

total = ((harga * (pajakMakan/100)) + harga) / jumlahOrang

round(total)

hasil1 = 'jumlah orang : {0} ' .format(jumlahOrang)
hasil3 = 'pajak yang diberikan : {0}' .format(pajakMakan)
hasil2 = 'Tiap orang harus membayar : {0}' .format(total)

print(hasil1, hasil3,hasil2)
