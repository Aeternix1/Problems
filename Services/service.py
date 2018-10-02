#Contains functions to stop,start and check service status

import subprocess
import time

def check_service_status(service):
    """Given a service name will check the status"""
    """Of the service and prints whether service is"""
    """Active or inactive"""
    try:
        output = subprocess.check_output(["service", service, "status"])
    except subprocess.CalledProcessError as e:
        output = e.output
        output = output.decode('utf-8')
        output = output.split()
    else:
        output = output.decode('utf-8')
        output = output.split()
   
    #Possible issue with service status
    if "(running)" in output:
        print("service is active")
        status = "active"
    elif "(dead)" in output:
        print("service is inactive")
        status = "inactive"
    return status

def start_service(service):
    """Given a service name will start the service"""
    subprocess.call(["service", service, "start"])

def stop_service(service):
    """Given a service name will stop the service"""
    subprocess.call(["service", service, "stop"])

def set_delay(seconds):
    """Given a number of seconds will set a delay"""
    """Between commands"""
    time.sleep(seconds)
    
