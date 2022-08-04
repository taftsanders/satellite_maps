#!/usr/bin/python3

import helper as helper


class PuppetEnviornment:

    def display(self):
        for file in helper.directory_content('puppet_environments_org'):
            information = helper.convert(file)
            print(file)
            print('')
            for env in information:
                print(helper.magentatext + 'Name: ', env.get('name'))
                print('ID: ', env.get('name'))
                print(helper.reset + helper.bluetext + 'Created: ', env.get('created_at'))
                print('Updated: ', env.get('updated_at'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
