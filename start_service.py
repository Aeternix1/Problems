#Starts a service
#Delays for 2 minutes
#Checks that the service is active
#If the service is inactive print "User intervention required" and close program
#If the service is active move onto the next service

from service import start_service, check_service_status,set_delay

#List contains all of the services you want to start
services_to_start = ["apache2", "apache2"]

#Will run through all the services until the end of list
#Or if a service that was started is currently inactive
for service in services_to_start:
    start_service(service)
    set_delay(10)
    status = check_service_status(service)
    if (status == "inactive"):
        print("Service did not start")
        print("User intervention required")
        print("Exiting program")
        break



