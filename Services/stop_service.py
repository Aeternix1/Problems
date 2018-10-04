#Stops a service
#Delays for 2 minutes
#Checks that the service is inactive
#If the service is active print "User intervention required" and close program
#If the service is inactive move onto the next service

from service import start_or_stop_services

#List contains all of the services you want to stop
services_to_stop = ["apache2"]

#Set the delay (s) between starting a service and checking the status of the service
delay = 10
start_or_stop_services(services_to_stop, delay, start_or_stop="stop")

