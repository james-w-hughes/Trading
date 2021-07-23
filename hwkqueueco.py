import ssl
import websocket

import numpy as np
import pandas as pd

import ijson
import json

bidprice = 0
bidquantity = 0
askprice = 0
askquantity = 0
results = dict.fromkeys(['bidprice','bidquantity','askprice','askquantity']) 


def on_message(ws, message):
    
    #First sort out the data so it can be managed for this task:
    y = json.loads(message)
    z = y["events"]
    x = str(z)[1:-1]
    w = x.replace('\'', '\"')
    k = json.loads(w)
    
    #Use an if loop to update the ask or bid prices accordingly:
    if (k["side"] == "ask"):
        results['askprice'] = k["price"]
        results['askquantity'] = k["remaining"]
        print(results['bidprice'],results['bidquantity'],"-",results['askprice'],results['askquantity'])
    
    else:
        results['bidprice'] = k["price"]
        results['bidquantity'] = k["remaining"]
        print(results['bidprice'],results['bidquantity'],"-",results['askprice'],results['askquantity'])
        

        #print(message)


ws = websocket.WebSocketApp(
    "wss://api.gemini.com/v1/marketdata/btcusd?bids=true&offers=true&top_of_book=false",
    on_message=on_message)
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

