import copy
updateCard={
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

    # "actions": [
    #     {
    #         "type": "Action.Submit",
    #         "title": "Submit",
    #         "data": {
    #             "card_type": "submit",
    #             "task_id": "12342151",
    #         },
    #         "id": "update_task_submit",
    #         "associatedInputs": "auto"
    #     }
    # ]
def prepareUpdateCard():
    cardReturn=copy.deepcopy(updateCard)
    return cardReturn

    
# prepareUpdateCard()