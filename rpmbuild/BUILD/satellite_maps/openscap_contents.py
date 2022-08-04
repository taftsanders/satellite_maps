#!/usr/bin/python3

import helper as helper


class OpenscapContent:

    def display(self):
            information = helper.convert('openscap_contents.json')
            for scap in information:
                print(helper.magentatext + 'Title: ', scap.get('title'))
                print(helper.reset + helper.bluetext + 'ID: ', scap.get('id'))
                print('Created: ', scap.get('created_at'))
                print('Updated: ', scap.get('updated_at'))
                print('Orgininal Filename: ', scap.get('orgininal_filename'))
                print('Digest: ', scap.get('digest'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
