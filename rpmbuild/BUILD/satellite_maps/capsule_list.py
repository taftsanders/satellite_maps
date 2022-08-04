#!/usr/bin/python3

import helper as helper


class CapsuleList:

    def __init__(self):
        self.information = helper.convert('capsule_list.json')

    def display(self):
        for capsule in self.information:
            print(helper.tealbg + 'Name: ', capsule.get('name'))
            print(helper.reset + helper.tealtext + 'ID: ', capsule.get('id'))
            print('URL: ', capsule.get('url'))
            print('Created: ', capsule.get('created_at'))
            print('Updated: ', capsule.get('updated_at'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
