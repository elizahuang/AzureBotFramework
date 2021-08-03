import copy
card={
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "My Ehr 快捷儀表板",
            "horizontalAlignment": "Center",
            "height": "stretch",
            "separator": True,
            "spacing": "Medium"
        }
    ],
    "actions": [
        {
            "type": "Action.ShowCard",
            "title": "類別一",
            "card": {
                "type": "AdaptiveCard",
                "actions": [
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://www.google.com/"
                    },
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://tw.yahoo.com/"
                    }
                ]
            },
            "style": "positive"
        },
        {
            "type": "Action.ShowCard",
            "title": "類別二",
            "card": {
                "type": "AdaptiveCard",
                "actions": [
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://www.google.com/"
                    },
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://tw.yahoo.com/"
                    }
                ]
            },
            "style": "positive"
        },
        {
            "type": "Action.ShowCard",
            "title": "類別三",
            "card": {
                "type": "AdaptiveCard",
                "actions": [
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://www.google.com/"
                    },
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://tw.yahoo.com/"
                    }
                ]
            },
            "style": "positive"
        }
    ]
}

card2={
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "My Ehr 快捷儀表板",
            "horizontalAlignment": "Center",
            "height": "stretch",
            "separator": True,
            "spacing": "Medium"
        }
    ],
    "actions": [
        {
            "type": "Action.ShowCard",
            "title": "類別一",
            "card": {
                "type": "AdaptiveCard",
                "actions": [
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://www.google.com/"
                    },
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://tw.yahoo.com/"
                    }
                ]
            },
            "style": "default"
        },
        {
            "type": "Action.ShowCard",
            "title": "類別二",
            "card": {
                "type": "AdaptiveCard",
                "actions": [
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://www.google.com/"
                    },
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://tw.yahoo.com/"
                    }
                ]
            },
            "style": "default"
        },
        {
            "type": "Action.ShowCard",
            "title": "類別三",
            "card": {
                "type": "AdaptiveCard",
                "actions": [
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://www.google.com/",
                        "style": "positive"
                    },
                    {
                        "type": "Action.OpenUrl",
                        "title": "View",
                        "url": "https://tw.yahoo.com/",
                        "style": "positive"
                    }
                ]
            },
            "style": "default"
        }
    ]
}

def prepareEhrCard(choice):
    # myEhrCard=copy.deepcopy(card)
    if choice==1:
        myEhrCard=copy.deepcopy(card)
    else: 
        myEhrCard=copy.deepcopy(card2)

    return myEhrCard