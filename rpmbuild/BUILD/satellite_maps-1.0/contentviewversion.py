#!/usr/bin/python3

import satellite_maps.helper as helper


class ContentViewVersion:

    def __init__(self):
        self.information = helper.convert('contentviewversions.json')

    def display(self):
        for ver in self.information:
            print(helper.greentext + 'Name: ', ver.get('name'))
            print('Content View: ', ver.get('content_view').get('name'))
            print('Version: ', ver.get('version'))
            print('Created: ', ver.get('created_at'))
            print('Updated: ', ver.get('updated_at'))
            print(helper.reset + helper.bluebg + 'Lifecycle Environments: ' + helper.reset)
            for lce in ver.get('environments'):
                print(helper.bluetext + '\tName: ', lce.get('name'))
                print('\tSystem count: ', lce.get('system_count'))
                print('\tActivation Key Count: ', lce.get('activation_key_count'))
            print(helper.reset + helper.darkredbg + 'Repositories:' + helper.reset)
            for repo in ver.get('repositories'):
                print(helper.darkredtext + '\tName: ', repo.get('name'))
                print('\tLabel: ', repo.get('label'))
                print('\tID: ', repo.get('id'))
            print(helper.reset + helper.magentabg + 'Content Count:' + helper.reset)
            print(helper.magentatext + '\tPackages: ', ver.get('package_count'))
            print('\t\tSecurity: ', ver.get('errata_counts').get('security'))
            print('\t\tBugfix: ', ver.get('errata_counts').get('bugfix'))
            print('\t\tEnhancement: ', ver.get('errata_counts').get('enhancement'))
            print('\t\tTotal: ', ver.get('errata_counts').get('total'))
            print('\tPuppet Modules: ', ver.get('puppet_module_count'))
            print('\tDocker Manifests: ', ver.get('docker_manifest_counts'))
            print('\tDocker Tags: ', ver.get('docker_tag_count'))
            print('\tOStree Brances: ', ver.get('ostree_branch_count'))
            print(helper.reset + helper.orangebg + 'Last Event Info:' + helper.reset)
            try:
                print(helper.orangetext + '\tTask ID: ', ver.get('last_event').get('task').get('id'))
                print('\tTask Label: ', ver.get('last_event').get('task').get('label'))
                print('\tTask State: ', ver.get('last_event').get('task').get('state'))
                print('\tTask Result: ', ver.get('last_event').get('task').get('result'))
                print('\tTask Progress: ', ver.get('last_event').get('task').get('progress'))
                print('\tTask Errors: ')
                for error in ver.get('last_event').get('task').get('humanized').get('errors'):
                    print(error)
                if ver.get('last_event').get('task').get('label') == 'Actions::Katello::ContentView::IncrementalUpdates':
                    print('')
                    print(helper.reset + helper.redtext + 'Incremental Update Includes:')
                    for outputs in ver.get('last_event').get('task').get('input').get('version_outputs'):
                        print('Erratum: ')
                        for errata in outputs.get('output').get('added_units').get('erratum'):
                            print('\t' + errata)
                        print('')
                        print('RPM: ')
                        for rpm in outputs.get('output').get('added_units').get('rpm'):
                            print('\t' + rpm)
                        print('')
                        print('Puppet Modules: ')
                        for puppet in outputs.get('output').get('added_units').get('puppet_module'):
                            print('\t' + puppet)
            except AttributeError:
                print(helper.orangetext + 'None' + helper.reset)
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)

