import requests
import pandas as pd

#################################
#  Table format:
#  |customerName | customerEmail | inputfile |

#
#################################





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

    print("Processing request for "+request['customerName']+'.')
    return(True)






def send_message(customer_name,customer_email):
    return requests.post(
    "https://api.mailgun.net/v3/sandbox8a8eabd810b540f5a7eca93aecbec851.mailgun.org/messages",
    auth=("api","key-22e20caa980e3fd1835b1105d6ea5e29"),
    data={"from": "Brain Printing Service <mailgun@sandbox8a8eabd810b540f5a7eca93aecbec851.mailgun.org>",
            "to": [customer_email],
            "subject": "Your Brain Is On Its Way",
            "text": "Congratulations!!! You are one step way from your printed brain. Just bring the attached .stl file to the printer."}
    )



if __name__ == "__main__":

    # from crontab import CronTab
    # cron = CronTab(tabfile='/etc/crontab')
    # job  = cron.new(command='/usr/bin/echo')
    # job.minute.during(5,50).every(5)

    import threading
    import time

    #TODO use requests table
    table_name = "database.csv"

    def ping_table():

        #TODO avoid reading whole table
        df = pd.read_csv(table_name)

        # apply approach
        # new_requests = df.loc[df["status"] == 'upload_finished']
        # if len(new_requests)>0:
        #    new_requests.apply(process_request, axis=1)

        # loop approach
        recordsToProcess = df.index[df["status"] == 'upload_finished']

        for id in recordsToProcess:

            df.loc[id]['status'] = 'process_started'
            df.to_csv(table_name,index=False) # Note:overwriting!!!
            res = process_request(df.loc[id])
            time.sleep(1)
            if res:
                df.loc[id]['status'] = 'process_ended'
                df.to_csv(table_name,index=False) # Note: overwriting!!!
        #TODO: modify csv in place!!!!!

        recordsToSendEmail = df.index[df["status"] == 'process_ended']
        for id in recordsToSendEmail:
            df.loc[id]['status'] = 'email_started'
            df.to_csv(table_name,index=False)
            r = send_message(df.loc[id]['customerName'],df.loc[id]['customerEmail'])
            if r.status_code == 200:
                df.loc[id]['status'] = 'email_sent'
                df.to_csv(table_name,index=False)



        # numline = len(file.readlines())
        # file.close()
        # rint(numline)
        ## assuming only one new record!!!
        # if numline == old_numline:
        #    row = pd.read_csv(table_name,index_col=numline)
        #    process_request(row)
        #    old_numline = numline
    while True:
        ping_table()
        time.sleep(5)
        #threading.Timer(5, ping_table).start()
