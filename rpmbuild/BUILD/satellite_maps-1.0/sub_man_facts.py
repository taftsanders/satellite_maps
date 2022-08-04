#!/usr/bin/python3

import satellite_maps.helper as helper
import json


class SubManFacts:

    def host_list(self):
        with open('sub-man_fact_values.json') as file:
            datastore = json.load(file)
            information = datastore['results']
            counter = 1
            for key in information:
                print(str(counter) + '. ' + key + '\n')
                counter+=1
            selection = (input('Please copy and paste the client you wish to see here: '))
            return str(selection)

    def display(self):
        information = helper.convert('sub-man_fact_values.json')
        fact = information.get(self.host_list())
        print(helper.orangetext + 'CPU:')
        print('\tCores per Socket: ', fact.get('cpu::core(s)_per_socket'))
        print('\tCPU Count: ', fact.get('cpu::cpu(s)'))
        print('\tCPU Sockets: ', fact.get('cpu::cpu_socket(s)'))
        print('\tCPU Threads Per Core: ', fact.get('cpu::thread(s)_per_core'))
        print('\tlscpu Socket Count: ', fact.get('lscpu::socket(s)'))
        print('\tlscpu Thread Per Core: ', fact.get('lscpu::thread(s)_per_core'))
        print('\tlscup CPUs: ', fact.get('lscpu::cpu(s)'))
        print('')
        print(helper.reset + helper.slatebluetext + 'Network:')
        print('\tNetwork IPv4 address: ', fact.get('network::ipv4_address'))
        print('\tNetwork IPv6 address: ', fact.get('network::ipv6_address'))
        print('\tHostname: ', fact.get('network::hostname'))
        print('\tHostname Override: ', fact.get('network::hostname-override'))
        print('')
        print(helper.reset + helper.darkredtext + 'OS:')
        print('\tuname Type: ', fact.get('virt::host_type'))
        print('\tuname Release: ', fact.get('uname::release'))
        print('\tUUID: ', fact.get('virt::uuid'))
        print('\tdmi System UUID: ', fact.get('dmi::system::uuid'))
        print('\tVirt Host Type: ', fact.get('virt::host_type'))
        print('\tManufacturer: ', fact.get('dmi::system::manufacturer'))
        print('\tFamily: ', fact.get('dmi::system::family'))
        print('\tDistro Name: ', fact.get('distribution::name'))
        print('\tSystem Version: ', fact.get('dmi::system::version'))
        print('\tVirt is guest: ', fact.get('virt::is_guest'))
        print('\tArchitecture: ', fact.get('lscpu::architecture'))
        print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
