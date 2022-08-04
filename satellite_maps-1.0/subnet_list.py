#!/usr/bin/python3

import satellite_maps.helper as helper


class SubnetList:

    def display(self):
            information = helper.convert('subnet_list.json')
            for sub in information:
                print(helper.magentatext + 'Name: ', sub.get('name'))
                print(helper.reset + helper.bluetext + 'ID: ', sub.get('id'))
                print('Created: ', sub.get('created_at'))
                print('Updated: ', sub.get('updated_at'))
                print('Network: ', sub.get('network'))
                print('CIDR: ', sub.get('cidr'))
                try:
                    print('Priority: ', sub.get('priority'))
                except AttributeError:
                    continue
                print('VLAN ID: ', sub.get('vlanid'))
                print('Gateway: ', sub.get('gateway'))
                print(helper.reset + helper.greentext + 'DNS:')
                print('\tPrimary: ', sub.get('dns_primary'))
                print('\tSecondary: ', sub.get('dns_secondary'))
                try:
                    print(helper.reset + helper.greentext + 'DHCP Range:')
                    print('\tFrom: ', sub.get('from'))
                    print('\tTo: ', sub.get('to'))
                except AttributeError:
                    print(helper.reset + helper.greentext + 'DHCP Range: ')
                    print('\tFrom: Null')
                    print('\tTo: Null')
                print(helper.reset + helper.bluetext + 'IPAM: ', sub.get('ipam'))
                print('Boot Mode: ', sub.get('boot_mode'))
                print('Network Address: ', sub.get('network_address'))
                try:
                    print('External DHCP: ', sub.get('dhcp'))
                except AttributeError:
                    print('External DHCP: Null')
                try:
                    print('External DNS: ', sub.get('dns'))
                except AttributeError:
                    print('External DNS: ', sub.get('dns'))
                print(helper.reset + helper.orangetext + 'TFTP:')
                print('\tName: ', sub.get('tftp').get('name'))
                print('\tID: ', sub.get('tftp').get('id'))
                print('\tURL: ', sub.get('tftp').get('url'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
