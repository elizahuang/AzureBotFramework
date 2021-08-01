import copy

viewAllCard={
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": " All Tasks",
            "wrap": True,
            "horizontalAlignment": "Center"
        },

    ]
}

singleTask= [{
            "type": "FactSet",
            "facts": [
                {
                    "title": "Task ID",
                    "value": "12342151"
                },
                {
                    "title": "Task Title",
                    "value": "making cards"
                },
                {
                    "title": "Start Date",
                    "value": "2021-07-31"
                },
                {
                    "title": "Start Time",
                    "value": "21:00"
                },                
                {
                    "title": "End Date",
                    "value": "2021-08-01"
                },
                {
                    "title": "End Time",
                    "value": "21:00"
                },                                
                {
                    "title": "Completed",
                    "value": "False"
                }
            ],
            "separator": True
        },
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
                                    "type": "Action.Submit",
                                    "title": "Update Task",
                                    "data": {
                                        "card_request_type": "update_task",
                                        "task_id": "12342151"
                                    }
                                }
                            ]
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
                                    "type": "Action.Submit",
                                    "title": "Delete Task",
                                    "data": {
                                        "card_request_type": "delete_task",
                                        "task_id": "12342151"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }]

def prepareViewAllCardTest():
    cardReturn=copy.deepcopy(viewAllCard)
    task=copy.deepcopy(singleTask)
    cardReturn["body"]=cardReturn["body"]+task+task
    return cardReturn

# [{"todo_id":"123123","todo_name":"test1","start_date":"2021-07-30","start_time":"20:08","end_date":"2021-08-01",\
#               "end_time":"12:00","todo_contents":"contents,contents","todo_completed":True},\
#  {"todo_id":"321321","todo_name":"test2","start_date":"2021-07-30","start_time":"20:08","end_date":"2021-08-01",\
#               "end_time":"12:00","todo_contents":"contents,contents","todo_completed":False}]
def prepareViewAllCard(taskInfos):
    cardReturn=copy.deepcopy(viewAllCard)
    for task in taskInfos:    
        task_template=copy.deepcopy(singleTask)
        task_template[0]["facts"][0]["value"]=task["todo_id"]
        task_template[0]["facts"][1]["value"]=task["todo_name"]
        task_template[0]["facts"][2]["value"]=task["start_date"]
        task_template[0]["facts"][3]["value"]=task["start_time"]      
        task_template[0]["facts"][4]["value"]=task["end_date"] 
        task_template[0]["facts"][5]["value"]=task["end_time"]
        task_template[0]["facts"][6]["value"]=task["todo_completed"]                             
        
        task_template[1]["columns"][0]["items"][0]["actions"][0]["data"].update(task)
        task_template[1]["columns"][1]["items"][0]["actions"][0]["data"].update(task)
        
        cardReturn["body"]=cardReturn["body"]+task_template
        
        
    return cardReturn

