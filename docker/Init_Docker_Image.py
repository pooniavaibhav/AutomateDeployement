import subprocess
import csv
import re
import datetime
import env
import os
import logerror


def create_docker_image():
    #This function creates a docker image in local with changed version and return successful on success.
    #Fetching Commands
    version = get_version()
    tag_name = "beamV" + version
    cmd = env.workdir("docker_cmd")
    docker_command = (cmd+tag_name)
    push_command = env.workdir("push_cmd")
    push_cmd = push_command + tag_name
    log_path = env.workdir("logs_dir")
    file = open(log_path , "a")
    wdir = env.workdir("current_Dir")
    path = wdir + "/docker"


    os.chdir(path)
    docker_string = "DOCKER COMMAND = " + docker_command + "\n"
    file.write(docker_string)
    subprocess.call(docker_command,shell=True,stdout = file)
    date_str = "DATE-TIME:" + str((datetime.datetime.now()))
    logerror.log("\n")
    logerror.log((date_str + "\n"))
    stat = get_status()

    if stat == "Successfully":
        subprocess.call(push_cmd, shell=True, stderr = file)
        logerror.log("\nBefore return\n")
        return "Successful"
    else:
        logerror.log("ERROR")


def get_status():
    #It reads the logs and confirm if image was tagged successfully.
    with open("/home/datanext/PythonProjects/AutomateDeployement/files/logs.txt", "r") as file2:
        readline = file2.readlines()
        leng = len(readline)
        Suc_len=(leng-4)
        if Suc_len > 2:
            split = (readline[Suc_len])
            stat = split[:12]
            return stat

def get_version():
    #It is for version control.With every time this function is called it returns a value adding 0.1 in it.
    with open("/home/datanext/PythonProjects/AutomateDeployement/files/config.txt", "r") as f:
        reader = csv.reader(f, delimiter='\n')
        for line in reader:
            for i in line:
                x = re.findall("\d+\.\d+", i)
                for i in x:
                    a = float(i)
                    new_val = (a + 0.1)
                    new_val_round = round(new_val, 2)
                    str_new_val = str(new_val_round)
                new = ("version=" + str_new_val)
                with open("/home/datanext/PythonProjects/AutomateDeployement/files/config.txt", "w+") as g:
                    g.write(new)
    return str_new_val


