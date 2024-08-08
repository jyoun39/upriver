# my_classes.py

# my_classes.py
import pandas as pd

class batch_file_details:
    def __init__(self, batch_file_path):
        self.batch_file_path = batch_file_path
        self.batch_data = None
        self.headers = []
        self.num_rows = 0
        self.num_columns = 0
        self.column_data = {}  # Initialize an empty dictionary to store column data
    
    def read_batch_file(self):
        try:
            # Read the CSV file
            self.batch_data = pd.read_csv(self.batch_file_path)
            
            # Get column headers
            self.headers = self.batch_data.columns.tolist()
            self.num_rows, self.num_columns = self.batch_data.shape

            # Process the data by columns
            for column_index in range(self.num_columns):
                column_name = self.headers[column_index]
                self.column_data[column_name] = self.batch_data.iloc[:, column_index].tolist()
        
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

    # def SetRefLenth(self, __key:str, L:float):
    #     self.store[__key] = {"type":RefType.length,"L":L}

    # def SetRefArea(self, __key:str, A:float):
    #     self.store[__key] = {"type":RefType.area,"A":A}

    # def SetRefAngle(self, __key:str, theta:float):
    #     self.store[__key] = {"type":RefType.angle,"theta":theta}

    # def SetRefPositionVec(self, __key:str, pVec:list[float]):
    #     self.store[__key] = {"type":RefType.positionvec,"pVec":pVec}

    # def SetRefDensity(self, __key:str, rho:float):
    #     self.store[__key] = {"type":RefType.density,"rho":rho}

    # def SetRefVelocity(self, __key:str, v:float):
    #     self.store[__key] = {"type":RefType.velocity,"v":v}
    
    # def SetRefTemperature(self, __key:str, T:float):
    #     self.store[__key] = {"type":RefType.temperature,"T":T}

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
