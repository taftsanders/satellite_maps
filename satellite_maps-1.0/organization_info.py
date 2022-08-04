#!/usr/bin/python3

import satellite_maps.helper as helper
import json


class Organization_info:

    def display(self):
        for file in helper.directory_content('organizational_details_org'):
            with open(file) as data:
                detail = json.load(data)
            print(helper.greenbluetext + "Filename: %s" % file + helper.reset)
            print('')
            print(helper.magentatext +  'Name: ', detail.get('name'))
            print('Label: ', detail.get('label'))
            print('ID: ', detail.get('id'))
            print('Created at: ', detail.get('created_at'))
            print('Description: ', detail.get('description'))
            print('Ancestry: ', detail.get('ancestry'))
            print('Red Hat Repo URL: ', detail.get('redhat_repository_url'))
            print('Service Level Set: ', detail.get('service_level'))
            print('Available Service Level: ')
            try:
                for level in detail.get('service_levels'):
                    print(level)
            except TypeError:
                print('None')
            print(helper.reset + '')
            print(helper.darkredtext + 'Users:')
            for user in detail.get('users'):
                print('\t' + 'Username: ', user.get('login'))
                print('\t' + 'ID: ', user.get('id'))
                print('\t' + 'Description: ', user.get('id'))
                print('')
            print(helper.reset + '')
            print(helper.darkredbg + 'Locations:')
            try:
                for loc in detail.get('locations'):
                    print('\t' + 'Name: ', loc.get('name'))
                    print('\t' + 'ID: ', loc.get('id'))
                    print('')
            except TypeError:
                print('\t' + 'None')
            print(helper.reset + '')
            print(helper.magentabg + 'Puppet Environment:')
            for env in detail.get('environments'):
                print('\t' + 'Name: ', env.get('name'))
                print('\t' + 'ID: ', env.get('id'))
                print('')
            print('Puppet Hostgroups:')
            for hg in detail.get('hostgroups'):
                print('\t' + 'Name: ', hg.get('name'))
                print('\t' + 'Title: ', hg.get('title'))
                print('\t' + 'ID: ', hg.get('id'))
                print('')
            print(helper.reset + '')
            print(helper.orangebg + 'Compute Resources:')
            try:
                for compute in detail.get('compute_resources'):
                    print('\t' + 'Name: ', compute.get('name'))
                    print('\t' + 'ID: ', compute.get('id'))
                    print('\t' + 'Provider: ', compute.get('provider'))
                    print('')
            except TypeError:
                print('None')
            print(helper.reset + '')
            print(helper.orangetext + 'Smart Proxies:')
            for smart in detail.get('smart_proxies'):
                print('\t' + 'Name: ', smart.get('name'))
                print('\t' + 'ID: ', smart.get('id'))
                print('\t' + 'URL: ', smart.get('url'))
                print('')
            print('')
            print('Subnets:')
            try:
                for subnet in detail.get('subnets'):
                    print('\t' + 'Name: ', subnet.get('name'))
                    print('\t' + 'ID: ', subnet.get('id'))
                    print('')
            except TypeError:
                print('\t' + 'None')
            print('')
            print('Domains:')
            try:
                for domain in detail.get('domains'):
                    print('\t' + 'Name: ', domain.get('name'))
                    print('\t' + 'ID: ', domain.get('id'))
                    print('')
            except TypeError:
                print('\t' + 'None')
            print('')
            print('Realms:')
            try:
                for realm in detail.get('realms'):
                    print('\t' + 'Name: ', realm.get('name'))
                    print('\t' + 'ID: ', realm.get('id'))
            except TypeError:
                print('\t' + 'None')
            print(helper.reset + '')
            print(helper.tealtext + 'Configuration Templates:')
            try:
                for template in detail.get('config_templates'):
                    print('\t' + 'Name: ', template.get('name'))
                    print('\t' + 'ID: ', template.get('id'))
                    print('\t' + 'Kind Name: ', template.get('template_kind_name'))
                    print('\t' + 'Kind ID: ', template.get('template_kind_id'))
                    print('')
            except TypeError:
                print('None')
            print('Media:')
            try:
                for iso in detail.get('media'):
                    print('\t' + 'Name: ', iso.get('name'))
                    print('\t' + 'ID: ', iso.get('id'))
                    print('')
            except TypeError:
                print('\t' + 'None')
            print('Partition Tables:')
            for ptable in detail.get('ptables'):
                print('\t' + 'Name: ', ptable.get('name'))
                print('\t' + 'ID:, ', ptable.get('id'))
                print('\t' + 'Created: ', ptable.get('created_at'))
                print('\t' + 'Updated: ', ptable.get('updated_at'))
                print('\t' + 'OS Family: ', ptable.get('os_family'))
                print('')
            print(helper.redtext + '#' * 50 + 'END OF ORG' + '#' * 50 + '\n' + helper.reset)
        print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)

