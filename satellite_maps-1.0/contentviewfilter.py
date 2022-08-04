#!/usr/bin/python3

import satellite_maps.helper as helper


class ContentViewFilter:

    def __init__(self):
        self.information = helper.convert('contentviewfilters.json')

    def display(self):
        for filter in self.information:
            print(helper.greentext + 'Name: ', filter.get('name'))
            print('ID: ', filter.get('id'))
            print('Created: ', filter.get('created_at'))
            print('Updated: ', filter.get('updated_at'))
            print('Description: ', filter.get('description'))
            print('Inclusion/Exclusion: ')
            if filter.get('inclusion') is False:
                print('Exclusion')
            else:
                print('Inclusion')
            print(helper.reset + '')
            print(helper.bluebg + 'Content View: ' + helper.reset)
            print(helper.bluetext + '\tName: ', filter.get('content_view').get('name'))
            print('\tLabel: ', filter.get('content_view').get('label'))
            print('\tID: ', filter.get('content_view').get('id'))
            print('\tOrganization: ', filter.get('content_view').get('organization').get('name'))
            print(helper.reset + helper.darkredbg + 'Lifecycle Environment: ' + helper.reset)
            for lce in filter.get('content_view').get('environments'):
                print(helper.reset + helper.darkredtext + '\t - ', lce.get('name'))
            print(helper.reset + helper.tealbg + 'Repositories: ' + helper.reset)
            for repo in filter.get('content_view').get('repositories'):
                print(helper.reset + helper.tealtext + '\t - ', repo.get('name'))
            print(helper.reset + helper.magentabg + 'Versions: ' + helper.reset)
            for version in filter.get('content_view').get('versions'):
                print(helper.reset + helper.magentatext + '\t - ', version.get('version'))
            print(helper.reset + helper.orangebg + 'Rules: ' + helper.reset)
            for rule in filter.get('rules'):
                print(helper.orangetext + '\tName: ', rule.get('name'))
                print('\tID: ', rule.get('id'))
                print('\tCreated: ', rule.get('created_at'))
                print('\tUpdated: ', rule.get('updated_at'))
                print('\tFilter ID: ', rule.get('content_view_filter_id'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
