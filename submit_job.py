import paramiko

def submit_job(row_index, general, batch, ssh):
    import subprocess

    # Define the PowerShell command
    ps_command = f"scp -r {general.directory_path_local}{batch.column_data['case_name'][row_index]} {ssh.username}@{ssh.hostname}:{general.directory_path_cluster}"

    if general.copy == True:
        ps_command += f"\nscp {general.directory_path_local}{general.template}.sim {ssh.username}@{ssh.hostname}:{general.directory_path_cluster}"
        print(f"Copying {general.template}.sim file to cluster at {general.directory_path_cluster}")
    
    ps_command = ps_command + "\nscp "+general.directory_path_local+"run.java "+ssh.username+"@"+ssh.hostname+":"+general.directory_path_cluster+batch.column_data['case_name'][row_index]

    print(f"Copying {batch.column_data['case_name'][row_index]} folder to cluster at {general.directory_path_cluster}")
    if general.copy == True:
        print(f"Copying {general.template}.sim file to cluster at {general.directory_path_cluster}")

    #Execute the PowerShell command
    #result = subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
    
    ssh_command = [
        f'ln -s {general.directory_path_cluster}{general.template}.sim {general.directory_path_cluster}{batch.column_data["case_name"][row_index]}',
        f'cd {general.directory_path_cluster}{batch.column_data["case_name"][row_index]}',
        f'dos2unix submit_{batch.column_data["case_name"][row_index]}.sbatch',
        f'sbatch submit_{batch.column_data["case_name"][row_index]}.sbatch'
    ]

    # try:
    #     # Create an SSH client
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
    #     # Connect to the remote host
    #     ssh.connect(hostname=ssh.hostname, port=ssh.port, username=ssh.username, password=ssh.password)
        
    #     # Combine ssh_command into a single string separated by semicolons
    #     command_string = ' && '.join(ssh_command)
        
    #     # Execute the combined command string
    #     stdin, stdout, stderr = ssh.exec_command(command_string)
    #     output = stdout.read().decode()
    #     errors = stderr.read().decode()
        
    #     # Close the connection
    #     ssh.close()
    # except Exception as e:
    #     print(f"An error occurred: {e}")