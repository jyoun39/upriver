# my_classes.py

# my_classes.py
import pandas as pd

class batch_file_details:
    def __init__(self, batch_file_path):
        self.batch_file_path = batch_file_path
        self.batch_data = None
        self.headers = []
        self.parameters = []
        self.batch_parameter_data = None
        self.num_rows = 0
        self.num_columns = 0
        self.case_name = None

    def read_batch_file(self):
        try:
            # Read the CSV file
            self.batch_data = pd.read_csv(self.batch_file_path)
            
            # Select columns from the second to the end
            self.headers = self.batch_data.columns.tolist()
            self.parameters = self.headers[1:]

            self.batch_parameter_data = self.batch_data.iloc[:, 1:]
            self.num_rows, self.num_columns = self.batch_parameter_data.shape

            target_header = 'case_name'
            if target_header in self.batch_data.columns:
                self.case_name = self.batch_data[target_header]
            else:
                print(f"Column '{target_header}' not found in the batch file.")
            
        except FileNotFoundError:
            print(f"Batch file '{self.batch_file_path}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the batch file: {e}")


# my_classes.py (continued)

class general_details(batch_file_details):
    def __init__(self, batch_file_path, directory_path_local, directory_path_cluster, run, copy, template):
        super().__init__(batch_file_path)  # Call the parent class constructor
        self.directory_path_local = directory_path_local
        self.directory_path_cluster = directory_path_cluster
        self.run = run
        self.copy = copy
        self.template = template

    def process_file(self):
        # Call read_batch_file from the base class to populate its attributes
        self.read_batch_file()

class ssh_connection_details:
    def __init__(self, hostname, port, username, password):
        # SSH Connection Details
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

class job_submission_details:
    def __init__(self, account, nodes, taskspernode, mempercpu, time, qos, email):
        # Job Submission Details
        self.account = account
        self.nodes = nodes
        self.taskspernode = taskspernode
        self.mempercpu = mempercpu
        self.time = time
        self.qos = qos
        self.email = email
