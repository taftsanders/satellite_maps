#!/usr/bin/python3

import helper as helper


class TemplateKind:

    def display(self):
            information = helper.convert('template_kinds.json')
            for temp in information:
                print(helper.magentatext + 'Name: ', temp.get('name'))
                print(helper.reset + helper.bluetext + 'ID: ', temp.get('id'))
                print('Created: ', temp.get('created_at'))
                print('Updated: ', temp.get('updated_at'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
