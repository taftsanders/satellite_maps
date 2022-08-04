#!/usr/bin/python3

import satellite_maps.helper as helper


class ComputeProfile:

    def __init__(self):
        self.information = helper.convert('compute_profiles.json')

    def display(self):
        for profile in self.information:
            print(helper.tealbg + 'Name: ', profile.get('name'))
            print(helper.reset + helper.tealtext + 'ID: ', profile.get('id'))
            print('Created: ', profile.get('created_at'))
            print('Updated: ', profile.get('updated_at'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
