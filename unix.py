# #Running unix commands with python script
#Code is required to stop a service in Linux
#Wait for two minutes 
#Check the status of the service:
        #If running -> end program and ask for human intervention
        #If not running move onto the next service
#CONCERN: program needs
import subprocess

def stop_service(service):
    subprocess.call(["service", service, "stop"])

    try:
        output = subprocess.check_output(["service", "apache2", "status"])
    except subprocess.CalledProcessError as e:
        output = e.output
        output = output.decode('utf-8')
        output = output.split()
    else:
        output = output.decode('utf-8')
        output = output.split()

    if "(running)" in output:
        print("service is running")
    elif "(dead)" in output:
        print("service is not running")

stop_service("apache2")
