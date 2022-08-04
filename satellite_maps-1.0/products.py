#!/usr/bin/python3

import satellite_maps.helper as helper


class Product:

    def display(self):
        for file in helper.directory_content('products_org'):
            information = helper.convert(file)
            print(file)
            for prod in information:
                print(helper.magentatext + 'Name: ', prod.get('name'))
                print('Label: ', prod.get('label'))
                print(helper.reset + helper.bluetext + 'ID: ', prod.get('id'))
                print('Candlepin ID: ', prod.get('cp_id'))
                try:
                    print('Description: ', prod.get('description'))
                except AttributeError:
                    print('Description: Null')
                print('Repo Count: ', prod.get('repository_count'))
                try:
                    print('Sync Plan ID: ', prod.get('sync_plan_id'))
                except AttributeError:
                    print('Sync Plan ID: Null')
                if prod.get('sync_summary').get('success'):
                    print(helper.reset + helper.darkredtext + 'Sync Summary: ')
                    print('Success: ', prod.get('sync_summary').get('success'))
                elif prod.get('sync_summary').get('warning'):
                    print(helper.reset + helper.darkredtext + 'Sync Summary: ')
                    print('Warning: ', prod.get('sync_summary').get('warning'))
                else:
                    print(helper.reset + helper.darkredtext + 'Sync Summary: None')
                try:
                    print('Sync State: ', prod.get('sync_state'))
                except AttributeError:
                    print('Sync State: Null')
                try:
                    print('Last Sync Date: ', prod.get('last_sync'))
                    print('\t', prod.get('last_sync_words'))
                except AttributeError:
                    print('Last Sync Date: Null')
                print(helper.reset + helper.orangetext + 'Organization')
                print('\tName: ', prod.get('organization').get('name'))
                print('\tLabel: ', prod.get('organization').get('label'))
                print('\tID: ', prod.get('organization').get('id'))
                print(helper.reset + helper.slatebluetext + 'Sync Plan:')
                try:
                    print('\tName: ', prod.get('sync_plan').get('name'))
                    print('\tSync Date: ', prod.get('sync_plan').get('sync_date'))
                    print('\tInterval: ', prod.get('sync_plan').get('interval'))
                    print('\tNext Sync Date: ', prod.get('sync_plan').get('next_sync'))
                except AttributeError:
                    print('\tNone')
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
