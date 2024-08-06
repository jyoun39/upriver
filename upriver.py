import pandas as pd

from class_define import general_details
from class_define import batch_file_details
from class_define import ssh_connection_details
from class_define import job_submission_details

from start_macro_writer import start_macro_writer
from append_macro_writer import append_macro_writer
from submit_job_script import submit_job_script
from submit_job import submit_job

#Notes:
# - function is to add as many scalars as specified in your batch spreadsheet
# - input: one batch spreadsheet of same format as default (can add as many scalars, but 1st column must be column name), one StarCCM template w/o solution
# - only scalars so if used in a unit needed application, default units are SI units
# - recommended to setup passwordless SSH for user experience

# SCRIPT FUNCTIONS
copy = 0 #0 means template will not be copied, 1 means template will be copied
run = 0 #0 means job will not run (template will still be updated), 1 means template will be updated AND job submitted

# MUST SPECIFY --> general details
batch_file_path = "C:\\Users\\GA10028979\\Downloads\\upriver\\parameter.csv"
directory_path_local = "C:\\Users\\GA10028979\\Downloads\\upriver\\"
directory_path_cluster = "/storage/coda1/p-sm53/0/jyoun39/project/"

template = "onera-m6-sharp_airfoil" #don't add .sim afterwards

# # MUST SPECIFY --> ssh connection details
hostname = "login-phoenix.pace.gatech.edu",
port = 22,
username = "jyoun39",
password = "96385207410yJ____"

# # MUST SPECIFY --> Job submission details
account = "gts-cperron7"
nodes = "2"
taskspernode = "24"
mempercpu = "7500M"
time = "0:15:00"
qos = "embers"
email = "jyoun39@gatech.edu"

#specify instance of objects
general = general_details(batch_file_path, directory_path_local, directory_path_cluster, run, copy, template) 
general.process_file()

ssh = ssh_connection_details(hostname, port, username, password)
job = job_submission_details(account, nodes, taskspernode, mempercpu, time, qos, email)

for row_index in range(general.num_rows):
    start_macro_writer(row_index, general)
    for column_index in range(general.num_columns):
        end = 0
        if column_index == (general.num_columns-1):
            end = 1
        append_macro_writer(row_index,column_index,general,end)

#Submit job per case
print("\n")
for row_index in range(general.num_rows):
    submit_job_script(row_index, general, job) #creates job submission script
    submit_job(row_index, general, ssh) #creates case directories, copies files, and submits job







