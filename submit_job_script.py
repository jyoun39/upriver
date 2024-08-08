#def submit_job_script(case_name, template_name, account, nodes, taskspernode, mempercpu, time, qos, email):

def submit_job_script(row_index, general, batch, job):
    import textwrap
    script_content = '''#!/bin/bash
# ----------------SBATCH Parameters----------------- #
#SBATCH --job-name='''+batch.column_data['case_name'][row_index]+'''
#SBATCH --account='''+job.account+'''
#SBATCH --nodes='''+job.nodes+'''
#SBATCH --ntasks-per-node='''+job.taskspernode+'''
#SBATCH --mem-per-cpu='''+job.mempercpu+'''
#SBATCH --time='''+job.time+'''
#SBATCH --qos='''+job.qos+'''
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user='''+job.email+'''

# First, go to submit directory
cd ${SLURM_SUBMIT_DIR}

# ----------------Print Some Info------------------- #
echo Running on host `hostname`
echo Using the following nodes:
echo ${SLURM_JOB_NODELIST}
# Compute the number of processors
echo This job has allocated ${SLURM_NTASKS} cores

# -----------------Load Modules--------------------- #
ASDL_BIN="/storage/coda1/p-cperron7/0/cperron7/bin"
source $ASDL_BIN/starccm+/18.02.008-R8/activate

# -------------Environment Variables---------------- #
MACROFILE="'''+batch.column_data['case_name'][row_index]+'''.java run.java"
SIMFILE="'''+general.template+'''.sim"

# -------------Generate Machine File---------------- #
MACHINEFILE="${TMPDIR}/machinefile.${SLURM_JOB_ID}"
# Generate Machinefile for mpi in the same order as if run via srun
srun -l /bin/hostname | sort -n | awk '{print $2}' > ${MACHINEFILE}
echo Machine file written to ${MACHINEFILE}
# Count number of ranks from machine file
SLURM_NTASKS=$(wc -l < ${MACHINEFILE})

# ----------------Execute Script-------------------- #
starccm+ -licpath 27100@ugslic2.ecs.gatech.edu -machinefile ${MACHINEFILE} -np ${SLURM_NTASKS} -batch $MACROFILE $SIMFILE > starccm_${SLURM_JOB_ID}.log'''
    
    import os

    # Create the directory
    file_content_path = general.directory_path_local + batch.column_data['case_name'][row_index] + "\\submit_" + batch.column_data['case_name'][row_index] + ".sbatch"
    with open(file_content_path, 'w') as file:
        # Convert Windows-style line endings to UNIX-style
        unix_script_content = script_content.replace('\r\n', '\n')
        file.write(unix_script_content)

    print("submit_" + batch.column_data['case_name'][row_index] + ".sbatch added to " + file_content_path)


