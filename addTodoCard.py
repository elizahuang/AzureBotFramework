addCard=addToDoListAdapCard={
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
            "type": "Input.Text",
            "id": "toDoName",
            "isMultiline": True,
            "placeholder": "請輸入代辦事項名稱"
          },
          {
            "type": "Input.Text",
            "id": "toDoContent",
            "isMultiline": True,
            "placeholder": "請輸入代辦事項內容"
          },
          {
            "type": "Input.Date",
            "id": "toDoDate",
            "placeholder": "請輸入代辦事項日期"
          },
          {
            "type": "Input.Time",
            "id": "toDoTime",
            "placeholder": "請輸入代辦事項時間"
          },
          {
            "type": "Input.Text",
            "id": "toDoComplete",
            "placeholder": "請輸入代辦事項完成狀態 True/False"
          },
        ],
        "actions": [
          {
            "type": "Action.Submit",
            "title": "OK",
            "data": {
            "card_type": "addToDoList"
          }
          }
        ]
      }
    }
  ]
}