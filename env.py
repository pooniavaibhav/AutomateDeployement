import os

def workdir(file):
    if (file == "current_Dir"):
        workdir = os.getcwd()
        return workdir

    if (file) == "logs_dir":
        error_dir = "/home/datanext/PythonProjects/AutomateDeployement/files/logs.txt"
        return error_dir

    if (file) == "docker_cmd":
        docker_comm = "sudo docker build . -t " + "192.168.0.169:30500/datanext:"
        return docker_comm

    if (file) == "push_cmd":
        push_comm = "sudo docker push 192.168.0.169:30500/datanext:"
        return push_comm


