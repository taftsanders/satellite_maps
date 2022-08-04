#!/usr/bin/python3

import helper as helper


class DiscoveredHosts:

    def __init__(self):
        self.information = helper.convert('discovered_hosts.json')

    def display(self):
        for host in self.information:
            print(host.get('name'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
