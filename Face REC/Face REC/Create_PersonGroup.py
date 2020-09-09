# Install the Python Requests library:
# `pip install requests`

import requests
import json


def create_persongroup():
    # Create Person Group
    # PUT https://api.projectoxford.ai/face/v1.0/persongroups/group1

    try:
        response = requests.put(
            url="https://api.projectoxford.ai/face/v1.0/persongroups/group1",
            headers={
                "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "name": "group1"
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')



