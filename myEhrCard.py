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
                                    "height": "stretch",
                                    "wrap":True
                                }
                            ],
                            "style": "default",
                            "height": "stretch",
                            "verticalContentAlignment": "Center",
                            "width": 30,
                        },
                        {
                            "type": "Column",
                            "width": 70,
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
                    },
                    {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": 30,
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
                                    "height": "stretch",
                                    "wrap":True
                                }
                            ],
                            "style": "default",
                            "height": "stretch",
                            "verticalContentAlignment": "Center"
                        },
                        {
                            "type": "Column",
                            "width": 70,
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


def prepareEhrCard():
    infos=[{"name": "Google","url":"https://www.google.com/","category":"cat 1", "description":"description,description,description,description,description,description"},
    {"name": "Google2","url":"https://www.google.com/","category":"cat 2", "description":"description,description,description,description,description,description"},
    {"name": "Google2","url":"https://www.google.com/","category":"cat 2", "description":"description,description,description,description,description,description"},
    {"name": "Google2","url":"https://www.google.com/","category":"cat 2", "description":"description,description,description,description,description,description"},
    {"name": "Google3","url":"https://www.google.com/","category":"cat 3", "description":"description,description,description,description,description,description"}    ]
        
    sortedInfoDict={}
    for info in infos:
        category=info["category"]
        del info["category"]
        sortedInfoDict[category]=sortedInfoDict[category]+[info] if category in sortedInfoDict.keys() else [info]

    print('sortedInfoDict\n',sortedInfoDict)  


    myEhrCard=copy.deepcopy(card)
    return myEhrCard