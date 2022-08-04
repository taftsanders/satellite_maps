#!/usr/bin/python3

import helper as helper


class Arch_List:

    def __init__(self):
        self.information = helper.convert('arch_list.json')

    def display(self):
        for arch in self.information:
            print(helper.greentext + 'Name: ', arch.get('name'))
            print('ID: ', arch.get('id'))
            print(helper.reset + helper.magentatext + 'Created at: ', arch.get('created_at'))
            print('Updated at: ', arch.get('updated_at'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)

