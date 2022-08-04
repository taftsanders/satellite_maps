#!/usr/bin/python3

import satellite_maps.helper as helper


class ComputeResource:

    def __init__(self):
        self.information = helper.convert('compute_resources.json')

    def display(self):
        for resource in self.information:
            print(helper.tealtext + 'Name: ', resource.get('name'))
            print('ID: ', resource.get('id'))
            print('Created: ', resource.get('created_at'))
            print('Updated: ', resource.get('updated_at'))
            print('Description: ', resource.get('description'))
            print(helper.reset + helper.darkredtext + 'URL: ', resource.get('url'))
            print('Provider: ', resource.get('provider'))
            print('Provider friendly version: ', resource.get('provider_friendly_name'))
            print('Display type: ', resource.get('display_type'))
            print('Console password?: ', resource.get('set_console_password'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
