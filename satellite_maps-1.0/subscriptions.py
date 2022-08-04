#!/usr/bin/python3

import satellite_maps.helper as helper


class Subscriptions:

    def display(self):
        for file in helper.directory_content('subscriptions_org'):
            information = helper.convert(file)
            print(file)
            for sub in information:
                print(helper.magentatext + 'Product Name: ', sub.get('product_name'))
                print('Name: ', sub.get('name'))
                print('ID: ', sub.get('id'))
                print('Subscription ID: ', sub.get('subscription_id'))
                print('Candlepin ID: ', sub.get('cp_id'))
                print('Product ID: ', sub.get('product_id'))
                print(helper.reset + helper.orangetext + 'Start Date: ', sub.get('start_date'))
                print('End Date: ', sub.get('end_date'))
                print(helper.reset + helper.darkredtext + 'Quantity: ', sub.get('quantity'))
                print('Available: ', sub.get('available'))
                print('Consumed: ', sub.get('consumed'))
                print(helper.reset + helper.slatebluetext + 'Sales:')
                try:
                    print('\tAccount #: ', sub.get('account_number'))
                    print('\tContract #: ', sub.get('contract_number'))
                except AttributeError:
                    print('\tAccount #: Null')
                    print('\tContract #: Null')
                try:
                    print(helper.reset + helper.goldtext + 'Support Level: ', sub.get('support_level'))
                except AttributeError:
                    print(helper.reset + helper.goldtext + 'Support Level: None')
                try:
                    print('Socket Limit: ', sub.get('sockets'))
                except AttributeError:
                    print('Socket Limit: None')
                try:
                    print('Core Limit: ', sub.get('cores'))
                except AttributeError:
                    print('Core Limit: None')
                try:
                    print('Ram Limit: ', sub.get('ram'))
                except AttributeError:
                    print('Ram Limit: None')
                print('Instance Multiplier: ', sub.get('instance_multiplier'))
                try:
                    if sub.get('stacking_id'):
                        print('Stackable: True')
                except AttributeError:
                    print('Stackable: False')
                try:
                    if sub.get('multi_entitlement'):
                        print('Multi-Entitlement: True')
                except AttributeError:
                    print('Multi-Entitlement: False')
                print(helper.reset + helper.greenbright + 'Unmapped Guest: ', sub.get('unmapped_guest'))
                print('Virt-Only: ', sub.get('virt_only'))
                print('Virt-Who: ', sub.get('virt_who'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
