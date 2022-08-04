#!/usr/bin/python3

import helper as helper


class ConfigTemplate:

    def __init__(self):
        self.information = helper.convert('config_templates.json')

    def display(self):
        for template in self.information:
            print(helper.tealtext + 'Name: ', template.get('name'))
            print('ID: ', template.get('id'))
            print('Created: ', template.get('created_at'))
            print('Updated: ', template.get('updated_at'))
            print('\tTemplate type: ', template.get('template_kind_name'))
            print('\tTemplate id: ', template.get('template_kind_id'))
            print('\tSnippet?: ', template.get('snippet'))
            try:
                print('\tAudit comment: ', template.get('audit_comment'))
            except AttributeError:
                print('\tAudit comment: None')
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
