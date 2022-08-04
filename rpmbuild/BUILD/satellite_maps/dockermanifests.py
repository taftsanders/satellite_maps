#!/usr/bin/python3

import helper as helper


class DockerManifest:

    def __init__(self):
        self.information = helper.convert('dockermanifests.json')

    def display(self):
        for mani in self.information:
            print(helper.magentatext + 'Name: ', mani.get('name'))
            print(helper.reset + helper.bluetext + 'ID: ', mani.get('id'))
            print('Schema Version: ', mani.get('schema_version'))
            print('Digest: ', mani.get('digest'))
            print('Downloaded: ', mani.get('downloaded'))
            print(helper.reset + helper.greentext + 'Tags:')
            for tag in mani.get('tags'):
                print('\tName: ', tag.get('name'))
                print('\tID: ', tag.get('id'))
                print('\tRepo ID: ', tag.get('repository_id'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)