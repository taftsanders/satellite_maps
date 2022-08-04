#!/usr/bin/python3

import helper as helper


class DockerRegistry:

    def __init__(self):
        self.information = helper.convert('docker_registries.json')

    def display(self):
        for reg in self.information:
            print(helper.magentatext + 'Name: ', reg.get('name'))
            print(helper.reset + helper.bluetext + 'ID: ', reg.get('id'))
            print('Created at: ', reg.get('created_at'))
            print('Updated at: ', reg.get('updated_at'))
            print('Description: ', reg.get('description'))
            print('Username: ', reg.get('username'))
            print('URL: ', reg.get('url'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)