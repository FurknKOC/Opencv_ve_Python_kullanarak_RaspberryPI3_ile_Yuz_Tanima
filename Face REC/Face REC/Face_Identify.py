#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Install the Python Requests library:
# `pip install requests`

import requests
import json
import os

def face_identify():
    # Face Identify
    # POST https://api.projectoxford.ai/face/v1.0/identify

    import Keys
    from Keys import keyz

    os.chdir("../")

    try:
        response = requests.post(
            url="https://api.projectoxford.ai/face/v1.0/identify",
            params={
                "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
            },
            headers={
                "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "maxNumOfCandidatesReturned": 1,
                "confidenceThreshold": 0.5,
                "faceIds": [
                    "{}".format(keyz.detectName)
                ],
                "personGroupId": "group1"
            })
        )

        try:
            Q = '{content}'.format(content=response.content)
            Parse_confidence = json.loads(Q)
            face_identify.confidence = Parse_confidence[0]['candidates'][0]['confidence']
            keyz.confidence = face_identify.confidence

        except IndexError:
            print "Kişiler aynı değildir."
            keyz.confidence = 0

       # if Parse_confidence[0]['candidates'] == None:
       #     keyz.confidence = 0
        #else:
         #   face_identify.confidence = Parse_confidence[0]['candidates'][0]['confidence']
          #  keyz.confidence = face_identify.confidence


        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


