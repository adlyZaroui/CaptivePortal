#!/bin/bash

IPTABLES=/sbin/iptables


$IPTABLES -N internet -t mangle

$IPTABLES -t mangle -A PREROUTING -j internet

$IPTABLES -t mangle -A internet -j MARK --set-mark 99

$IPTABLES -t nat -A PREROUTING -m mark --mark 99 -p tcp --dport 80 -j DNAT --to-destination 10.42.0.1

#$IPTABLES -t filter -A INPUT -p tcp --dport 80 -j ACCEPT
#$IPTABLES -t filter -A INPUT -p udp --dport 53 -j ACCEPT
#$IPTABLES -t filter -A INPUT -m mark --mark 99 -j DROP

echo "1" > /proc/sys/net/ipv4/ip_forward

$IPTABLES -A FORWARD -i eno1 -o wlo1 -m state --state ESTABLISHED,RELATED -j ACCEPT
$IPTABLES -A FORWARD -m mark --mark 99 -j REJECT
$IPTABLES -A FORWARD -i wlo1 -o eno1 -j ACCEPT
$IPTABLES -t nat -A POSTROUTING -o eno1 -j MASQUERADE
