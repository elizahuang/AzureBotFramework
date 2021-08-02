# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext, CardFactory, MessageFactory
from botbuilder.schema import ChannelAccount, HeroCard, CardAction, CardImage, ActionTypes, Attachment, Activity, ActivityTypes
import requests
import json
import copy
from updateCard import *
from viewAllCard import *
from addTodoCard import *
from addOrUpdateResultCard import *


def create_hero_card() -> Attachment:
    herocard = HeroCard(title="推薦以下兩個選項",
    images=[
        CardImage(
            url="https://ct.yimg.com/xd/api/res/1.2/VhPkyLMc5NAyXyGfjLgA5g--/YXBwaWQ9eXR3YXVjdGlvbnNlcnZpY2U7aD01ODU7cT04NTtyb3RhdGU9YXV0bzt3PTcwMA--/https://s.yimg.com/ob/image/82cbd7d4-5802-4b2b-99bd-690512b34730.jpg"
        )],  # https://sec.ch9.ms/ch9/7ff5/e07cfef0-aa3b-40bb-9baa-7c9ef8ff7ff5/buildreactionbotframework_960.jpg
    buttons=[
        CardAction(type=ActionTypes.open_url, title="url1",
                   value="https://www.google.com"),
        CardAction(type=ActionTypes.open_url, title="url2",
                   value="https://www.yahoo.com"),
        ])
    return CardFactory.hero_card(herocard)


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    contextToReturn = None

    async def on_message_activity(self, turn_context: TurnContext):
        # print('activity: ',json.dumps(turn_context.activity, sort_keys=True, indent=4),'\n')
        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")
        print('turn_context.activity:\n',turn_context.activity)
        if turn_context.activity.text != None:
            # print(turn_context.activity.text)
            if turn_context.activity.text.startswith("工號_"):
                # TODO 連接 API
                # see mongo DB connect mongo db
                
                # response
                contextToReturn = '恭喜您，添加成功! \n\n 請輸入 "help"，來查看更多服務\n\n 輸入"查看ToDoList"，查看代辦事項\n\n 輸入"tsmc"，查看網頁的url'
            elif turn_context.activity.text == 'help':
                contextToReturn = '輸入"查看代辦事項"，查看代辦事項\n\n 輸入"tsmc"，查看網頁的url\n\n 輸入"新增代辦事項"，新增代辦事項\n\n'
            elif turn_context.activity.text == '新增代辦事項':
                contextToReturn = MessageFactory.attachment(Attachment(content_type='application/vnd.microsoft.card.adaptive',
                                        content=copy.deepcopy(addToDoListAdapCard)))
            elif turn_context.activity.text == 'todo':
                contextToReturn = requests.get(
                    'https://jsonplaceholder.typicode.com/todos/1').content.decode('utf-8')
            elif turn_context.activity.text == 'my_ehr':
                contextToReturn = 'https://myehr'
            elif turn_context.activity.text == 'card':
                cardAtt = create_hero_card()
                contextToReturn = MessageFactory.attachment(cardAtt)
            elif turn_context.activity.text == 'testMessage':
                contextToReturn = MessageFactory.text(
                        "Welcome to CardBot. "
                        + "This bot will show you different types of Rich Cards. "
                        + "Please type anything to get started."
                    )
            elif turn_context.activity.text == 'adaptive':
                # contextToReturn =MessageFactory.attachment(Attachment(content_type='application/vnd.microsoft.card.adaptive',
                #                           content=adapCard))
                contextToReturn = MessageFactory.attachment(Attachment(
                    content_type='application/vnd.microsoft.card.adaptive', content=prepareUpdateCard()))
            elif turn_context.activity.text == 'viewAllTest':
                contextToReturn = MessageFactory.attachment(Attachment(
                    content_type='application/vnd.microsoft.card.adaptive', content=prepareViewAllCardTest()))
            elif turn_context.activity.text == '查看代辦事項':
                tasksInfo = [{"todo_id": "123123", "todo_name": "test1", "todo_date": "2021-07-30", "start_time": "20:08", "end_date": "2021-08-01",
                "end_time": "12:00", "todo_contents": "contents,contents", "todo_completed": True},
                    {"todo_id": "321321", "todo_name": "test2", "todo_date": "2021-07-30", "start_time": "20:08", "end_date": "2021-08-01",
                "end_time": "12:00", "todo_contents": "contents,contents", "todo_completed": False},
                {"todo_id": "321321", "todo_name": "test2", "todo_date": "2021-07-30", "start_time": "20:08", "end_date": "2021-08-01",
                "end_time": "12:00", "todo_contents": "contents,contents", "todo_completed": False},
                {"todo_id": "321321", "todo_name": "test2", "todo_date": "2021-07-30", "start_time": "20:08", "end_date": "2021-08-01",
                "end_time": "12:00", "todo_contents": "contents,contents", "todo_completed": False},
                {"todo_id": "321321", "todo_name": "test2", "todo_date": "2021-07-30", "start_time": "20:08", "end_date": "2021-08-01",
                "end_time": "12:00", "todo_contents": "contents,contents", "todo_completed": False},
                {"todo_id": "321321", "todo_name": "test2", "todo_date": "2021-07-30", "start_time": "20:08", "end_date": "2021-08-01",
                "end_time": "12:00", "todo_contents": "contents,contents", "todo_completed": False}]
                contextToReturn = MessageFactory.attachment(Attachment(
                    content_type='application/vnd.microsoft.card.adaptive', content=prepareViewAllCard(tasksInfo)))
            else:
                contextToReturn = f"You said '{ turn_context.activity.text }'"
        elif turn_context.activity.value != None:
            if turn_context.activity.value['card_request_type']!=None:
                if turn_context.activity.value['card_request_type'] == 'submit_add': 
                    # TODO 接到正確的API
                    my_data = {'todo_name': turn_context.activity.value['todo_name'], 
                                'todo_date': turn_context.activity.value['start_date'].replace("-","/"),
                                'todo_contents': turn_context.activity.value['todo_contents'],
                                'todo_update_date': turn_context.activity.timestamp.strftime("%Y/%m/%d"),
                                'todo_completed': turn_context.activity.value['todo_completed'],
                                'employee_id': turn_context.activity.channel_data['tenant']['id'],
                                "line_user_id": turn_context.activity.channel_data['tenant']['id'],    #delete
                                "teams_user_id": turn_context.activity.channel_data['tenant']['id']    #delete
                                }

                    # 將資料加入 POST 請求中
                    r = requests.post('https://tsmcbot-404notfound.du.r.appspot.com/api/todo/', data = json.dumps(my_data))
                    if r.status_code == requests.codes.ok:
                        contextToReturn = '你已成功新增 %s 至代辦事項，下一步您可以透過查詢代辦事項來查看您的清單。' % (
                            turn_context.activity.value['todo_name'],)
                    else: 
                        print(r.status_code)
                        print("Error: ", r.content)
                        contextToReturn = '請確認是否已經添加工號，如果問題持續發生，請聯絡系統管理員，謝謝'
                
                elif turn_context.activity.value['card_request_type'] == 'update_task':                
                    data=turn_context.activity.value
                    singletask={"todo_id":data["todo_id"],"todo_name":data["todo_name"],"todo_date":data["todo_date"],"todo_contents":data["todo_contents"],"todo_completed":data["todo_completed"]}
                    contextToReturn=prepareUpdateCard(singletask)
                # elif turn_context.activity.value['card_request_type'] == 'delete_task':
                    # call 德瑋的function
                elif turn_context.activity.value['card_request_type'] == 'submit_update':
                    data=turn_context.activity.value
                    singletask={"todo_id":data["todo_id"],"todo_name":data["todo_name"],"todo_date":data["todo_date"],"todo_contents":data["todo_contents"],"todo_completed":data["todo_completed"]}
                    # call submit出去的API
                    contextToReturn=addOrUpdateResultCard(singletask)# contextToReturn=已新增的card

        await turn_context.send_activity(contextToReturn)
        print()

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("歡迎使用本機器人，請享受你在台積的時光。 \n\n "+
        "初次使用請輸入您的工號，以方便連結 line 及 web 的服務\n\n 輸入格式(舉例):  工號_120734")
