#!/usr/bin/python3

import satellite_maps.helper as helper


class ProvisionTemplate:

    def display(self):
        for file in helper.directory_content('provisioning_templates_org'):
            information = helper.convert(file)
            print(file)
            print('')
            for template in information:
                print(helper.magentatext + 'Name: ', template.get('name'))
                print(helper.reset + helper.bluetext + 'ID: ', template.get('id'))
                print('Created: ', template.get('created_at'))
                print('Updated: ', template.get('updated_at'))
                print(helper.reset + helper.greentext + 'Snippet?: ', template.get('snippet'))
                try:
                    print(helper.reset + helper.bluetext + 'Template Kind: ', template.get('template_kind_name'))
                except AttributeError:
                    continue
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
