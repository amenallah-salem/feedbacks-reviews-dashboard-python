from flask import Flask, Response, stream_with_context
import time 
import uuid
import random 
from datetime import datetime



APP = Flask(__name__)#intialize APP as a flask appilication 
@APP.route("/data/<int:rowcount>", methods =["GET"])

def get_data(rowcount):
    "func to return n row of data for pd"
    def generate_random_data():
        for i in range(rowcount):
            #time.sleep(.01) #this may be enabeled in production
            #now = datetime.now()
            #current_time = now.strftime("%d/%m/%Y %H:%M:%S")#30/05/2021 13:38:48
            unix_current_time = time.time()
            User_ID=uuid.uuid4()#ransom id for each user 
            context=random.randint(0,10)

            env = random.choice(["web", "App"])
            Context_amount={context: 0.0 if context not in [7,8,9] else round(random.uniform(0,1000),2)} #context amout is :  [(0.0$, 660.54$)]
            #insure that the context we get is coherent with the amout spent with the user
            Envirement_Os=["Windows", "Mac OS", "Other"] if env =="web" else ["Android", "Other", "Ios"]
            yield f"({unix_current_time},{User_ID},{env},{random.choice(Envirement_Os)},{context},{Context_amount[context]})\n"
    
    return Response(stream_with_context(generate_random_data()))


if __name__=="__main__":
    APP.run(debug=True)