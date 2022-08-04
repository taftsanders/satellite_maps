#!/usr/bin/python3

import helper as helper
import json


class ManifestHistory:

    def convert(self, file_name):
        with open(file_name) as file:
            information = json.load(file)
            return information

    def display(self):
        for file in helper.directory_content('manifest_history_org'):
            information = self.convert(file)
            print(file)
            print('')
            for manifest in information:
                print(helper.bluetext + 'Date: ', manifest.get('created'))
                print(helper.reset + helper.darkredtext + 'Status: ', manifest.get('status'))
                print(helper.reset + helper.slatebluetext + 'Message: ', manifest.get('statusMessage'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
