# Install the Python Requests library:
# `pip install requests`

import requests


def face_grouptrain():
    # Person Group Train
    # POST https://api.projectoxford.ai/face/v1.0/persongroups/group1/train

    try:
        response = requests.post(
            url="https://api.projectoxford.ai/face/v1.0/persongroups/group1/train",
            headers={
                "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


