'''
This file is for creating the log files dynamically at the time of run.
'''

import logging
import time
import datetime
def set_log(log_name):
    #Setting date and time with log file name
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H%M%S')
    log=logging.getLogger(log_name)#"common_functions"
    log.setLevel(logging.DEBUG)
    #Creating log filename dynamically with date and time
    fh = logging.FileHandler("CallHub-"+st.split()[0]+".log")
    formatter = logging.Formatter('%(asctime)s - [%(name)s - %(lineno)d - %(funcName)s()] - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    return log 