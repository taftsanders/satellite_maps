#!/usr/bin/python3

import helper as helper
import json


class Capsule_LCE_Available:

    def convert(self, file_name):
        with open(file_name) as file:
            datastore = json.load(file)
            information = datastore['results']
            return information


    def display(self):
        for file in helper.directory_content('capsule_lce_available_cap'):
            self.information = self.convert(file)
            for lce in self.information:
                print(helper.greentext + 'Organization: ')
                print('Name: ', lce.get('organization').get('name'))
                print('Label: ', lce.get('organization').get('label'))
                print('ID: ', lce.get('organization').get('id'))
                print('Is Library: ', lce.get('library'))
                print(helper.reset + helper.bluetext + '\tName: ', lce.get('name'))
                print('\tLabel: ', lce.get('label'))
                print('\tID: ', lce.get('id'))
                print('\tDescription: ', lce.get('description'))
                print('\tCreated: ', lce.get('created_at'))
                print('\tUpdated: ', lce.get('updated_at'))
                print('\tParent: ')
                try:
                    print('\t\tName: ', lce.get('prior').get('name'))
                    print('\t\tID: ', lce.get('prior').get('id'))
                except AttributeError:
                    print('\t\tNone')
                print('\tChild: ')
                try:
                    print('\t\tName: ', lce.get('successor').get('name'))
                    print('\t\tID: ', lce.get('successor').get('id'))
                except AttributeError:
                    print('\t\tNone')
                print(helper.reset + helper.magentatext + '\tCounts: ')
                print('\t\tHosts: ', lce.get('counts').get('content_hosts'))
                print('\t\tContent Views: ', lce.get('counts').get('content_views'))
                print('\t\tPackages: ', lce.get('counts').get('packages'))
                print('\t\tPuppet Modules: ', lce.get('counts').get('puppet_modules'))
                print('\t\tYum Repos: ', lce.get('counts').get('yum_repositories'))
                print('\t\tDocker Repos: ', lce.get('counts').get('docker_repositories'))
                print('\t\tOStree Repos: ', lce.get('counts').get('ostree_repositories'))
                print('\t\tProducts: ', lce.get('counts').get('products'))
                print('\tErrata: ')
                try:
                    print('\t\tSecurity: ', lce.get('counts').get('errata').get('security'))
                    print('\t\tBugfix: ', lce.get('counts').get('errata').get('bugfix'))
                    print('\t\tEnhancement: ', lce.get('counts').get('errata').get('enhancement'))
                    print('\t\tTotal: ', lce.get('counts').get('errata').get('total'))
                except AttributeError:
                    print('\t\tNone')
                print(helper.reset + '\tPermissions: ')
                print('\t\tCreate LCE: ', lce.get('permissions').get('create_lifecycle_environments'))
                print('\t\tView LCE: ', lce.get('permissions').get('view_lifecycle_environments'))
                print('\t\tEdit LCE: ', lce.get('permissions').get('edit_lifecycle_environments'))
                print('\t\tDestroy LCE: ', lce.get('permissions').get('destroy_lifecycle_environments'))
                print('\t\tPromote/Destroy Content Views: ',
                      lce.get('permissions').get('promote_or_remove_content_views_to_environments'))
                print(helper.yellowtext + '#' * 50 + 'END OF ' + lce.get('organization').get('name') + '|' +
                      lce.get('name') + '#' * 50 + '\n' + helper.reset)
