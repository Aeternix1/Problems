#Stops a service
#Delays for 2 minutes
#Checks that the service is inactive
#If the service is active print "User intervention required" and close program
#If the service is inactive move onto the next service

from service import stop_service, check_service_status,set_delay

#List contains all of the services you want to stop
services_to_stop = ["apache2", "apache2"]

#Will run through all the services until the end of list
#Or if a service that was started is currently inactive
for service in services_to_stop:
    stop_service(service)
    set_delay(10)
    status = check_service_status(service)
    if (status == "active"):
        print("Service was not stopped")
        print("User intervention required")
        print("Exiting program")
        break
