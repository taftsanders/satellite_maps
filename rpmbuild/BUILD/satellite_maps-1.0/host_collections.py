#!/usr/bin/python3

import satellite_maps.helper as helper


class HostCollection:

    def display(self):
        for file in helper.directory_content('host_collections_org'):
            self.information = helper.convert(file)
            print(file)
            print('')
            for collection in self.information:
                print(helper.magentatext + 'Name: ', collection.get('name'))
                print(helper.reset + helper.bluetext + 'ID: ', collection.get('id'))
                print('Created: ', collection.get('created_at'))
                print('Updated: ', collection.get('updated_at'))
                print('Description: ', collection.get('description'))
                print('Organization ID: ', collection.get('organization_id'))
                print('Unlimited Hosts: ', collection.get('unlimited_hosts'))
                print('Max Hosts: ', collection.get('max_hosts'))
                print('Total Hosts: ', collection.get('total_hosts'))
                print(helper.reset + helper.boldwhite + 'Permissions')
                print('\tDeletable: ', collection.get('permissions').get('deletable'))
                print('\tEditable: ', collection.get('permissions').get('editable'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
