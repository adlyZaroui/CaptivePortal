# CaptivePortal
Simple captive portal using Python3, Flask and Netfilter

First, install all the dependencies by executing the setup.sh file.

Then, you have to connect your computer to an RJ45 connecter (or all other kind
of wired connexion) and execute as root the start.sh file

You have to change the IP adress in the main script server.py

All web requests from the users are redirected to the local machine and all
the traffic to the outside is rejected as long as the user has not logged in.
You can create an account, and once the user has logged in, his traffic is
accepted.

Correctly detected by OS x, Windows, Ubuntu, iOS, Android

If any help needed, please feel free to contact me at dassko5@hotmail.fr

This programm is a fork of the AloysAugustin programm (https://github.com/AloysAugustin/captive_portal)
