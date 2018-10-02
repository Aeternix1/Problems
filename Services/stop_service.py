#Stops a service
#Delays for 2 minutes
#Checks that the service is inactive
#If the service is active print "User intervention required" and close program
#If the service is inactive move onto the next service

from service import stop_service, check_service_status,set_delay

#List contains all of the services you want to stop
services_to_stop = ["apache2"]

#Set the delay (s) between starting a service and checking the status of the service
delay = 10

#Starts all services in services_to_start list
#If any of the services failed to start program will be exited
for service in services_to_stop:
    print("stopping service " + service)
    stop_service(service)
    set_delay(delay)
    status = check_service_status(service)
    if (status == "active"):
        print(service.title() + " did not stop")
        print("User intervention required")
        print("Exiting program")
        break




