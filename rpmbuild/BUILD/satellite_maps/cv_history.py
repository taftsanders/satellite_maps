#!/usr/bin/python3

import helper as helper


class ContentViewHistory:

    def display(self):
        for file in helper.directory_content('cv_history_'):
            self.information = helper.convert(file)
            for entry in self.information:
                #name = entry.get('task').get('input').get('content_view').get('name')
                if entry.get('task').get('label') != 'Actions::Katello::ContentView::IncrementalUpdates':
                    print(helper.magentatext + 'Content View: ', entry.get('task').get('input').get('content_view').get('name'))
                    print('Version: ', entry.get('version'))
                    print(helper.reset + helper.greentext + 'Created at: ', entry.get('created_at'))
                    print('Updated at: ', entry.get('updated_at'))
                    print('Description: ', entry.get('task').get('description'))
                    print('Organization: ', entry.get('task').get('input').get('organization').get('name'))
                    try:
                        print('Lifecycle Environment: ', entry.get('environment').get('name'))
                    except AttributeError:
                        print('Lifecycle Environment: None')
                    print('')
                    print(helper.reset + helper.tealtext + 'Task:')
                    print('\tID: ', entry.get('task').get('id'))
                    print('\tLabel: ', entry.get('task').get('label'))
                    print(helper.reset + helper.boldwhite + '\tTask type: ', entry.get('task').get('humanized').get('action'))
                    print(helper.reset + helper.tealtext + '\tStarted at: ', entry.get('task').get('started_at'))
                    print('\tFinished at: ', entry.get('task').get('ended_at'))
                    print('\tPending: ', entry.get('task').get('pending'))
                    print('\tState: ', entry.get('task').get('state'))
                    print('\tResult: ', entry.get('task').get('result'))
                    if entry.get('task').get('label') == 'Actions::Katello::ContentView::IncrementalUpdates':
                        for output in entry.get('task').get('version_output'):
                            print('\tErrata added: ', output.get('output').get('added_units').get('erratum'))
                            print('\tRPMs added: ', output.get('output').get('added_units').get('rpm'))
                            print('\tPuppet Modules added: ', output.get('output').get('added_units').get('puppet_module'))
                    print(helper.reset + helper.redtext + 'Errors: ', entry.get('task').get('humanized').get('errors'))
                    print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
                else:
                    #print('Content View: ', name)
                    print(helper.magentatext + 'Version: ', entry.get('version'))
                    print(helper.reset + helper.greentext + 'Created at: ', entry.get('created_at'))
                    print('Updated at: ', entry.get('updated_at'))
                    try:
                        print('Lifecycle Environment: ', entry.get('environment').get('name'))
                    except AttributeError:
                        print('Lifecycle Environment: None')
                    print('Description: ', entry.get('task').get('description'))
                    print(helper.reset + helper.tealtext + 'Task:')
                    print('\tID: ', entry.get('task').get('id'))
                    print('\tLabel: ', entry.get('task').get('label'))
                    print('\tTask type: ', entry.get('task').get('humanized').get('action'))
                    print('\tStarted at: ', entry.get('task').get('started_at'))
                    print('\tFinished at: ', entry.get('task').get('ended_at'))
                    print('\tPending: ', entry.get('task').get('pending'))
                    print('\tState: ', entry.get('task').get('state'))
                    print('\tResult: ', entry.get('task').get('result'))
                    for output in entry.get('task').get('input').get('version_outputs'):
                       print('\tErrata added: ') #output.get('output').get('added_units').get('erratum'))
                       output.get('output').get('added_units').get('erratum').sort()
                       for errata in output.get('output').get('added_units').get('erratum'):
                           print('\t\t' + errata)
                       print('\tRPMs added: ') #, output.get('output').get('added_units').get('rpm'))
                       output.get('output').get('added_units').get('rpm').sort()
                       for rpm in output.get('output').get('added_units').get('rpm'):
                           print('\t\t' + rpm)
                       print('\tPuppet Modules added: ') #output.get('output').get('added_units').get('puppet_module'))
                       output.get('output').get('added_units').get('puppet_module').sort()
                       for mod in output.get('output').get('added_units').get('puppet_module'):
                           print('\t\t' + mod)
                    print(helper.reset + helper.redtext + 'Errors: ', entry.get('task').get('humanized').get('errors'))
                    print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
        print(helper.reset + helper.greentext + '#' * 100 + '\n' + helper.reset)

