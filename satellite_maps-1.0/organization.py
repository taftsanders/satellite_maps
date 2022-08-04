#!/usr/bin/python3

import satellite_maps.helper as helper


class Organization:

    def __init__(self):
        self.information = helper.convert('organization_list.json')

    def display(self):
        for org in self.information:
            print(helper.greentext + 'Name: ', org.get('name'))
            print('Title: ', org.get('title'))
            print('Label: ', org.get('label'))
            print('ID: ', org.get('id'))
            print(helper.reset + helper.magentatext + '\tCreated: ', org.get('created_at'))
            print('\tUpdated: ', org.get('updated_at'))
            print('\tDescription: ', org.get('description'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
