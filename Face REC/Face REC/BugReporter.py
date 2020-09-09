# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# # Install the Python Requests library:
# # `pip install requests`
#
# import requests
# import json
# import os
#
#
# import Face_Group_Train
# from Face_Group_Train import face_grouptrain
# import Face_Detect
# from Face_Detect import face_detect
# import Keys
# from Keys import keyz
#
# def face_identify():
#     # Face Identify
#     # POST https://api.projectoxford.ai/face/v1.0/identify
#
#
#
#     key = "40779b4c-5643-4c8a-b115-625c2cfea6bc"
#
#     try:
#         response = requests.post(
#             url="https://api.projectoxford.ai/face/v1.0/identify",
#             params={
#                 "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
#             },
#             headers={
#                 "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
#                 "Content-Type": "application/json; charset=utf-8",
#             },
#             data=json.dumps({
#                 "maxNumOfCandidatesReturned": 1,
#                 "confidenceThreshold": 0.5,
#                 "faceIds": [
#                     "{}".format(key)
#                 ],
#                 "personGroupId": "group1"
#             })
#
#         )
#         print('Response HTTP Status Code: {status_code}'.format(
#             status_code=response.status_code))
#         print('Response HTTP Response Body: {content}'.format(
#             content=response.content))
#     except requests.exceptions.RequestException:
#         print('HTTP Request failed')
#
# def clv():
#
#     import Keys
#     from Keys import keyz
#
#     try:
#         os.chdir("../")
#         data = open(keyz.detectName, 'rb').read()
#         response = requests.post(
#             url="https://api.projectoxford.ai/face/v1.0/detect",
#             data=data,
#             params={
#                 "returnFaceId": "true",
#                 "returnFaceLandmarks": "true",
#                 "returnFaceAttributes": "age,gender,smile",
#             },
#             headers={
#                 "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
#                 "Content-Type": "application/octet-stream",
#             },
#         )
#         Parse_fID = ""
#         Q = '{content}'.format(content=response.content)
#         Parse_fID = json.loads(Q)
#
#         face_detect.fID = Parse_fID['faceId']
#         keyz.detectName = face_detect.fID
#
#         print keyz.detectName
#
#         print('Response HTTP Status Code: {status_code}'.format(
#             status_code=response.status_code))
#         print('Response HTTP Response Body: {content}'.format(
#             content=response.content))
#     except requests.exceptions.RequestException:
#         print('HTTP Request failed')
#
# def vlv():
#
#     import cv2
#     import os
#
#     import Keys
#     from Keys import keyz
#
#
#     os.chdir("./ImageLibrary/")
#
#     cam = cv2.VideoCapture(0)
#
#     cv2.namedWindow("test")
#
#     img_counter = 0
#
#     print("Resim adi : ")
#     resimIsmi = raw_input()
#
#     while True:
#         ret, frame = cam.read()
#         cv2.imshow("test", frame)
#         if not ret:
#             break
#         k = cv2.waitKey(1)
#
#         if k%256 == 27:
#             # ESC pressed
#             print "OK.."
#             break
#         elif k%256 == 32:
#             # SPACE pressed
#             img_name = "{}{}.png".format(resimIsmi, img_counter)
#             cv2.imwrite(img_name, frame)
#             keyz.detectName = "./ImageLibrary/{}".format(img_name)
#             print("{} resmi ImageLibrary kütüphanesine kaydedildi!".format(img_name))
#             img_counter += 1
#
#     cam.release()
#
#     cv2.destroyAllWindows()


vlv()
clv()
face_grouptrain()
face_identify()