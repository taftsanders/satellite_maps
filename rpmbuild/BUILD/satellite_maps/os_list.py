#!/usr/bin/python3

import helper as helper


class OSList:

    def display(self):
            information = helper.convert('os_list.json')
            for os in information:
                print(helper.bluetext + 'Name: ', os.get('name'))
                print(helper.reset + helper.redtext + 'Title: ', os.get('title'))
                print(helper.reset + helper.bluetext + 'ID: ', os.get('id'))
                print('Created at: ', os.get('created_at'))
                print('Updated at: ', os.get('updated_at'))
                print('Description: ', os.get('description'))
                print(helper.reset + helper.greentext + 'Family: ', os.get('family'))
                print('Major Release: ', os.get('major'))
                print('Minor Release: ', os.get('minor'))
                print(helper.reset + helper.bluetext + 'Release Name: ', os.get('release_name'))
                print('Password Hash: ', os.get('password_hash'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
