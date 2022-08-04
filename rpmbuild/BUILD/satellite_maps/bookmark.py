#!/usr/bin/python3

import helper as helper


class Bookmark:

    def __init__(self):
        self.information = helper.convert('bookmark_list.json')

    def display(self):
        for mark in self.information:
            print(helper.greentext + 'Name: ', mark.get('name'))
            print('ID: ', mark.get('id'))
            print('Controller: ', mark.get('controller'))
            print(helper.reset + helper.darkredtext + 'Query: ', mark.get('query'))
            print(helper.reset + helper.greentext + 'Public: ', mark.get('public'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
