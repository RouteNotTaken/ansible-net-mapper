# ansible-net-mapper
Ansible Role to gather IPv4 networks configured on Cisco devices

## Role Variables

    log: "false"

If true, collect current date/time and write host's networks to disk.
## Dependencies
None.
## Example Playbook
    ---
    - name: Get IP networks from all devices
      hosts: all
      connection: network_cli
      roles:
        - role: net_mapper
          vars:
            log: true
    ...
