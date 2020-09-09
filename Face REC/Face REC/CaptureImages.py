#!/usr/bin/env python
# -*- coding: utf-8 -*-

def capture():

    import cv2
    import os

    import Keys
    from Keys import keyz


    os.chdir("./FaceImages/")

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    print("Resim adi : ")
    resimIsmi = raw_input()
    keyz.captureImgName = resimIsmi

    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC
            print("OK..")
            break
        elif k%256 == 32:
            # SPACE
            img_name = "{}{}.png".format(resimIsmi, img_counter)
            cv2.imwrite(img_name, frame)
            keyz.captureName = "./FaceImages/{}".format(img_name)
            print("{} resmi FaceImages kütüphanesine kaydedildi!".format(img_name))
            img_counter += 1

            cv2.destroyAllWindows()


