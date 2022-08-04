#!/usr/bin/python3

import satellite_maps.helper as helper


class Settings:

    def display(self):
            information = helper.convert('settings.json')
            for setting in information:
                print(helper.magentatext + 'Name: ', setting.get('name'))
                print(helper.reset + helper.bluetext + 'ID: ', setting.get('id'))
                print(helper.reset + helper.greentext + 'Description: ', setting.get('description'))
                print(helper.reset + helper.redtext + 'Value: ', setting.get('value'))
                try:
                    print(helper.reset + helper.goldtext + 'Default: ', setting.get('default'))
                except AttributeError:
                    print(helper.reset + helper.goldtext + 'Default: Null')
                print(helper.reset + helper.slatebluetext + 'Updated at', setting.get('updated_at'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
