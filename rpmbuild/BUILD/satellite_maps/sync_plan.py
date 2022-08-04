#!/usr/bin/python3

import helper as helper


class SyncPlan:

    def display(self):
        for file in helper.directory_content('sync_plan_org'):
            information = helper.convert(file)
            print(file)
            print('')
            for plan in information:
                print(helper.magentatext + 'Name: ', plan.get('name'))
                print('ID: ', plan.get('id'))
                print('Organization ID: ', plan.get('organization_id'))
                print('Created: ', plan.get('created_at'))
                print('Updated: ', plan.get('updated_at'))
                print('Description: ', plan.get('description'))
                print('Interval: ', plan.get('interval'))
                print('Next Sync Date: ', plan.get('next_sync'))
                print('Enabled: ', plan.get('enabled'))
                print(helper.reset + helper.bluetext + 'Products:')
                for prod in plan.get('products'):
                    print('\tName: ', prod.get('name'))
                    print('\tLabel: ', prod.get('label'))
                    print('\tID: ', prod.get('id'))
                    print('\tCandlepin ID: ', prod.get('cp_id'))
                    print('\tDescription: ', prod.get('description'))
                    print('\tSync State: ', prod.get('sync_state'))
                    print('\tLast Sync: ', prod.get('last_sync_words'))
                    print('\tLast Sync Date: ', prod.get('last_sync'))
                    print('\tRepo Count: ', prod.get('repository_count'))
                    print('')
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
