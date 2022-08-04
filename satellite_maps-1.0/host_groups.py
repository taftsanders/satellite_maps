#!/usr/bin/python3

import satellite_maps.helper as helper


class HostGroup:

    def display(self):
        for file in helper.directory_content('hostgroups_org'):
            self.information = helper.convert(file)
            print(file)
            for group in self.information:
                print('Name: ', group.get('name'))
                print('Title: ', group.get('title'))
                print('ID: ', group.get('id'))
                print('Environment Name: ', group.get('environment_name'))
                print('Created: ', group.get('created_at'))
                print('Updated: ', group.get('updated_at'))
                print('Subnet Name: ', group.get('subnet_name'))
                print('Subnet ID: ', group.get('subnet_id'))
                print('Operating System Name: ', group.get('operatingsystem_name'))
                print('Operating System ID: ', group.get('operatingsystem_id'))
                print('Domain Name: ', group.get('domain_name'))
                print('Domain ID: ', group.get('domain_id'))
                print('Environment Name: ', group.get('environment_name'))
                print('Enviornment ID: ', group.get('environment_id'))
                print('Compute Profile Name: ', group.get('compute_profile_name'))
                print('Compute Profile ID: ', group.get('compute_profile_id'))
                print('Ancestry: ', group.get('ancestry'))
                print('Parent Name: ', group.get('parent_name'))
                print('Parent ID: ', group.get('parent_id'))
                print('Puppet Proxy ID: ', group.get('puppet_proxy_id'))
                print('Puppet CA Proxy ID: ', group.get('puppet_ca_proxy_id'))
                print('Ptable Name: ', group.get('ptable_name'))
                print('Ptable ID: ', group.get('ptable_id'))
                print('Medium Name: ', group.get('medium_name'))
                print('Medium ID: ', group.get('medium_id'))
                print('Architecture Name: ', group.get('architecture_name'))
                print('Architecture ID: ', group.get('architecture_id'))
                print('Realm Name: ', group.get('realm_name'))
                print('Realm ID: ', group.get('realm_id'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)