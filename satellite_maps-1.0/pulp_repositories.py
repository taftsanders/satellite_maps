#!/usr/bin/python3

import satellite_maps.helper as helper
import json


class PulpRepositories:

    def display(self):
        for file in helper.directory_content('pulp_repositories.json'):
            with open(file) as data:
                detail = json.load(data)
            for repo in detail:
                print(helper.magentatext + 'ID: ', repo.get('id'))
                print('HREF: ', repo.get('_href'))
                print('Display Name: ', repo.get('display_name'))
                print('Description: ', repo.get('description'))
                print(helper.reset + helper.orangetext + 'Repo Type: ', repo.get('notes').get('_repo-type'))
                print(helper.reset + helper.slatebluetext + 'Last Unit Added: ', repo.get('last_unit_added'))
                print('Last Unit Removed: ', repo.get('last_unit_removed'))
                print(helper.reset + helper.yellowtext + 'Content Unit Counts:')
                for key in repo.get('content_unit_counts'):
                    print(key + ':', repo.get('content_unit_counts').get(key))
                print(helper.redtext + '#' * 50 + 'END OF REPO' + '#' * 50 + '\n' + helper.reset)
