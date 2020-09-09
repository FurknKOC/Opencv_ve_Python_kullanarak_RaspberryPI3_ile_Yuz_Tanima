# Install the Python Requests library:
# `pip install requests`

import requests
import json


def delete_person():
    # Face Identify
    # POST https://api.projectoxford.ai/face/v1.0/identify

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
                    "8d801f64-769e-40c7-8a3c-c97ba32dda8d"
                ],
                "personGroupId": "group1"
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


