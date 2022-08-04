#!/usr/bin/python3

import helper as helper
import json


class Dashboard:

    def convert(self, file_name):
        with open(file_name) as file:
            information = json.load(file)
            return information

    def display(self):
        information = self.convert('dashboard.json')
        print(helper.orangetext + 'Total Hosts: ', information.get('total_hosts'))
        print('Bad Hosts: ', information.get('bad_hosts'))
        print('Bad Hosts Enabled: ', information.get('bad_hosts_enabled'))
        print('Active Hosts: ', information.get('active_hosts'))
        print('Active Hosts OK: ', information.get('active_hosts_ok'))
        print('Active Hosts OK Enabled: ', information.get('active_hosts_ok_enabled'))
        print('OK Hosts: ', information.get('ok_hosts'))
        print('OK Hosts Enabled: ', information.get('ok_hosts_enabled'))
        print('Out of Sync Hosts: ', information.get('out_of_sync_hosts'))
        print('Out of Sync Hosts Enabled: ', information.get('out_of_sync_hosts_enabled'))
        print('Disabled Hosts: ', information.get('disabled_hosts'))
        print('Pending Hosts: ', information.get('pending_hosts'))
        print('Pending Hosts Enabled: ', information.get('pending_hosts_enabled'))
        print('Good Hosts: ', information.get('good_hosts'))
        print('Good Hosts Enabled: ', information.get('good_hosts_enabled'))
        print('Percentage: ', information.get('percentage'))
        print('Reports Missing: ', information.get('reports_missing'))
        print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
