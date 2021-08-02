import copy
updateCard_oldver={
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.0",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "Update Todo Task",
            "horizontalAlignment": "Center",
            "wrap": True
        },
        {
            "type": "TextBlock",
            "text": "Task_ID:  "+"12342151",
            "wrap": True,
            "id": "show_task_id",
            "separator": True,            
        },
        {
            "type": "TextBlock",
            "text": "Task Name",
            "wrap": True,
            "id": "task_name_label",
            "separator": True,
        },       
        {
            "type": "Input.Text",
            "style": "text",
            "id": "todo_name",
            "isRequired": True,
            "errorMessage": "Task name is required",
            "value": "Original_task_name",
            "spacing": "Padding"
        },
        {
            "type": "TextBlock",
            "text": "Task Start Date Time",
            "wrap": True,
            "id": "task_start_label",
            "separator": True,
        },     
        {
            "type": "Input.Date",
            "isRequired": True,
            "errorMessage": "Start date for the task is required",
            "id": "start_date",
            "value": "2021-08-01"
        },
        {
            "type": "Input.Time",
            "id": "start_time",
            "value": "16:59"
        },
        {
            "type": "TextBlock",
            "text": "Task End Date Time",
            "wrap": True,
            "id": "task_end_label",
            "separator": True,
        },             
        {
            "type": "Input.Date",
            "isRequired": True,
            "errorMessage": "End date for the task is required",
            "id": "end_date",
            "value": "2021-08-01"
        },
        {
            "type": "Input.Time",
            "id": "end_time",
            "value": "16:59"
        },
        {
            "type": "TextBlock",
            "text": "Task Contents",
            "wrap": True,
            "id": "task_content_label",
            "separator": True,
        },             
        {
            "type": "Input.Text",
            "style": "text",
            "isMultiline": True,
            "id": "todo_contents"
        },
        {
            "type": "Input.Toggle",
            "title": "Task Complete",
            "value": "false",
            "id": "todo_completed",
            "separator": True,
        },
        {
            "type": "Container",
            "items": [
                {
                    "type": "ActionSet",
                    "horizontalAlignment": "Center",
                    "actions": [
                        {
                            "type": "Action.Submit",
                            "title": "Submit",
                            "style": "positive",
                            "data": {
                                "card_request_type": "submit_update",
                                "task_id": "12342151"
                            },
                            "id": "update_task_submit",
                            "associatedInputs": "auto"
                        }
                    ]
                }
            ]
        }
        
    ],
}

updateCard={
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.0",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "更新代辦事項",
            "horizontalAlignment": "Center",
            "wrap": True
        },
        {
            "type": "TextBlock",
            "text": "項目_ID:  "+"12342151",
            "wrap": True,
            "id": "show_task_id",
            "separator": True,            
        },
        {
            "type": "TextBlock",
            "text": "項目名稱：",
            "wrap": True,
            "id": "task_name_label",
            "separator": True,
        },       
        {
            "type": "Input.Text",
            "style": "text",
            "id": "todo_name",
            "isRequired": True,
            "errorMessage": "Task name is required",
            "value": "Original_task_name",
            "spacing": "Padding"
        },
        {
            "type": "TextBlock",
            "text": "日期：", #/時間
            "wrap": True,
            "id": "task_start_label",
            "separator": True,
        },     
        {
            "type": "Input.Date",
            "isRequired": True,
            "errorMessage": "Start date for the task is required",
            "id": "start_date",
            "value": "2021-08-01"
        },
        {
            "type": "Input.Time",
            "id": "start_time",
            "value": "16:59",
            "isVisible": False
        },
        {
            "type": "TextBlock",
            "text": "Task End Date Time",
            "wrap": True,
            "id": "task_end_label",
            "separator": True,
            "isVisible": False
        },             
        {
            "type": "Input.Date",
            "isRequired": True,
            "errorMessage": "End date for the task is required",
            "id": "end_date",
            "value": "2021-08-01",
            "isVisible": False
        },
        {
            "type": "Input.Time",
            "id": "end_time",
            "value": "16:59",
            "isVisible": False
        },
        {
            "type": "TextBlock",
            "text": "項目內容及備註：",
            "wrap": True,
            "id": "task_content_label",
            "separator": True,
        },             
        {
            "type": "Input.Text",
            "style": "text",
            "isMultiline": True,
            "id": "todo_contents"
        },
        {
            "type": "Input.Toggle",
            "title": "已完成",
            "value": "false",
            "id": "todo_completed",
            "separator": True,
        },
        {
            "type": "Container",
            "items": [
                {
                    "type": "ActionSet",
                    "horizontalAlignment": "Center",
                    "actions": [
                        {
                            "type": "Action.Submit",
                            "title": "送出更新",
                            "style": "positive",
                            "data": {
                                "card_request_type": "submit_update",
                                "task_id": "12342151"
                            },
                            "id": "update_task_submit",
                            "associatedInputs": "auto"
                        }
                    ]
                }
            ]
        }
        
    ],
}
def prepareUpdateCard(singletask):
    cardToReturn=copy.deepcopy(updateCard)    
    singletask={"todo_id":"123123","todo_name":"test1","todo_date":"2021-07-30","start_time":"20:08","end_date":"2021-08-01",
                "end_time":"12:00","todo_contents":"contents,contents","todo_completed":True}
    
    cardToReturn["body"][1]["text"]="項目_ID:  "+singletask["todo_id"]
    cardToReturn["body"][3]["value"]=singletask["todo_name"]
    cardToReturn["body"][5]["value"]=singletask["todo_date"]
    cardToReturn["body"][11]["value"]=singletask["todo_contents"]
    cardToReturn["body"][12]["value"]="true" if singletask["todo_completed"] else "false"
    cardToReturn["body"][13]["items"][0]["actions"][0]["data"]["task_id"]=singletask["todo_id"]
    
    return cardToReturn

    
# prepareUpdateCard()