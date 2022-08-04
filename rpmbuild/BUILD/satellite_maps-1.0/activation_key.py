#!/usr/bin/env python3

import satellite_maps.helper as helper


class ActivationKey:

    def get_products(self, data):
        return [data.get('products') if data.get('products') is not None else []]

    def display(self):
        for file in helper.directory_content('activationkey_org'):
            self.information = helper.convert(file)
            for ak in self.information:
                print(helper.greentext + 'Name: ', ak.get('name'))
                print('ID: ', ak.get('id'))
                print('Created: ', ak.get('created_at'))
                print('Updated: ', ak.get('updated_at'))
                print('Description: ', ak.get('description'))
                print(helper.reset + helper.orangebg + 'Organization: ' + helper.reset)
                print(helper.orangetext + '\tName: ', ak.get('organization').get('name'))
                print('\tLabel: ', ak.get('organization').get('label'))
                print('\tID: ', ak.get('organization').get('id'))
                print(helper.reset + helper.bluebg + 'Lifecycle Environment: ' + helper.reset)
                print(helper.bluetext + '\tName: ', ak.get('environment').get('name'))
                print('\tID: ', ak.get('environment').get('id'))
                print(helper.reset + helper.magentatext + 'Auto-attach: ', ak.get('auto_attach'))
                print('Unlimited use: ', ak.get('unlimited_hosts'))
                print('Max Count: ', ak.get('max_hosts'))
                print('Usage count: ', ak.get('usage_count'))
                print('Release version: ', ak.get('release_version'))
                print('Service level: ', ak.get('service_level'))
                print(helper.reset + helper.tealbg + 'Content View: ' + helper.reset)
                print(helper.tealtext + '\tName: ', ak.get('content_view').get('name'))
                print('\tID: ', ak.get('content_view').get('id'))
                print(helper.reset + helper.tealbg + 'Content Overrides: ' + helper.reset)
                for override in ak.get('content_overrides'):
                    print(helper.reset + helper.tealtext + '\tRepository: ', override.get('contentLabel'))
                    print('\tEnabled/Disabled: ', override.get('name'))
                print(helper.reset + helper.darkredbg + 'Products: ' + helper.reset)
                for product in self.get_products(ak):
                    if product != []:
                        for i in product:
                            print(helper.darkredtext + '\tName: ', i.get('name'))
                            print('\tID: ', i.get('id'))
                print(helper.reset + helper.darkredbg + 'Host Collection: ' + helper.reset)
                for hc in ak.get('host_collections'):
                    if hc == []:
                        print(helper.darkredtext + 'None')
                    else:
                        print(helper.darkredtext + '\tName: ', hc.get('name'))
                        print('\tID: ', hc.get('id'))
                print(helper.reset + 'Permissions: ')
                print('\tView: ', ak.get('permissions').get('view_activation_keys'))
                print('\tEdit: ', ak.get('permissions').get('edit_activation_keys'))
                print('\tDestroy: ', ak.get('permissions').get('destroy_activation_keys'))
                print(helper.yellowtext + '#' * 100 + '\n' + helper.reset)
