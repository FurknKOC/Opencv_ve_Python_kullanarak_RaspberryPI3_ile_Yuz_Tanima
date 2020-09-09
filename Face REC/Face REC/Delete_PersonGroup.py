# Install the Python Requests library:
# `pip install requests`

import requests


def delete_persongroup():
    # Delete Person Group
    # DELETE https://api.projectoxford.ai/face/v1.0/persongroups/group1

    try:
        response = requests.delete(
            url="https://api.projectoxford.ai/face/v1.0/persongroups/group1",
            params={
                "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
            },
            headers={
                "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
                "Content-Type": "application/json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


