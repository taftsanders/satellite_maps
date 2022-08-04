#!/usr/bin/python3

import satellite_maps.helper as helper


class ContentViewPuppetMods:

    def cv_version(self):
        file = helper.directory_content('cv_puppet_modules_')
        return file

    def display(self):
        for file in helper.directory_content('cv_puppet_modules_'):
            print(file)
            print('')
            self.information = helper.convert(file)
            for mod in self.information:
                print(helper.magentatext + 'Name: ', mod.get('name'))
                print(helper.reset + helper.tealtext + 'ID: ', mod.get('id'))
                print('Version: ', mod.get('computed_version'))
                print('Author: ', mod.get('author'))
                print('Created: ', mod.get('created_at'))
                print('Updated: ', mod.get('updated_at'))
                print('')
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)

