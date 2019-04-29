#!/bin/bash
SESSION=$USER

#sudo hostapd hostapd.conf

#wondershaper wlo1 8192 1600

sudo ./clean_firewall.sh

sudo ./firewall.sh

sudo python server.py
