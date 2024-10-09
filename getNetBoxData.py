#!/usr/bin/env python3

import sys
import pynetbox


def getNetBox(netbox_url, netbox_token):
    try:
        nb = pynetbox.api(url=netbox_url, token=netbox_token)
        f = open("netbox.log", "w")

        # Get all devices
        devices = nb.dcim.devices.all()
        print(devices, file = f)

        # Get all virtual machines
        vms = nb.virtualization.virtual_machines.all()
        print(vms, file = f)

        f.close()

    except Exception as e:
        print(f"Error fetching data from NetBox: {e}")
        exit

if __name__ == "__main__":
    netbox_url = sys.argv[1]
    netbox_token = sys.argv[2]
    getNetBox(netbox_url, netbox_token)
