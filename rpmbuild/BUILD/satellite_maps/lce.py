#!/usr/bin/python3

import helper as helper


class LCE:

    def display(self):
        for file in helper.directory_content('lce_org'):
            information = helper.convert(file)
            print(file)
            print('')
            for lce in information:
                print(helper.magentatext + 'Name: ', lce.get('name'))
                print('Label: ', lce.get('label'))
                print('ID: ', lce.get('id'))
                print('Is Library: ', lce.get('library'))
                print('Description: ', lce.get('description'))
                print('Created: ', lce.get('created_at'))
                print('Updated: ', lce.get('updated_at'))
                print(helper.reset + helper.darkredtext + 'Organization:')
                print('\tName: ', lce.get('organization').get('name'))
                print('\tLabel: ', lce.get('organization').get('label'))
                print('\tID: ', lce.get('organization').get('id'))
                print(helper.reset + helper.orangetext + 'Parent LCE:')
                try:
                    print('\tName: ', lce.get('prior').get('name'))
                    print('\tID: ', lce.get('prior').get('id'))
                except AttributeError:
                    print('\tNONE')
                print('Child LCE:')
                try:
                    print('\tName: ', lce.get('successor').get('name'))
                    print('\tID: ', lce.get('successor').get('id'))
                except AttributeError:
                    print('\tNone')
                print(helper.reset + helper.bluetext + 'Counts:')
                try:
                    print('\tContent Hosts: ', lce.get('counts').get('content_hosts'))
                    print('\tContent Views: ', lce.get('counts').get('content_views'))
                    print('\tPackages: ', lce.get('counts').get('packages'))
                    print('\tPuppet Modules: ', lce.get('counts').get('puppet_modules'))
                    print('\tYum Repos: ', lce.get('counts').get('yum_repositories'))
                    print('\tDocker Repos: ', lce.get('counts').get('docker_repositories'))
                    print('\tOStree Repos: ', lce.get('counts').get('ostree_repositories'))
                    print('\tProducts: ', lce.get('counts').get('products'))
                    print(helper.reset + helper.slatebluetext + 'Errata:')
                    print('\tSecurity: ', lce.get('counts').get('errata').get('security'))
                    print('\tBugfix: ', lce.get('counts').get('errata').get('bugfix'))
                    print('\tEnhancement: ', lce.get('counts').get('errata').get('enhancement'))
                    print('\tTotal: ', lce.get('counts').get('errata').get('total'))
                except AttributeError:
                    print('\tNone')
                print(helper.reset + helper.boldwhite + 'Counts:')
                print('\tContent Hosts: ', lce.get('counts').get('content_hosts'))
                print('\tContent Views: ', lce.get('counts').get('content_views'))
                print(helper.reset + helper.tealtext + 'Permissions:')
                print('\tCreate LCE: ', lce.get('permissions').get('created_lifecycle_environments'))
                print('\tView LCE: ', lce.get('permissions').get('view_lifecycle_environments'))
                print('\tEdit LCE: ', lce.get('permissions').get('edit_lifecycle_environments'))
                print('\tDestroy LCE: ', lce.get('permissions').get('destroy_lifecycle_environments'))
                print('\tPromote/Destroy Content View to LCE: ', lce.get('permissions').get('promote_or_remove_content_views_to_environments'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)