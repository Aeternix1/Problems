#Starts a service
#Delays for 2 minutes
#Checks that the service is active
#If the service is inactive print "User intervention required" and close program
#If the service is active move onto the next service

from service import start_service, check_service_status,set_delay

#List contains all of the services you want to start
services_to_start = ["apache2"]

#Set the delay (s) between starting a service and checking the status of the service
delay = 90

#Starts all services in services_to_start list
#If any of the services failed to start program will be exited
for service in services_to_start:
    print("starting service " + service)
    start_service(service)
    set_delay(delay)
    status = check_service_status(service)
    if (status == "inactive"):
        print(service.title() + " did not start")
        print("User intervention required")
        print("Exiting program")
        break





