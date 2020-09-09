#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os


def secim() :

    prompt = '> '
    print "\n"
    print "Hoşgeldiniz %s\n" %os.getlogin()
    print("Islem secimi yapiniz : \n")
    print("[ 1 ] Grup Oluştur \n[ 2 ] Kişi Oluştur \n[ 3 ] Kişi Yüzü Ekle \n[ 4 ] Kişi Yüzü Ara \n[ 5 ] Yüz Tespiti \n[ 6 ] Yüz Tanı \n\n[ 7 ] Grup Sil\n ")
    secim.secim = int(raw_input(prompt))
