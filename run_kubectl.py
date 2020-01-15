import subprocess
import env
import os

def pullImage():
    """
    It will create an instance from beam.yml file and pull image from local registry running
    :return:
    """
    x = "/home/datanext/PythonProjects/AutomateDeployement/Rancher"
    cmd1 = "./rancher kubectl apply -f " + x + "/beam.yml"
    #print(cmd2)
    with open("/home/datanext/PythonProjects/AutomateDeployement/files/logs.txt", "a") as f:
        os.chdir(x)
        subprocess.call(cmd1,shell=True, stdout=f)
