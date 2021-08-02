import copy

presentCard={
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "所有事項",
            "wrap": True,
            "horizontalAlignment": "Center"
        },
        {
            "type": "FactSet",
            "facts": [
                {
                    "title": "項目 ID",
                    "value": "12342151"
                },
                {
                    "title": "項目名稱",
                    "value": "making cards"
                },
                {
                    "title": "項目日期",
                    "value": "2021-07-31"
                },                
                {
                    "title": "項目內容及備註",
                    "value": "xxxtask contentsxxx"  
                },                        
                {
                    "title": "完成",
                    "value": "False"
                }
            ]
        }
    ]
}

async def addOrUpdateResultCard(singletask):
    cardToReturn=copy.deepcopy(presentCard)
    cardToReturn["body"][1]["facts"][0]["value"]=singletask["todo_id"]
    cardToReturn["body"][1]["facts"][1]["value"]=singletask["todo_name"]
    cardToReturn["body"][1]["facts"][2]["value"]=singletask["todo_date"]
    cardToReturn["body"][1]["facts"][3]["value"]=singletask["todo_contents"]
    cardToReturn["body"][1]["facts"][4]["value"]=singletask["todo_completed"]
    return await cardToReturn