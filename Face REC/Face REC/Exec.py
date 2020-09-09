#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys
import os

import Ana_Menu
from Ana_Menu import secim
import Add_Person_Face
from Add_Person_Face import add_person_face
import Create_Person
from Create_Person import create_person
import Create_PersonGroup
from Create_PersonGroup import create_persongroup
import Delete_Person
from Delete_Person import delete_person
import Delete_PersonGroup
from Delete_PersonGroup import delete_persongroup
import Face_Detect
from Face_Detect import face_detect
import Face_Group_Train
from Face_Group_Train import face_grouptrain
import Face_Identify
from Face_Identify import face_identify
import Delete_PersonGroup
from Delete_PersonGroup import delete_persongroup
import CaptureImages
from CaptureImages import capture
import Keys
from Keys import keyz
import DetectImage
from DetectImage import detect

def exeter():

    import Ana_Menu
    from Ana_Menu import secim
    import Keys
    from Keys import keyz

    secim()
    secim = secim.secim
    pin = ""
    prompt = '> '


    if secim == 1:

        print "Grup Oluşturuluyor.."
        create_persongroup()

        print "\n\nİşlem tamamlandı, anasayfa için \'A\', çıkış için \'Q\'"
        pin = raw_input(prompt)

        if pin == "q" or pin == "Q":
            return None
        if pin == "a" or pin == "A":
            exeter()

    elif secim == 2:

        print "Kişi Oluşturuluyor.."
        create_person()

        print keyz.pID
        print "\n\nİşlem tamamlandı, anasayfa için \'A\', çıkış için \'Q\'"
        pin = raw_input(prompt)

        if pin == "q" or pin == "Q":
            return None
        if pin == "a" or pin == "A":
            exeter()

    elif secim == 3:

            capture()

            print "Kişi Yüzü Ekleniyor.."
            add_person_face()

            print "\n\nİşlem tamamlandı, anasayfa için \'A\', çıkış için \'Q\'"
            pin = raw_input(prompt)

            if pin == "q" or pin == "Q":
                return None
            if pin == "a" or pin == "A":
                exeter()

    elif secim == 4:

        os.chdir("./FaceImages/")
        resimIsmi = ""
        print "Resim adını giriniz: {}".format(resimIsmi)
        resimIsmi = raw_input(prompt)
        keyz.captureName = "./FaceImages/{}.png".format(resimIsmi)
        keyz.captureImgName = resimIsmi
        add_person_face()

        print "\n\nİşlem tamamlandı, anasayfa için \'A\', çıkış için \'Q\'"
        pin = raw_input(prompt)

        if pin == "q" or pin == "Q":
            return None
        if pin == "a" or pin == "A":
            exeter()

    elif secim == 5:

        detect()

        print "Yüz Tespit Ediliyor.."
        face_detect()
        face_grouptrain()

        keyz.faceID = face_detect.fID

        print keyz.faceID
        print "\n"

        face_identify()


        if keyz.confidence >= 0.5:
            print "{} resmindeki kişi ile {} resmindeki kişi %{} oranla aynıdır.".format(keyz.captureImgName,keyz.detectImgName,keyz.confidence)
        if keyz.confidence == 0:
            print "{} resmindeki kişi ile {} resmindeki kişi, aynı kişi değildir.".format(keyz.captureImgName,keyz.detectImgName)

        raw_input(prompt)

        print "\n\nİşlem tamamlandı, anasayfa için \'A\', çıkış için \'Q\'"
        pin = raw_input(prompt)

        if pin == "q" or pin == "Q":
            return None
        if pin == "a" or pin == "A":
            exeter()

    elif secim == 6:

        print "Grup Tanımlanıyor.."
        face_identify()

        print "\n\nİşlem tamamlandı, anasayfa için \'A\', çıkış için \'Q\'"
        pin = raw_input(prompt)

        if pin == "q" or pin == "Q":
            return None
        if pin == "a" or pin == "A":
            exeter()

    elif secim == 7:

        delete_persongroup()

        print "\n\nİşlem tamamlandı, anasayfa için \'A\', çıkış için \'Q\'"
        pin = raw_input(prompt)

        if pin == "q" or pin == "Q":
            return None
        if pin == "a" or pin == "A":
            exeter()

exeter()