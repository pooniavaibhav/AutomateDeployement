import subprocess
import datetime
import os
import env
import logerror

def fetch():
    try:
        """
        It fetches latest code from git repository.
        """
        wdir = env.workdir("current_Dir")
        git_dir = "/home/datanext/Documents/gitfetch"
        os.chdir(git_dir)
        cmd = "git fetch http://Vaibhav.Poonia@192.168.0.4/datanext/ai.git"
        cmd2 = "git checkout datanext"
        x = subprocess.run(cmd, shell=True)
        subprocess.run(cmd2, shell=True)
        code = x.returncode
        print(code)
        os.chdir(wdir)
    except OSError as e:
        logerror.log("Error while IO operation while taking fetch")
    finally:
        """
        If fetch was successful.It will return Successful else nothing. and write logs in log file"" 
        """
        log = env.workdir("logs_dir")
        with open(log,"w+") as file:
            if code == 0:
                msg = "[SUCCESS] " + str(datetime.datetime.now()) + " :fetch has been taken successfully\n"
                file.write(msg)
                return "Successful"
            else:
                    error = "[ERROR] " + str(datetime.datetime.now()) + " :Error while fetching file"
                    file.write(error)