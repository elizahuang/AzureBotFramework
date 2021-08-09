#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    # APP_ID = os.environ.get("MicrosoftAppId", "30eba4f2-6e15-458b-9fdf-f8bbf25efb4f")
    # APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "ElizaHuangTaigidian2021")
    CONNECTION_NAME = os.environ.get("ConnectionName", "")
    SERVICE_URL=os.environ.get("Service_url", "https://smba.trafficmanager.net/apac/")
    APP_ID = os.environ.get("MicrosoftAppId", "37a137cd-6495-44f6-885d-106cdde6afe6")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "}T1m:qf^dUH-jhD_JDZ]v}G2KXx23jJ")
    
# https://azure-bot-framework.herokuapp.com/api/messages