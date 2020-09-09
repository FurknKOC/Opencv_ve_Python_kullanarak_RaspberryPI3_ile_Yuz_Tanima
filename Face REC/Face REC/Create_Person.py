# Install the Python Requests library:
# `pip install requests`

import requests
import json


def create_person():
    # Create Person
    # POST https://api.projectoxford.ai/face/v1.0/persongroups/group1/persons

    import Keys
    from Keys import keyz

    try:
        response = requests.post(
            url="https://api.projectoxford.ai/face/v1.0/persongroups/group1/persons",
            headers={
                "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "name": "person01"
            })
        )

        Q = '{content}'.format(content = response.content)
        Parse_pID = json.loads(Q)

        create_person.pID = Parse_pID['personId']
        keyz.pID = create_person.pID

        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

