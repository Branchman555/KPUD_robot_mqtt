import paho.mqtt.client as paho
import json

"""
------------------------------------------
[서버 >>>>=========>>>> 로봇] 메시지 구조
------------------------------------------
{
  "header": "ORDER",
  "contents": {
    "node": [
      [37.1274,127.5693],
      [37.1274,127.5693],
      [37.1274,127.5693],
      [37.1274,127.5693],
      [37.1274,127.5693],
      [37.1274,127.5693]
    ],
    "command": "order"
  },
  "memo": "order msg"
}

header :
{
    ORDER
    RETURN
    UNLOCK
}
"""
"""
------------------------------------------
[로봇 >>>>=========>>>> 서버] 메시지 구조
------------------------------------------
{
  "robot": 1,
  "contents": {
    "progress": 50,
    "state": "M"
  },
  "memo": "robot msg"
}

state : 
{
    M(Moving)
    W(Waiting)
    A(Arrival)
    R(Returning)
}
"""
broker="49.50.165.20"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")

def on_message(client,userdata,msg):             #create function for callback
    if msg.topic == 'ggg':
        #topic이 ggg일때
        robot_dict = json.loads(str(msg.payload))
        robot = robot_dict['robot']
        if robot == 1:
            pass
        elif robot == 2:
            pass

        state = robot_dict['state']
        if state == 'M':
            progress = robot_dict['progress']


        robot = robot_dict['memo']

    if msg.topic == 'hhh':
        # topic이 hhh일때
        robot_dict = json.loads(str(msg.payload))
        robot = robot_dict['robot']
        robot = robot_dict['contents']
        robot = robot_dict['memo']

    print("You've got message")
    print(" : " + str(msg.payload))

client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.on_message = on_message
client1.connect(broker,port)                                 #establish connection
client1.loop_start()
client1.subscribe("ggg", 0)

while True:
    chat = str(input())
    if chat is "QUIT":
        break
    ret = client1.publish("hhh", chat)
client1.loop_stop()
client1.disconnect()