#!/usr/bin/python3

import helper as helper
import json


class Capsule_LCE_Assigned:

    def convert(self, file_name):
        with open(file_name) as file:
            information = json.load(file)
            return information

    def display(self):
        for file in helper.directory_content('capsule_lce_assigned_cap'):
            self.information = self.convert(file)
            print(helper.greentext + 'Last Sync: ', self.information.get('last_sync_time'))
            print('Active Sync Tasks: ', self.information.get('active_sync_tasks'))
            print('Last Failed Sync: ', self.information.get('last_failed_sync_tasks'))
            for capsule in self.information.get('lifecycle_environments'):
                print(helper.greentext + '\tLCE Organization: ', capsule.get('organization').get('name'))
                print(helper.greentext + '\tLCE Name: ', capsule.get('name'))
                print(helper.greentext + '\tLCE ID: ', capsule.get('id'))
                print(helper.greentext + '\tLCE Label: ', capsule.get('label'))
                print(helper.reset + helper.bluebg + 'Number of: ' + helper.reset)
                print(helper.bluetext + '\tHosts on this LCE: ', capsule.get('counts').get('content_hosts'))
                print('\tContent Views for this LCE: ', capsule.get('counts').get('content_views'))
                print('\tProducts associated with this LCE: ', capsule.get('counts').get('products'))
                print('\tYum Repos associated with this LCE: ', capsule.get('counts').get('yum_repositories'))
                print('\tPackages associated with this LCE: ', capsule.get('counts').get('packages'))
                print('\tPackage Groups associated with this LCE: ', capsule.get('counts').get('package_groups'))
                print('\tErrata associated with this LCE: ', capsule.get('counts').get('errata'))
                print('\tPuppet Repos associated with this LCE: ', capsule.get('counts').get('puppet_repositories'))
                print('\tPuppet Modules associated with this LCE: ', capsule.get('counts').get('puppet_modules'))
                print('\tDocker Repos associated with this LCE: ', capsule.get('counts').get('docker_repositories'))
                print('\tDocker Images associated with this LCE: ', capsule.get('counts').get('docker_images'))
                print(helper.reset + helper.tealbg + 'Content Views: ' + helper.reset)
                for cv in capsule.get('content_views'):
                    print(helper.tealtext + '\tName: ', cv.get('name'))
                    print('\tLabel: ', cv.get('label'))
                    print('\tID: ', cv.get('id'))
                    print('\tComposite View?: ', cv.get('composite'))
                    print('\tLast Published: ', cv.get('last_published'))
                    print('\tHosts: ', cv.get('counts').get('content_hosts'))
                    print('\tProducts: ', cv.get('counts').get('products'))
                    print('\tYum Repos: ', cv.get('counts').get('yum_repositories'))
                    print('\tPackages: ', cv.get('counts').get('packages'))
                    print('\tPackage Groups: ', cv.get('counts').get('package_groups'))
                    print('\tErrata: ', cv.get('counts').get('errata'))
                    print('\tPuppet Repos: ', cv.get('counts').get('puppet_repositories'))
                    print('\tPuppet Modules: ', cv.get('counts').get('puppet_modules'))
                    print('\tDocker Repos: ', cv.get('counts').get('docker_repositories'))
                    print('\tDocker Images: ', cv.get('counts').get('docker_images'))
                    print(helper.tealbg + '####END OF ' + cv.get('name') + '####' + helper.reset)
                print(helper.yellowtext + '#' * 50 + 'END OF ' + capsule.get('name') + '#' * 50 + '\n' + helper.reset)
            print(helper.redtext + '#' * 50 + 'END OF CAPSULE' + '#' * 50 + '\n' + helper.reset)

