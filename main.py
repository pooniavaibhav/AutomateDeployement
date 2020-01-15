import gitfetch as fetch
from docker import Init_Docker_Image as dock
import Maintenance as maintain
import run_kubectl as kube
import logerror
import env
#Take git path

if __name__=="__main__":
    git_status = fetch.fetch()

    if git_status=="Successful":
        #nameofimage=getArgs()
        Docker_status = dock.create_docker_image()
        if Docker_status=="Successful":
            #maintenance_stat = maintain.debug_mode()
            #if Docker_status == "Successful":
                kube.pullImage()
            #else:
                #logerror.log("Error while pulling image.")
        else:
            logerror.log("error while pulling image.")
    else:
        logerror.log("Error in getting fetch.")














