#!/usr/bin/python3

import helper as helper


class RexFeatures:

    def display(self):
            information = helper.convert('rex_features.json')
            for rex in information:
                print(helper.magentatext + 'Name: ', rex.get('name'))
                print('Label: ', rex.get('label'))
                print(helper.reset + helper.bluetext + 'ID: ', rex.get('id'))
                print('Description: ', rex.get('description'))
                print('Job Template Name: ', rex.get('job_template_name'))
                print('Job Template ID: ', rex.get('job_template_id'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
