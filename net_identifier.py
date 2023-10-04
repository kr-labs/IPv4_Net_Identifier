#!/usr/bin/env python3
import ipaddress


def identify_network_and_broadcast(ip_str, subnet_str):
    try:
        ip_address = ipaddress.IPv4Address(ip_str)
        subnet_mask = ipaddress.IPv4Address(subnet_str)

        return logic_network_and_broadcast(ip_address, subnet_mask)

    except ValueError:
        return "Invalid IP address or Subnet Mask."


def logic_network_and_broadcast(ip_add, subnet_mask):
    if not ip_add.is_private or not subnet_mask.is_private:
        return "Please provide a valid private IP Address and Subnet Mask."

    network_address = ipaddress.IPv4Network(f"{ip_add}/{subnet_mask}", strict=False)
    broadcast_address = network_address.broadcast_address

    return f"Network Address: {network_address}\nBroadcast Address: {broadcast_address}"


ip_string = input("Enter an IPv4 address: ")
subnet_string = input("Enter a subnet mask: ")

result = identify_network_and_broadcast(ip_string, subnet_string)

print(result)
