#!/usr/bin/python3

import helper as helper
import json


class Statistics:

    def convert(self, file_name):
        with open(file_name) as file:
            information = json.load(file)
            return information

    def display(self):
            information = self.convert('statistics.json')
            print(helper.magentatext + 'Operating Systems:')
            for os in information.get('os_count'):
                print('\tLabel: ', os.get('label'))
                print('\tCount: ', os.get('data'))
                print('')
            print(helper.reset + helper.bluetext + 'Architectures:')
            for arch in information.get('arch_count'):
                print('\tLabel: ', arch.get('label'))
                print('\tCount: ', arch.get('data'))
                print('')
            print(helper.reset + helper.slatebluetext + 'Puppet Environments:')
            for env in information.get('env_count'):
                print('\tLabel: ', env.get('label'))
                print('\tCount: ', env.get('data'))
                print('')
            print(helper.reset + helper.orangetext + 'CPU Count:')
            for cpu in information.get('cpu_count'):
                print('\tLabel: ', cpu.get('label'))
                print('\tCount: ', cpu.get('data'))
                print('')
            print(helper.reset + helper.darkredtext + 'Model:')
            for model in information.get('model_count'):
                print('\tLabel: ', model.get('label'))
                print('\tCount: ', model.get('count'))
                print('')
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)

