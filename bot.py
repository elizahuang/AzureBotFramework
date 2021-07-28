# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext,CardFactory,MessageFactory
from botbuilder.schema import ChannelAccount,HeroCard, CardAction, CardImage,ActionTypes ,Attachment,Activity,ActivityTypes
import requests,json

adapCard={
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "type": "AdaptiveCard",
  "version": "1.0",
  "body": [
    {
      "type": "Container",
      "items": [
        {
          "type": "TextBlock",
          "text": "Publish Adaptive Card schema",
          "weight": "bolder",
          "size": "medium"
        },
        {
          "type": "ColumnSet",
          "columns": [
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "Image",
                  "url": "https://pbs.twimg.com/profile_images/3647943215/d7f12830b3c17a5a9e4afcc370e3a37e_400x400.jpeg",
                  "size": "small",
                  "style": "person"
                }
              ]
            },
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "Matt Hidinger",
                  "weight": "bolder",
                  "wrap": True
                },
                {
                  "type": "TextBlock",
                  "spacing": "none",
                  "text": "Created {{DATE(2017-02-14T06:08:39Z, SHORT)}}",
                  "isSubtle": True,
                  "wrap": True
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "Container",
      "items": [
        {
          "type": "TextBlock",
          "text": "Now that we have defined the main rules and features of the format, we need to produce a schema and publish it to GitHub. The schema will be the starting point of our reference documentation.",
          "wrap": True
        },
        {
          "type": "FactSet",
          "facts": [
            {
              "title": "Board:",
              "value": "Adaptive Card"
            },
            {
              "title": "List:",
              "value": "Backlog"
            },
            {
              "title": "Assigned to:",
              "value": "Matt Hidinger"
            },
            {
              "title": "Due date:",
              "value": "Not set"
            }
          ]
        }
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.ShowCard",
      "title": "Comment",
      "card": {
        "type": "AdaptiveCard",
        "body": [
          {
            "type": "Input.Text",
            "id": "comment",
            "isMultiline": True,
            "placeholder": "Enter your comment"
          }
        ],
        "actions": [
          {
            "type": "Action.Submit",
            "title": "OK"
          }
        ]
      }
    },
    {
      "type": "Action.OpenUrl",
      "title": "View",
      "url": "https://adaptivecards.io"
    }
  ]
}

def create_hero_card() -> Attachment:
    herocard = HeroCard(title="推薦以下兩個選項", 
    images=[
        CardImage(
            url="https://ct.yimg.com/xd/api/res/1.2/VhPkyLMc5NAyXyGfjLgA5g--/YXBwaWQ9eXR3YXVjdGlvbnNlcnZpY2U7aD01ODU7cT04NTtyb3RhdGU9YXV0bzt3PTcwMA--/https://s.yimg.com/ob/image/82cbd7d4-5802-4b2b-99bd-690512b34730.jpg"
        )],#https://sec.ch9.ms/ch9/7ff5/e07cfef0-aa3b-40bb-9baa-7c9ef8ff7ff5/buildreactionbotframework_960.jpg
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
        elif turn_context.activity.text=='adaptive':
            contextToReturn =MessageFactory.attachments([Attachment(content_type='application/vnd.microsoft.card.adaptive',
                                      content=adapCard)])
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
