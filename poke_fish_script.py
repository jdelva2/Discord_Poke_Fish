# Pokemon Fishing Automation   

import requests
import json
import schedule
from schedule import every, repeat, run_pending
import time


#Global variables to edit
#Found using the web browser developer tool.
request_url  = ""
header = { 'Authorization' : ''
    }


# Sends POST message to channel to cast reel
def cast_reel():
    cast = {'content' : "+c"}
    r = requests.post(request_url, data = cast, headers = header)

    
#Sends POST message to channel to reel in catch
def reel_in():
    reel = {'content': "+r"}
    s = requests.post(request_url, data = reel, headers = header)
    
    
# Retrieves GET message from parabot to reel in catch or wait. repeat every 2 minutes
def get_message():
    L = []
    loot_message = "@Pepe Parker! Something's caught on the hook!"
    poke_message = "Oh! @Pepe Parker! A bite!"
    no_nibble_message = "@Pepe Parker, try a different route. There's not even a nibble.."
    BIG_FISH = "@Pepe Parker, something massive is on the line! It's putting up a fight.. Get ready to reel!"
    #BIG_FISH_2 = ""
    
    req = requests.get(request_url, headers = header)
    jsonn = json.loads(req.text)
    
    
    for m_dict in jsonn:
        L.append(m_dict['content'])
    # Appends first n-1 messages in the list.  
    L = L[:101]

    for message in L:
        if message == loot_message:
            reel_in()
            
        elif message == poke_message:
            reel_in()
            
        elif message == no_nibble_message:
            cast_reel()
            
        elif message == BIG_FISH:
            #DO SOME CODE HERE
            pass
        else:
            pass
       
    
def schedule_message():
    cast_reel()
    schedule.every(30).minutes.do(cast_reel)
    schedule.every(4).minutes.do(get_message) # change this to 4 minutes on average
    
    while True:
        schedule.run_pending()
        time.sleep(10) 

schedule_message()
    
