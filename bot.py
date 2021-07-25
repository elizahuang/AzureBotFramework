# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext,CardFactory,MessageFactory
from botbuilder.schema import ChannelAccount,HeroCard, CardAction, CardImage,ActionTypes ,Attachment,Activity,ActivityTypes
import requests,json

def create_hero_card() -> Attachment:
    herocard = HeroCard(title="推薦以下兩個選項", 
    images=[
        CardImage(
            url="https://sec.ch9.ms/ch9/7ff5/e07cfef0-aa3b-40bb-9baa-7c9ef8ff7ff5/buildreactionbotframework_960.jpg"
        )],
    buttons=[
        CardAction(type=ActionTypes.open_url,title="url1",value="https://www.google.com"),
        CardAction(type=ActionTypes.open_url,title="url2",value="https://www.yahoo.com"),
        ])
    return CardFactory.hero_card(herocard)

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    contextToReturn=None
    async def on_message_activity(self, turn_context: TurnContext):
        print((turn_context.activity))
        # print('activity: ',json.dumps(turn_context.activity, sort_keys=True, indent=4),'\n')
        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
        if turn_context.activity.text=='todo':
            contextToReturn=requests.get('https://jsonplaceholder.typicode.com/todos/1').content.decode('utf-8')
        elif turn_context.activity.text=='my_ehr':
            contextToReturn='https://myehr'
        elif turn_context.activity.text=='card':
            cardAtt = create_hero_card()
            contextToReturn = MessageFactory.attachment(cardAtt)
        elif turn_context.activity.text=='testMessage':
            contextToReturn = MessageFactory.text(
                    "Welcome to CardBot. "
                    + "This bot will show you different types of Rich Cards. "
                    + "Please type anything to get started."
                )
        else:   
            contextToReturn=f"You said '{ turn_context.activity.text }'"
        await turn_context.send_activity(contextToReturn)
        print()
        
    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
