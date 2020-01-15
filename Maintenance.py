import os

def debug_mode():
    """
    After getting fetch we need to change the back slash to forward slash to run it in linux machine.
    """
    pom = open(workingdir + '/DataFlowService/pom.xml', 'r')
    pomxml = pom.read().replace(r"${project.basedir}\src\lib\cassandra-jdbc-driver-0.6.2-shaded.jar</systemPath>",
                                "${project.basedir}/src/lib/cassandra-jdbc-driver-0.6.2-shaded.jar</systemPath>")
    print(pomxml, file=open(workingdir + '/DataFlowService/pom.xml', 'w'))
    os.system("clear")
    return "Successful"
