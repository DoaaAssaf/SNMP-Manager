# SNMP-Manager
snmp protocol manager
This simple "linux-based" desktop application with GUI like other management tools, PowerSNMP for example.
I focused  on the manager side only not the agen.

The application GUI  handle the following: 

1- Determine the IP address for the target agent.

2- Select the version of snmp.

3- Enter all information related to the security of snmp based on the version selected by the user.

4- Show a list of common  MIB objects to be managed. 

5- perform scanning the network and show up hosts

6- show all MIB tree

7- Get the selected object value via sending a GetRequest pdu to the target agent. Then display the response.

8- Set  the selected object value via sending a SetRequest pdu to the target agent.

9- Handle and show Trap messages whenever it happens. 



 
