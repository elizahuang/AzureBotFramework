import copy

card_old={
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
            "title": "類別三",
            "card": {
                "type": "AdaptiveCard",
                "version": "1.3",
                "body": [
                    {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "stretch",
                            "items": [
                                {
                                    "type": "ActionSet",
                                    "actions": [
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "Google1",
                                            "url": "https://www.google.com/",
                                            "style": "positive"
                                        }
                                    ],
                                    "height": "stretch"
                                }
                            ],
                            "style": "accent",
                            "height": "stretch",
                            "verticalContentAlignment": "Center"
                        },
                        {
                            "type": "Column",
                            "width": "stretch",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "description,description,description,description,description,description,description,description,description,description",
                                    "wrap": True
                                }
                            ]
                        },
                        {
                            "type": "Column",
                            "width": "stretch",
                            "items": [
                                {
                                    "type": "ActionSet",
                                    "actions": [
                                        {
                                            "type": "Action.OpenUrl",
                                            "title": "Google1",
                                            "url": "https://www.google.com/",
                                            "style": "positive"
                                        }
                                    ],
                                    "height": "stretch"
                                }
                            ],
                            "style": "accent",
                            "height": "stretch",
                            "verticalContentAlignment": "Center"
                        },
                        {
                            "type": "Column",
                            "width": "stretch",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "description,description,description,description,description,description,description,description,description,description",
                                    "wrap": True
                                }
                            ]
                        }
                    ],
                    "height": "stretch",
                    "separator": True
                }
            ]
            },
            "style": "default"
        }
    ]
}


emptycard={
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
    "actions": []
}

showcardAction={
            "type": "Action.ShowCard",
            "title": "類別三",
            "card": {
                "type": "AdaptiveCard",
                "actions": []
            },
            "style": "default"
        }

singleAction={
            "type": "Action.OpenUrl",
            "title": "View",
            "url": "https://www.google.com/",
            "style": "positive"
        }

def prepareEhrCard():
    infos=[{"name": "Google","url": "https://www.google.com/", "category":"cat 1","description":"nothing"},
    {"name": "Google2","url": "https://www.google.com/", "category":"cat 2","description":"nothing"},
    {"name": "Google2","url": "https://www.google.com/", "category":"cat 2","description":"nothing"},
    {"name": "Google3","url": "https://www.google.com/", "category":"cat 3","description":"nothing"},
    {"name": "Google3","url": "https://www.google.com/", "category":"cat 3","description":"nothing"},
    {"name": "Google3","url": "https://www.google.com/", "category":"cat 3","description":"nothing"},
    {"name": "Google3","url": "https://www.google.com/", "category":"cat 3","description":"nothing"},
    {"name": "Google4","url": "https://www.google.com/", "category":"cat 4","description":"nothing"},
    {"name": "Google4","url": "https://www.google.com/", "category":"cat 4","description":"nothing"},
    {"name": "Google5","url": "https://www.google.com/", "category":"cat 5","description":"nothing"},
    {"name": "Google5","url": "https://www.google.com/", "category":"cat 5","description":"nothing"},
    {"name": "Google5","url": "https://www.google.com/", "category":"cat 5","description":"nothing"},
    {"name": "Google5","url": "https://www.google.com/", "category":"cat 5","description":"nothing"},
    {"name": "Google5","url": "https://www.google.com/", "category":"cat 5","description":"nothing"},
    {"name": "Google5","url": "https://www.google.com/", "category":"cat 5","description":"nothing"}]

    #sort info
    sortedInfoDict={}
    for singleInfo in infos:
        category=singleInfo["category"]
        del singleInfo["category"]
        sortedInfoDict[category]=sortedInfoDict[category]+[singleInfo] if category in sortedInfoDict.keys() else [singleInfo] 

    print('sortedInfoDict: \n', sortedInfoDict)
    
    #fill the card
    myEhrCard=copy.deepcopy(card)

    # myEhrCard=copy.deepcopy(emptycard)
    # for catName,infos in sortedInfoDict.items():
    #     showcardToAdd=copy.deepcopy(showcardAction)
    #     showcardToAdd["title"]=catName
    #     for singleUrlInfo in infos:
    #         actionToAdd=copy.deepcopy(singleAction)
    #         actionToAdd['title']=name

    #     myEhrCard["actions"]+=[showcardToAdd]

    return myEhrCard