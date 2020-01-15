## 1st problem: Cannot type *AT* command via Screen or Minicom in Raspberry Pi


Procedure commands of connecting OBD-ii bluetooth to raspberry pi
Install Pi Bluetooth Manager or using Command line as following:
```
bluetoothctl
power on
pairable on
agent on
default-agent

#find OBDII and its MAC address
scan on   

pair <OBD2_mac_address>
#enter pin 1234

#Automatically pair with the device next time
trust <OBD2_mac_address>  

scan off

#show paired devices, OBDII should be within list
paired-devices  

quit
```
check /dev/
```
cd /dev
ls <-- check if there is rfcomm0

sudo rfcomm bind rfcomm0 <OBD2_mac_address> 
rfcomm <-- it should show 'rfcomm0: <OBD2_mac_address> channel 1 clean'
```
### using minicom or screen to send AT commands like following:
```
ATD
ATZ
AT E0
AT L0
AT S0
AT H0
AT SP 0
```
**this is where we have problems now**

using screen (apt-get install screen):
```
sudo screen /dev/rfcomm0
```
or using minicom (sudo apt-get install minicom):
```
sudo minicom -b 9600 -o -D /dev/rfcomm0
```
**currently, it fails everytime with 'screen is terminating' & the rfcomm0 will turn from 'clean' to 'closed'**

Then, the release command is needed to release and rebind the rfcomm0 with <OBD2_mac_address> 
```
sudo rfcomm release OBDII

sudo rfcomm bind rfcomm0 <OBD2_mac_address> 

rfcomm

#shows 'rfcomm0: <OBD2_mac_address> channel 1 clean'
```
### successful config should have output from Screen like this:
https://www.youtube.com/watch?v=DABytIdutKk

### Or from Minicom like this:
https://www.youtube.com/watch?v=NvYXtQmOYDw

## However, connect to OBD python is successful
install steps plz follow: https://python-obd.readthedocs.io/en/latest/

```
sudo rfcomm bind hci0 <OBD2_mac_address> 

```
run python script
```
python3 reader.py
```
Out put as readeroutput1.png & readeroutput2.png

**TODO**
* Troubleshoting AT Commands Sending in Raspberry Pi
* Based on OBD python to make a program with UI and keep asking OBD data and log
