import requests
import pandas as pd
from pymongo import MongoClient
from bson.objectid import ObjectId
import subprocess
import os

#################################
#  Table format:
#  |customerName | customerEmail | inputfile |

#
#################################


def db_connect():
    client = MongoClient('localhost', 27017)
    db = client.test
    return(db.requests)

def read_table(table_filename):
    try:
        df = pd.read_csv(table_filename)
    except FileNotFoundError:
            print("Could not find table.")

def process_request(request):
    """ This requests a row from the table.
        Usage:
            process_request(df[row_number])


    """

    print("Processing request for "+request['customerEmail']+'.')
    #TODO calling of real bash script goes here
    p = subprocess.call(['/bin/sh',os.path.join(os.getcwd(),'sleeper.sh')],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    return(True)






def send_message(customer_email):
    return requests.post(
    "https://api.mailgun.net/v3/sandbox8a8eabd810b540f5a7eca93aecbec851.mailgun.org/messages",
    auth=("api","key-22e20caa980e3fd1835b1105d6ea5e29"),
    # comment out .stl version for now: send only gif
    # files=[("attachment", open("rh_decim.stl.stl","rb")),("inline",open("rh.gif","rb"))],
    files=[("inline",open("rh.gif","rb"))],
    data={"from": "Brain Printing Service <mailgun@sandbox8a8eabd810b540f5a7eca93aecbec851.mailgun.org>",
            "to": [customer_email],
            "subject": "Your Brain Is On Its Way",
            "text": "Congratulations!!! You are one step way from your printed brain. Just bring the attached .stl file to the printer."}
    #headers={'Content-type': 'multipart/form-data'}
    )

def ping_table(table):

    #TODO avoid reading whole table
    df = pd.DataFrame(list(table.find()))
    df.set_index(['_id'],inplace = True)

    # process upload_finished
    recordsToProcess = df[df["status"] == 'upload_finished'].index.tolist()

    for id in recordsToProcess:

        table.update_one({'_id':ObjectId(id)},{'$set':{'status':'process_started'}})
        print(df.loc[ObjectId(id)])
        res = process_request(df.loc[ObjectId(id)])
        time.sleep(1)
        if res:
            table.update_one({'_id':ObjectId(id)},{'$set':{'status':'process_ended'}})


    # process process_ended
    recordsToSendEmail = df[df["status"] == 'process_ended'].index.tolist()

    for id in recordsToSendEmail:
        print(df.loc[ObjectId(id)]['customerEmail'])
        table.update_one({'_id':ObjectId(id)},{'$set':{'status':'email_started'}})
        r = send_message(df.loc[ObjectId(id)]['customerEmail'])
        if r.status_code == 200:
            table.update_one({'_id':ObjectId(id)},{'$set':{'status':'email_sent'}})


if __name__ == "__main__":

    # import threading
    import time

    requests_table = db_connect()

    while True:
        ping_table(requests_table)
        time.sleep(5)
        #threading.Timer(5, ping_table).start()
