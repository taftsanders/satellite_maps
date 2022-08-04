#!/usr/bin/python3

import helper as helper


class DockerTag:

    def __init__(self):
        self.information = helper.convert('dockertags.json')

    def display(self):
        for tag in self.information:
            print(helper.magentatext + 'Name: ', tag.get('name'))
            print('ID: ', tag.get('id'))
            print('Full Name: ', tag.get('full_name'))
            print('Repository ID: ', tag.get('repository_id'))
            print(helper.reset + helper.bluetext + 'Manifest:')
            print('\tName: ', tag.get('manifest').get('name'))
            print('\tID: ', tag.get('manifest').get('id'))
            print(helper.reset + helper.greentext + 'Repository:')
            print('\tName: ', tag.get('repository').get('name'))
            print('\tID: ', tag.get('repository').get('id'))
            print('\tFull Path: ', tag.get('repository').get('full_path'))
            print(helper.reset + helper.orangetext + 'Product:')
            print('\tName: ', tag.get('product').get('name'))
            print('\tID: ', tag.get('product').get('id'))
            print(helper.reset + helper.tealtext + 'Environment:')
            print('\tName: ', tag.get('environment').get('name'))
            print('\tID: ', tag.get('environment').get('id'))
            print(helper.reset + helper.boldwhite + 'Content View Version:')
            print('\tName: ', tag.get('content_view_version').get('name'))
            print('\tID: ', tag.get('content_view_version').get('id'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
