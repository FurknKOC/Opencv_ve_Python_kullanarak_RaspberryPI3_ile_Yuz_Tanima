#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Install the Python Requests library:
# `pip install requests`

import requests
import json
import os


def add_person_face():
    # Add Person Face
    # POST https://api.projectoxford.ai/face/v1.0/persongroups/group1/persons/3fc6716d-8d6b-463b-99cb-c7381b68b888/persistedFaces

    import Keys
    from Keys import keyz


    try:
        os.chdir("../")
        data = open(keyz.captureName, 'rb').read()
        response = requests.post(
            url="https://api.projectoxford.ai/face/v1.0/persongroups/group1/persons/{}/persistedFaces".format(keyz.pID),
            data=data,
            headers={
                "Ocp-Apim-Subscription-Key": "8007d3f4ca0041ae8d0c708fd5c1b7d5",
                "Content-Type": "application/octet-stream",

            },
        )
        print keyz.captureName

        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')



