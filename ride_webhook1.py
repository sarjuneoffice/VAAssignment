import json
import os

from flask import Flask, request, jsonify, render_template
import datetime
import os
import dialogflow
from datetime import date
from datetime import datetime
import requests
import json
from flask import request
from flask import make_response
import pandas as pd



app = Flask(__name__)

@app.route('/ride', methods=['POST'])
def ride():
    try :
        dict2 = {'Pickup': {0: 'Loyang Clubhouse',
        1: 'Loyang Clubhouse',
        2: 'Loyang Clubhouse',
        3: 'Loyang Clubhouse',
        4: 'Loyang Clubhouse',
        5: 'Loyang Clubhouse',
        6: 'Loyang Clubhouse',
        7: 'Loyang Clubhouse',
        8: 'Loyang Clubhouse',
        9: 'Loyang Clubhouse',
        10: 'Loyang Clubhouse',
        11: 'Pasir Ris MRT',
        12: 'Pasir Ris MRT',
        13: 'Pasir Ris MRT',
        14: 'Pasir Ris MRT',
        15: 'Pasir Ris MRT',
        16: 'Pasir Ris MRT',
        17: 'Pasir Ris MRT',
        18: 'Pasir Ris MRT',
        19: 'Pasir Ris MRT',
        20: 'Pasir Ris MRT',
        21: 'Pasir Ris MRT',
        22: 'AI Park Tower A',
        23: 'AI Park Tower A',
        24: 'AI Park Tower A',
        25: 'AI Park Tower B',
        26: 'AI Park Tower B',
        27: 'AI Park Tower B',
        28: 'Clementi MRT',
        29: 'Clementi MRT',
        30: 'Clementi MRT'},
        'Dropoff': {0: 'Pasir Ris MRT',
        1: 'Pasir Ris MRT',
        2: 'Pasir Ris MRT',
        3: 'Pasir Ris MRT',
        4: 'Pasir Ris MRT',
        5: 'Pasir Ris MRT',
        6: 'Pasir Ris MRT',
        7: 'Pasir Ris MRT',
        8: 'Pasir Ris MRT',
        9: 'Pasir Ris MRT',
        10: 'Pasir Ris MRT',
        11: 'Loyang Clubhouse',
        12: 'Loyang Clubhouse',
        13: 'Loyang Clubhouse',
        14: 'Loyang Clubhouse',
        15: 'Loyang Clubhouse',
        16: 'Loyang Clubhouse',
        17: 'Loyang Clubhouse',
        18: 'Loyang Clubhouse',
        19: 'Loyang Clubhouse',
        20: 'Loyang Clubhouse',
        21: 'Loyang Clubhouse',
        22: 'Clementi MRT',
        23: 'Clementi MRT',
        24: 'Clementi MRT',
        25: 'Clementi MRT',
        26: 'Clementi MRT',
        27: 'Clementi MRT',
        28: 'AI Park Tower A/B',
        29: 'AI Park Tower A/B',
        30: 'AI Park Tower A/B'},
        'Week': {0: 'Weekday',
        1: 'Weekday',
        2: 'Weekday',
        3: 'Weekday',
        4: 'Weekend',
        5: 'Weekend',
        6: 'Weekend',
        7: 'Weekend',
        8: 'Weekend',
        9: 'Weekend',
        10: 'Weekend',
        11: 'Weekday',
        12: 'Weekday',
        13: 'Weekday',
        14: 'Weekday',
        15: 'Weekend',
        16: 'Weekend',
        17: 'Weekend',
        18: 'Weekend',
        19: 'Weekend',
        20: 'Weekend',
        21: 'Weekend',
        22: 'Weekday',
        23: 'Weekday',
        24: 'Weekday',
        25: 'Weekday',
        26: 'Weekday',
        27: 'Weekday',
        28: 'Weekday',
        29: 'Weekday',
        30: 'Weekday'},
        'Time': {0: '13:00:00',
        1: '15:00:00',
        2: '17:00:00',
        3: '19:00:00',
        4: '13:00:00',
        5: '14:00:00',
        6: '15:00:00',
        7: '16:00:00',
        8: '17:00:00',
        9: '18:00:00',
        10: '19:00:00',
        11: '13:30:00',
        12: '15:30:00',
        13: '17:30:00',
        14: '19:30:00',
        15: '13:30:00',
        16: '14:30:00',
        17: '15:30:00',
        18: '16:30:00',
        19: '17:30:00',
        20: '18:30:00',
        21: '19:30:00',
        22: '17:00:00',
        23: '18:00:00',
        24: '19:00:00',
        25: '17:15:00',
        26: '18:15:00',
        27: '19:15:00',
        28: '8:00:00',
        29: '8:30:00',
        30: '9:00:00'},
        'Charge': {0: 'Free',
        1: 'Free',
        2: 'Free',
        3: 'Free',
        4: 'Free',
        5: 'Free',
        6: 'Free',
        7: 'Free',
        8: 'Free',
        9: 'Free',
        10: 'Free',
        11: 'Free',
        12: 'Free',
        13: 'Free',
        14: 'Free',
        15: 'Free',
        16: 'Free',
        17: 'Free',
        18: 'Free',
        19: 'Free',
        20: 'Free',
        21: 'Free',
        22: '$1.40, payment by EZ-link only.',
        23: '$1.40, payment by EZ-link only.',
        24: '$1.40, payment by EZ-link only.',
        25: '$1.40, payment by EZ-link only.',
        26: '$1.40, payment by EZ-link only.',
        27: '$1.40, payment by EZ-link only.',
        28: '$1.40, payment by EZ-link only.',
        29: '$1.40, payment by EZ-link only.',
        30: '$1.40, payment by EZ-link only.'}}

        data1 = pd.DataFrame(dict2)
        invoke_next_question = True
        data = request.get_json(silent=True)   # get the incoming JSON structure
        
        print("----------------START-------------------")
        print("Request:")

        parameters = data["queryResult"]["parameters"]
        current_answer = data["queryResult"]["queryText"]
        current_question = data["queryResult"]["outputContexts"][0]["parameters"]["current-question"]
        pickup = data["queryResult"]["outputContexts"][0]["parameters"]["pickup"]
        dateinfo = data["queryResult"]["outputContexts"][0]["parameters"]["date-time"]
        inputdate = dateinfo.split("T")[0]
        inputdate = datetime.strptime(inputdate, '%Y-%m-%d').date()
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_time1 = datetime.strptime(current_time, "%H:%M:%S").time()
        w1 = inputdate.weekday()
        print("current_question - ", current_question)
        print ("current_answer - ", current_answer)
        next_question = "sbq" + str(int(current_question[-1:]) + 1 )
        print ("next question - ", next_question)
        print(parameters)
        print(data1)

        #I am not using these parameters anywhere but just an showing here how one can extract all the answers
        # parameter1 = data["queryResult"]["outputContexts"][0]["parameters"]["parameter1"]
        # parameter2 = data["queryResult"]["outputContexts"][0]["parameters"]["parameter2"]
        # # parameter1 = req.get("result").get("contexts")[0].get("parameters").get("parameter1")
        # # parameter2 = req.get("result").get("contexts")[0].get("parameters").get("parameter2")
        # parameter3 = "question3." + current_answer
        # print ("parameters - ", parameter1, parameter2, parameter3)
        if (current_question =="sbq1"):
            reply = {}

            reply["followupEventInput"] = {"name": next_question,
                                        "languageCode": "en-US",
                                        "parameters": {
                                        "user-answer": current_answer,
                                        "user-date": inputdate
                                        }}
        elif(current_question == "sbq2"):
            print("sbq3")
            print(pickup)
            print(inputdate)
            print(type(inputdate))
            print(today)
            print(current_time1)
            print(type(current_time1))
            if (inputdate >= today):
                if (inputdate > today):
                    if (((w1<5) & (current_answer=="AI Park Tower A")) |((w1<5) & (current_answer=="AI Park Tower B")) |((w1<5) & (current_answer=="Clementi MRT"))):
                        data1 = data1[data1["Pickup"] == current_answer]
                        TimeSeries = data1["Time"]
                        TimeSeries = TimeSeries.to_dict()
                        Charge = data1["Charge"].to_list()[0]
                        print(Charge)
                        Dropoff = data1["Dropoff"].to_list()[0]
                    else:
                        if (w1<5):
                            data1 = data1[data1["Pickup"] == current_answer]
                            data1 = data1[data1["Week"] == "Weekday"]
                            TimeSeries = data1["Time"]
                            TimeSeries = TimeSeries.to_dict()
                            Charge = data1["Charge"].to_list()[0]
                            print(Charge)
                            Dropoff = data1["Dropoff"].to_list()[0]
                        else:
                            data1 = data1[data1["Pickup"] == current_answer]
                            data1 = data1[data1["Week"] == "Weekend"]
                            TimeSeries = data1["Time"]
                            TimeSeries = TimeSeries.to_dict()
                            Charge = data1["Charge"].to_list()[0]
                            print(Charge)
                            Dropoff = data1["Dropoff"].to_list()[0]
                else:
                    print("first")
                    def func(v):
                        z = datetime.strptime(v, "%H:%M:%S").time()
                        if current_time1 > z:
                            return 0
                        else:
                            return 1
                    data1["CustomRating"] = data1.apply(lambda x: func(x["Time"]),axis=1)
                    data1 = data1[data1["CustomRating"] == 1]
                    data1 = data1.drop(["CustomRating"], axis=1)
                    print(data1)
                    if (((w1<5) & (current_answer=="AI Park Tower A")) |((w1<5) & (current_answer=="AI Park Tower B")) |((w1<5) & (current_answer=="Clementi MRT"))):
                        data1 = data1[data1["Pickup"] == current_answer]
                        TimeSeries = data1["Time"]
                        TimeSeries = TimeSeries.to_dict()
                        Charge = data1["Charge"].to_list()[0]
                        print(Charge)
                        Dropoff = data1["Dropoff"].to_list()[0]
                    else:
                        if (w1<5):
                            data1 = data1[data1["Pickup"] == current_answer]
                            data1 = data1[data1["Week"] == "Weekday"]
                            TimeSeries = data1["Time"]
                            TimeSeries = TimeSeries.to_dict()
                            Charge = data1["Charge"].to_list()[0]
                            print(Charge)
                            Dropoff = data1["Dropoff"].to_list()[0]
                        else:
                            data1 = data1[data1["Pickup"] == current_answer]
                            data1 = data1[data1["Week"] == "Weekend"]
                            TimeSeries = data1["Time"]
                            TimeSeries = TimeSeries.to_dict()
                            Charge = data1["Charge"].to_list()[0]
                            print(Charge)
                            Dropoff = data1["Dropoff"].to_list()[0]
            
            if len(Dropoff)>0:
                reply = {}
                reply["followupEventInput"] = {"name": next_question,
                                            "languageCode": "en-US",
                                            "parameters": {
                                            "user-answer": current_answer,
                                            "user-date": inputdate,
                                            "charge": Charge,
                                            "drop": Dropoff,
                                            "schedule": TimeSeries
                                            }}
            else:
                next_question = "sbq4"

                reply = {}
                reply["followupEventInput"] = {"name": next_question,
                                            "languageCode": "en-US",
                                            "parameters": {
                                            "user-answer": current_answer,
                                            "user-date": inputdate
                                            }}

            
            
        # elif(current_question == "sbq3"):
        #     print("sbq3")
        #     print(pickup)
        #     print(inputdate)
        #     print(type(inputdate))
        #     print(today)
        #     print(current_time1)
        #     print(type(current_time1))
        #     if (inputdate >= today):
        #         if (inputdate > today):
        #             if (((w1<5) & (current_answer=="AI Park Tower A")) |((w1<5) & (current_answer=="AI Park Tower B")) |((w1<5) & (current_answer=="Clementi MRT"))):
        #                 data1 = data1[data1["Pickup"] == current_answer]
        #                 TimeSeries = data1["Time"]
        #                 TimeSeries = TimeSeries.to_dict()
        #                 Charge = data1["Charge"].to_list()[0]
        #                 Dropoff = data1["Dropoff"].to_list()[0]
        #             else:
        #                 data1 = data1[data1["Pickup"] == current_answer]
        #                 TimeSeries = data1["Time"]
        #                 TimeSeries = TimeSeries.to_dict()
        #                 Charge = data1["Charge"].to_list()[0]
        #                 Dropoff = data1["Dropoff"].to_list()[0]
        #         else:
        #             def func(v):
        #                 z = datetime.strptime(v, "%H:%M:%S").time()
        #                 if current_time1 > z:
        #                     return 0
        #                 else:
        #                     return 1
        #             data1["CustomRating"] = data.apply(lambda x: func(x["Time"]),axis=1)
        #             data1 = data1[data1["CustomRating"] == 1]
        #             data1 = data1.drop(["CustomRating"], axis=1)
        #             if (((w1<5) & (current_answer=="AI Park Tower A")) |((w1<5) & (current_answer=="AI Park Tower B")) |((w1<5) & (current_answer=="Clementi MRT"))):
        #                 data1 = data1[data1["Pickup"] == current_answer]
        #                 TimeSeries = data1["Time"]
        #                 TimeSeries = TimeSeries.to_dict()
        #                 Charge = data1["Charge"].to_list()[0]
        #                 Dropoff = data1["Dropoff"].to_list()[0]
        #             else:
        #                 data1 = data1[data1["Pickup"] == current_answer]
        #                 TimeSeries = data1["Time"]
        #                 TimeSeries = TimeSeries.to_dict()
        #                 Charge = data1["Charge"].to_list()[0]
        #                 Dropoff = data1["Dropoff"].to_list()[0]
            
        #     response = "Your bus schedule from {} to {} for {} is scheduled for {} and is for {}" .format(current_answer, Dropoff, inputdate, TimeSeries, Charge)
            
            
        #     reply = {}
        #     reply["fulfillmentText"] = ""
        #     reply["fulfillmentMessages"] = []
            
            
        #     ### TODO #5: Creates the message object for Telegram 
        #     ### .        

        #     msg_object = {}
        #     msg_object["platform"] = "TELEGRAM"

        #     ### TODO #6: Creates the custom payload with inline_keyboard
        
        #     msg_object["payload"] = {}
        #     msg_object["payload"]["telegram"] = {}
        #     msg_object["payload"]["telegram"]["text"] = response
        #     msg_object["payload"]["telegram"]["reply_markup"] =  {}
        #     msg_object["payload"]["telegram"]["reply_markup"]["inline_keyboard"] =  []
            
        #     ### TODO #7: Creates a keyboard row with two keys and append to the message object
                
        #     tg_keyboard_row = []
        #     tg_keyboard_row.append({"text" : "👍👍'", "callback_data": "acknowledges the queue number"})
        #     tg_keyboard_row.append({"text" : "😊😊", "callback_data": "acknowledges the queue number"})
            
        #     msg_object["payload"]["telegram"]["reply_markup"]["inline_keyboard"].append(tg_keyboard_row)

        #     reply["fulfillmentMessages"].append(msg_object)    

        # elif(current_answer == "Yes"):
        #     print("sbq3")
        #     print(pickup)
        #     print(inputdate)
        #     print(today)
        #     print(current_time)
        #     speech = "Greeting from webhook"
        #     reply = {}
        #     reply["fulfillmentText"] = speech
        
        # elif(current_answer == "No"):
        #     print("sbq3")
        #     print(pickup)
        #     print(inputdate)
        #     print(today)
        #     print(current_time)
        #     speech = "Please try again"
        #     reply = {}
        #     reply["fulfillmentText"] = speech


            
        else:
            print("why here!!!!!")
            speech = "Greeting from webhook"
            reply = {}
            reply["fulfillmentText"] = speech

       


    except:
        speech = "There are no transport services for the requested period"
        reply = {}
        reply["fulfillmentText"] = speech
        

    # res = json.dumps(bot_reply, indent=4)
    # r = make_response(res)
    # r.headers['Content-Type'] = 'application/json'
    print (reply)
    print("###############################")
    return jsonify(reply)


if __name__ == '__main__':
    # port = int(os.getenv('PORT', 5002))

    # print("Starting app on port %d" % port)

    # app.run(debug=True, port=port, host='0.0.0.0')
    app.run()
