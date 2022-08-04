#!/usr/bin/python3

import helper as helper


class Media:

    def display(self):
        for file in helper.directory_content('media_org'):
            information = helper.convert(file)
            print(file)
            print('')
            for media in information:
                print(helper.magentatext + 'Name: ', media.get('name'))
                print(helper.reset + helper.bluetext + 'ID: ', media.get('id'))
                print('Created at: ', media.get('created_at'))
                print('Updated at: ', media.get('updated_at'))
                print('OS Family: ', media.get('os_family'))
                print(helper.reset + helper.greentext + 'Path: ', media.get('path'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
