# NETS1030 Network Security Assignment 3

Starting Base File Hash:

    Assignment_3_Base.pkt       ca03d686b44826752f1ba06b8560a247e21ce805 

## Assignment

Using the provided Assignment 3.pkt Packet Tracer File create the VPN as described below.


It is very simple instructions. 
Create a VPN from both Router 1 and Router 2 that terminates on Router 3.   To be clear…….Router 3 will have two vpn connections on it and the other routers will have 1 each.
You may use any Pre Shared Keys you want to make up but they must be different for both VPN’s.
I should be able to ping from the laptops in Router 1 and 2 networks to the laptop in Router 3 network.    Tunnels should show up if I check.
Take screen shots at a few times during your configurations.   Take screen shots of the pings working.  Screen shot should include your name and student number in a text box.
Use google if you get stuck.   I have provided a doc as a reference.

Hint.   Remember the issue we encountered in class with the NAT rules needing to be modified.
Please remember to do your own work.  (Working in a group is fine but each student must do and submit their own work)    I reserve the right to question your work for further explanation on how you set it up.   Best to make sure you can answer by having done the config yourself.   😊

This assignment is worth 15% of your final mark.   Total marks available are…..30    Submit your working Packet Tracer File as well as your word doc with your screen shots in it.
Assignments will be accepted after the due date with a 10% deduction in mark per day late.


#### Debug Commands

    debug crypto ipsec      Shows the IPsec negotiations of phase 2.

    debug crypto isakmp     Shows the ISAKMP negotiations of phase 1.

    debug crypto engine     Shows the traffic that is encrypted.

    clear crypto isakmp     Clears the SAs related to phase 1.

    clear crypto sa         Clears the SAs related to phase 2.
