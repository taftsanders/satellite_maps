#!/usr/bin/python3

import helper as helper


class DiscoveryRules:

    def __init__(self):
        self.information = helper.convert('discovery_rules.json')

    def display(self):
        for rule in self.information:
            print(helper.magentatext + 'Name: ', rule.get('name'))
            print(helper.reset + helper.redtext + 'Enabled: ', rule.get('enabled'))
            print(helper.reset + helper.bluetext + 'Hostgroup ID: ', rule.get('hostgroup_id'))
            print('Hostgroup Name: ', rule.get('hostgroup_name'))
            print('Hostname: ', rule.get('hostname'))
            print('Priority: ', rule.get('priority'))
            print(helper.reset + helper.greentext + 'Search: ', rule.get('search'))
            print(helper.reset + helper.bluetext + 'Hosts Limit: ', rule.get('hosts_limits'))
            print('ID: ', rule.get('id'))
            for host in rule.get('hosts'):
                print(host)
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
