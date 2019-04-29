# CaptivePortal
Simple captive portal using Python3, Flask and Netfilter

First, install all the dependencies by executing the setup.sh file.

Then, you have to connect your computer to an RJ45 connexion (or all other kind
of connexion except Wi-Fi) and execute the start.sh file (as root)

You have to change the IP adress in the main script server.py

All web requests from the users are redirected to the local machine and all
the traffic to the outside is rejected as long as the user has not logged in.
You can create an account, and one the user has logged in, his traffic is
accepted.

Correctly detected by OS x, Windows, Ubuntu, iOS, Android

Available at dassko5@hotmail.fr for bugs.

This programm is a fork of the AloysAugustin programm
(https://github.com/AloysAugustin/captive_portal)
