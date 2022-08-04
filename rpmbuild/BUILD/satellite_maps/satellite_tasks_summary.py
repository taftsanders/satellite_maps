#!/usr/bin/python3

import helper as helper
import json


class TaskSummary:

    def convert(self, file_name):
        with open(file_name) as file:
            information = json.load(file)
            return information

    def display(self):
            information = self.convert('satellite_tasks_summary.json')
            for summ in information:
                if summ.get('state') == 'paused':
                    print(helper.reset + helper.redtext + 'State: ', summ.get('state'))
                elif summ.get('state') == 'planning':
                    print(helper.reset + helper.goldtext + 'State: ', summ.get('state'))
                elif summ.get('state') == 'running':
                    print(helper.reset + helper.greentext + 'State: ', summ.get('state'))
                elif summ.get('state') == 'scheduled':
                    print(helper.reset + helper.magentatext + 'State: ', summ.get('state'))
                elif summ.get('state') == 'stopped' and summ.get('result') == 'error':
                    print(helper.reset + helper.redtext + 'State: ', summ.get('state'))
                elif summ.get('state') == 'stopped' and summ.get('result') == 'success':
                    print(helper.reset + helper.bluetext + 'State: ', summ.get('state'))
                elif summ.get('state') == 'stopped' and summ.get('result') == 'warning':
                    print(helper.reset + helper.slatebluetext + 'State: ', summ.get('state'))
                print('Result: ', summ.get('result'))
                print('Count: ', summ.get('count'))
                print('')
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
