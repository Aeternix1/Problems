# #Running unix commands with python script
import subprocess

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





