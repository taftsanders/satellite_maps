#!/usr/bin/python3

import satellite_maps.helper as helper


class RexHistory:

    def display(self):
            information = helper.convert('rex_history.json')
            for his in information:
                print(helper.magentatext + 'Description: ', his.get('description'))
                print(helper.reset + helper.bluetext + 'ID: ', his.get('id'))
                print('Job Category: ', his.get('job_category'))
                print('Target ID: ', his.get('targeting_id'))
                if his.get('status_label') == 'failed':
                    print(helper.reset + helper.redtext + 'Status: ', his.get('status_label'))
                elif his.get('status_label') == 'succeeded':
                    print(helper.reset + helper.greenbright + 'Status: ', his.get('status_label'))
                else:
                    print(helper.reset + helper.goldtext + 'Status: ', his.get('status_label'))
                print(helper.reset + helper.slatebluetext + 'Dynflow Task:')
                print('\tID: ', his.get('dynflow_task').get('id'))
                print('\tState: ', his.get('dynflow_task').get('state'))
                print(helper.reset + helper.greentext + 'Counts:')
                print('\tSucceeded: ', his.get('succeeded'))
                print('\tFailed: ', his.get('failed'))
                print('\tPending: ', his.get('pending'))
                print('\tTotal: ', his.get('total'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
