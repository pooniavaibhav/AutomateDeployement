import env

def log(error_msg):
    """
    This function writes logs in log file when ever called.
    :param error_msg:
    :return : Written successfully
    """
    dir = env.workdir("logs_dir")
    with open(dir,"a") as file:
        file.write(error_msg)
    return ("Written Successfully")



