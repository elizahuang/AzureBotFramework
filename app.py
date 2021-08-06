# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys,os
import traceback
from datetime import datetime

from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity, ActivityTypes

from bot import MyBot
from config import DefaultConfig


CONFIG = DefaultConfig()

# Create adapter.
# See https://aka.ms/about-bot-adapter to learn more about how bots work.
SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)


# Catch-all for errors.
async def on_error(context: TurnContext, error: Exception):
    # This check writes out errors to console log .vs. app insights.
    # NOTE: In production environment, you should consider logging this to Azure
    #       application insights.
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity(
        "To continue to run this bot, please fix the bot source code."
    )
    # Send a trace activity if we're talking to the Bot Framework Emulator
    if context.activity.channel_id == "emulator":
        # Create a trace activity that contains the error object
        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error Trace",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        # Send a trace activity, which will be displayed in Bot Framework Emulator
        await context.send_activity(trace_activity)


ADAPTER.on_turn_error = on_error

# Create the Bot
BOT = MyBot()


# Listen for incoming requests on /api/messages
async def messages(req: Request) -> Response:
    # Main bot message handler.
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return Response(status=415)
    activity = Activity().deserialize(body)
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return json_response(data=response.body, status=response.status)
    return Response(status=201)


async def sendReminder(req: Request)-> Response:
    params=req.json()
    print('params',params)
    print('params type',type(params))
    print('params decode',params.decode('utf-8'))
    print('params transfer to json',json.loads(params))
    '''
    ## access token
    url='https://login.microsoftonline.com/botframework.com/oauth2/v2.0/token'
    payload = {'Host': 'login.microsoftonline.com',
        "Content-Type": "application/x-www-form-urlencoded",
        'grant_type':'client_credentials',
        'client_id':'30eba4f2-6e15-458b-9fdf-f8bbf25efb4f',
        'client_secret':'ElizaHuangTaigidian2021',
        'scope':'https://api.botframework.com/.default'}
    
    headers = {}# 
    r = requests.post(url, data=(payload), headers=headers)# data=json.dumps(payload)
    response=json.loads(r.content.decode('utf-8'))
    print('access_token response:\n',response)
    print('type: ',type(response))
    access_token_dict=response
    access_token=response['access_token']

    ## get conversationId
    userId='29:1lNWDIz8Jn0YgoFx8LTJWrkqchAJb1Vg0bJK-PvHxe2FHzNXzFHYaeA0P9j58qQyPVVUCKUfpbZlBNcepHMaajg'
    usesrid_office='29:1htJmKwuNtPEggpMm5kJ73ht47oIbddUOeEh1r1DFpf7vJmh83_C7Q3sBnFcxS3EJv5hHqcu0Po3_-dMmfqnMfA'
    chiahao_usrid='29:1Wp-wm0z5gjBGyNBqmeAnHZVrEz_x8QNh-DQKlIgNuVB59ACaKVJql-cQz2n6IixsodQs12DorLl9c7Rbwi4e9w'
    teams_appid='30eba4f2-6e15-458b-9fdf-f8bbf25efb4f'
    botId='28:30eba4f2-6e15-458b-9fdf-f8bbf25efb4f'
    # tenant_id='9255f64b-1818-42e5-ad78-f619a9a7b1e7'
    tenant_id='010281b3-d5d6-4bc8-b561-bf4794b97036'

    header={'Authorization': 'Bearer ' + access_token} #, 'content-type':'application/json'
    url=f'https://smba.trafficmanager.net/apac/v3/conversations'
    payload={
        "bot": {
            "id": botId,#30eba4f2-6e15-458b-9fdf-f8bbf25efb4f
            # "name": "AzureBot001_Regis"
        },
        "isGroup": False,
        "members": [
            {
                "id": userId,#usesrid_office,
                "name": "借我測試一下"#"Yi Huang 黃懿"
            }
        ],
        "tenantId": tenant_id,
        "topicName": "Testing proactive msg"
    }
    response2= requests.post(url,json=(payload), headers=header).content.decode('utf-8')
    response2=json.loads(response2)
    print('conversationId:\n',response2)
    conversation_id=response2["id"]

    url=f'https://smba.trafficmanager.net/apac/v3/conversations/%s/activities'%(conversation_id)
    payload={
        "type": "message",
        "from": {
            "id": botId,
            "name": "AzureBot001_Regis"
        },
        "conversation": {
            "id": conversation_id,
            "name": "test conversation name"
        },
        "recipient": {
            "id": userId,
            "name": "Yi Huang 黃懿"
        },
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.hero",
                "content": {
                    "title": "title goes here",
                    "subtitle": "subtitle goes here",
                    "text": "descriptive text goes here",
                    "images": [
                        {
                            "url": "https://www.publicdomainpictures.net/pictures/30000/t2/duck-on-a-rock.jpg",
                            "alt": "picture of a duck",
                            "tap": {
                                "type": "playAudio",
                                "value": "url to an audio track of a duck call goes here"
                            }
                        }
                    ],
                    "buttons": [
                        {
                            "type": "playAudio",
                            "title": "Duck Call",
                            "value": "url to an audio track of a duck call goes here"
                        },
                        {
                            "type": "openUrl",
                            "title": "Watch Video",
                            "image": "https://www.publicdomainpictures.net/pictures/30000/t2/duck-on-a-rock.jpg",
                            "value": "url goes here of the duck in flight"
                        }
                    ]
                }
            }
        ]
    }
    response4 = requests.post(url, json=(payload), headers=header)
    response4=response4.content.decode('utf-8')
    print('response3',response3)
    return'''


APP = web.Application(middlewares=[aiohttp_error_middleware])
APP.router.add_post("/api/messages", messages)
APP.router.add_post("/api/v1/cron-messages",sendReminder)


if __name__ == "__main__":
    try:
        # web.run_app(APP, host="localhost", port=CONFIG.PORT)
        port = os.getenv('PORT', default=CONFIG.PORT)
        web.run_app(APP,port=port)
    except Exception as error:
        raise error
