#!/usr/bin/python3

import satellite_maps.helper as helper
# import LCE to replace 'environment id #'s       #RFE


class ContentView:

    def display(self):
        for file in helper.directory_content('content_views_org'):
            self.information = helper.convert(file)
            for cv in self.information:
                print(helper.greentext + 'Name: ', cv.get('name'))
                print('Label: ', cv.get('label'))
                print('ID: ', cv.get('id'))
                print('Description: ', cv.get('description'))
                print('Created: ', cv.get('created_at'))
                print('Updated: ', cv.get('updated_at'))
                print('Last Published: ', cv.get('last_published'))
                print('Organization: ', cv.get('organization').get('name'))
                print('Lifecycle Environments: ')
                for env in cv.get('environments'):
                    print('\t - ', env.get('name'))
                print(helper.reset + '')
                print(helper.tealtext + 'Composite?: ', cv.get('composite'))
                print(helper.reset + helper.orangebg + 'Content Views: ' + helper.reset)
                if cv.get('components'):
                    for cview in cv.get('components'):
                        print(helper.orangetext + '\tName: ', cview.get('content_view').get('name'))
                        print('\tVersion ', cview.get('version'))
                        print('\tPuppet Modules: ', cview.get('puppet_module_count'))
                        print('')
                else:
                    print(helper.orangetext + 'None')
                print(helper.reset + helper.darkredbg + 'Repositories: ' + helper.reset)
                if cv.get('repositories'):
                    for repo in cv.get('repositories'):
                        print(helper.darkredtext + '\tName: ', repo.get('name'))
                        print('\tLabel: ', repo.get('label'))
                        print('\tID: ', repo.get('id'))
                        print('\tContent Type: ', repo.get('content_type'))
                else:
                    print(helper.darkredtext + 'None')
                print(helper.reset + helper.bluebg + 'Versions: ' + helper.reset)
                if cv.get('versions'):
                    for ver in cv.get('versions'):
                        print(helper.bluetext + '\tVersion: ', ver.get('version'))
                        print('\tID: ', ver.get('id'))
                        print('\tPublished: ', ver.get('published'))
                        print('\tEnvironment ID: ')
                        for id in ver.get('environment_ids'):
                            print('\t - ', id)
                else:
                    print(helper.bluetext + 'None')
                print(helper.reset + helper.magentabg + 'Puppet Modules: ' + helper.reset)
                if cv.get('puppet_modules'):
                    for mod in cv.get('puppet_modules'):
                        print(helper.magentatext + '\tName: ', mod.get('name'))
                else:
                    print(helper.magentatext + 'None')
                print(helper.yellowtext + '#' * 100 + '\n' + helper.reset)

