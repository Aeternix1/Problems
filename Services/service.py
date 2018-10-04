#Contains functions to stop,start and check service status

import subprocess
import time

def check_service_status(service):
    """Given a service name will check the status and return it"""
    """Either active or inactive"""
    try:
        output = subprocess.check_output(["service", service, "status"])
    except subprocess.CalledProcessError as e:
        output = e.output
        output = output.decode('utf-8')
        output = output.split()
    else:
        output = output.decode('utf-8')
        output = output.split()

    status = "default"
    if "(running)" in output:
        status = "active"
    elif "(dead)" in output:
        status = "inactive"
    return status

def start_service(service):
    """Given a service name will start the service"""
    subprocess.call(["service", service, "start"])

def stop_service(service):
    """Given a service name will stop the service"""
    subprocess.call(["service", service, "stop"])

def delay_action(seconds):
    """Given a number of seconds will set a delay"""
    """Between commands"""
    time.sleep(seconds)

def start_or_stop_services(services, start_or_stop, delay):
    """Program will perform start or stop operation on all services in list"""
    """Program will perform operation, wait for user specified delay and print
    the status of the service"""
    """If the status of the service doesn't match the requested operation then
    inform the user that something has gone wrong and exit the program"""

    if (start_or_stop.lower() == "start"):
        for service in services:
            print("starting service " + service)
            start_service(service)
            delay_action(delay)
            status = check_service_status(service)
            if (status == "active"):
                print(service.title() + "started successfully")
            elif (status == "inactive"):
                print(service.title() + "was not started successfully")
                print("User intervention required")
                print("Exiting program")
                break
            elif (status == "default"):
                print("Check status function didn't find a status")
                print("Exiting program")
                break

    elif (start_or_stop.lower() == "stop"):
        for service in services:
            print("stopping service " + service)
            stop_service(service)
            delay_action(delay)
            status = check_service_status(service)
            if (status == "inactive"):
                print(service.title() + "was stopped successfully")
            elif (status == "active"):
                print(service.title() + "was not stopped successfully")
                print("User intervention required")
                print("Exiting program")
                break
            elif (status == "default"):
                print("Check status function didn't find a status")
                print("Exiting program")
                break

