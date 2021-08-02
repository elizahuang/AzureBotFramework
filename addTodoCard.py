addToDoListAdapCard={
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "type": "AdaptiveCard",
  "version": "1.0",
  "body": [
    {
      "type": "Container",
      "items": [
        {
          "type": "TextBlock",
          "text": "代辦事項清單服務",
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
                  "url": "https://img.ltn.com.tw/Upload/ent/page/800/2015/11/06/1500206_1.jpg",
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
                  "text": "維尼 (虛擬助手)",
                  "weight": "bolder",
                  "wrap": True
                },
                {
                  "type": "TextBlock",
                  "spacing": "none",
                  "text": "Created {{DATE(2021-08-01T06:08:39Z, SHORT)}}",
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
          "text": "歡迎使用代辦事項服務，點選下列按鈕開始使用相關功能。",
          "wrap": True
        }
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.ShowCard",
      "title": "添加新的代辦事項",
      "card": {
        "type": "AdaptiveCard",
        "body": [
          {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "添加新的代辦事項",
            "horizontalAlignment": "Center",
            "wrap": True
        },
        # {
            # "type": "TextBlock",
            # "text": "Task_ID:  "+"12342151",
            # "wrap": True,
            # "id": "show_task_id",
            # "separator": True,            
        # },
        {
            "type": "TextBlock",
            "text": "代辦事項",
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
            "placeholder": "請輸入代辦事項名稱",
            "spacing": "Padding"
        },
        {
            "type": "TextBlock",
            "text": "代辦事項日期與時間",
            "wrap": True,
            "id": "task_start_label",
            "separator": True,
        },     
        {
            "type": "Input.Date",
            "isRequired": True,
            "errorMessage": "Start date for the task is required",
            "id": "start_date",
            "placeholder": "請輸入代辦事項日期"
        },
        {
            "type": "Input.Time",
            "id": "start_time",
            "placeholder": "請輸入代辦事項時間"
        },
        # {
            # "type": "TextBlock",
            # "text": "Task End Date Time",
            # "wrap": True,
            # "id": "task_end_label",
            # "separator": True,
        # },             
        # {
            # "type": "Input.Date",
            # "isRequired": True,
            # "errorMessage": "End date for the task is required",
            # "id": "end_date",
            # "value": "2021-08-01"
        # },
        # {
            # "type": "Input.Time",
            # "id": "end_time",
            # "value": "16:59"
        # },
        {
            "type": "TextBlock",
            "text": "代辦事項內容",
            "wrap": True,
            "id": "task_content_label",
            "separator": True,
        },             
        {
            "type": "Input.Text",
            "style": "text",
            "isMultiline": True,
            # "placeholder": "請輸入代辦事項內容",
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
                                "card_request_type": "submit_add",
                                # "task_id": "12342151"
                            },
                            "id": "update_task_submit",
                            "associatedInputs": "auto"
                        }
                    ]
                }
            ]
        }
        ],
        # "actions": [
          # {
            # "type": "Action.Submit",
            # "title": "OK",
            # "data": {
            # "card_type": "addToDoList"
          # }
          # }
        # ]
      }
    }
  ]
}

def prepareAddToDoListAdapCard():
    cardReturn=copy.deepcopy(addToDoListAdapCard)
    return cardReturn