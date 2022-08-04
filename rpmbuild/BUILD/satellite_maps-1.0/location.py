#!/usr/bin/python3

import satellite_maps.helper as helper


class Location:

    def __init__(self):
        self.information = helper.convert('location_list.json')

    def display(self):
        for location in self.information:
            print(helper.greentext + 'Name: ', location.get('name'))
            print('Title: ', location.get('title'))
            print('ID: ', location.get('id'))
            print(helper.reset + helper.magentatext + '\tCreated: ', location.get('create_at'))
            print('\tUpdated: ', location.get('updated_at'))
            print('\tDescription: ', location.get('description'))
            print('\tParent Name: ', location.get('parent_name'))
            print('\tParent ID: ', location.get('parent_id'))
            print('\tAncestry: ', location.get('ancestry'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)

