# Install the Python Requests library:
# `pip install requests`

import requests
import json
import os

def face_detect():
    # Face Detect
    # POST https://api.projectoxford.ai/face/v1.0/detect

    import Keys
    from Keys import keyz

    try:
        os.chdir("../")
        data = open(keyz.detectName, 'rb').read()
        response = requests.post(
            url="https://api.projectoxford.ai/face/v1.0/detect",
            data=data,
            params={
                "returnFaceId": "true",
                "returnFaceLandmarks": "true",
                "returnFaceAttributes": "age,gender,smile",
            },
            headers={
                "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
                "Content-Type": "application/octet-stream",
            },
        )

        Q = '{content}'.format(content = response.content)
        Parse_fID = json.loads(Q)

        face_detect.fID = Parse_fID[0]['faceId']
        keyz.detectName = face_detect.fID

        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')




