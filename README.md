# ansible-net-mapper
Ansible Role to gather IPv4 networks configured on Cisco devices

## Role Variables

    log: "false"

If true, collect current date/time and write host's networks to disk.
## Dependencies
None.
## Example Playbook
```
---
- name: Get IP networks from all devices
  hosts: all
  connection: network_cli
  roles:
    - role: net_mapper
      vars:
        log: true
...
```
## Example Returned Data (per host)
```
[
    {
        "ipv4": [
            {
                "network": "172.16.10.32/30",
                "address": "172.16.10.33/30"
            }
        ],
        "name": "Vlan10"
    },
    {
        "ipv4": [
            {
                "network": "10.1.0.0/21",
                "address": "10.1.1.1/21"
            }
        ],
        "name": "Ethernet1/1"
    },
    {
        "ipv4": [
            {
                "network": "192.168.1.2/32",
                "address": "192.168.1.2/32"
            }
        ],
        "name": "loopback0"
    }
]
```
