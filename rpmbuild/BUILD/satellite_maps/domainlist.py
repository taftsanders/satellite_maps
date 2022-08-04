#!/usr/bin/python3

import helper as helper


class DomainList:

    def __init__(self):
        self.information = helper.convert('domain_list.json')

    def display(self):
        for domain in self.information:
            print(helper.magentatext + 'Name: ', domain.get('name'))
            print(helper.reset + helper.bluetext + 'ID: ', domain.get('id'))
            print('Created at: ', domain.get('created_at'))
            print('Updated at: ', domain.get('updated_at'))
            print('Fullname: ', domain.get('fullname'))
            print('DNS ID: ', domain.get('dns_id'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)