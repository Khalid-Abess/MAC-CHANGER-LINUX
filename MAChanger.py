import subprocess
interface = input("Please set the name of the network interface (eth0 or wlan0...) you want to change its MAC: ")
MAC = input("Please set the desired MAC Addresse (xx:xx:xx:xx:xx:xx) to be changed to: ")

subprocess.call("sudo ifconfig " + interface + " down", shell=True)
subprocess.call("sudo ifconfig " + interface + " hw ether " + MAC, shell=True)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)

print("The new MAC for "+ interface +" is: " + MAC)
print("_________________ifconfig results:___________________ ")
subprocess.call("ifconfig", shell=True)