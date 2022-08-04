#!/usr/bin/python3

import satellite_maps.helper as helper


class OpenscapPolicy:

    def display(self):
            information = helper.convert('openscap_policies_list.json')
            for scap in information:
                print(helper.magentatext + 'Name: ', scap.get('name'))
                print(helper.reset + helper.bluetext + 'ID: ', scap.get('id'))
                print('Created at: ', scap.get('created_at'))
                print('Updated at: ', scap.get('updated_at'))
                print('Description: ', scap.get('description'))
                print('SCAP Content ID: ', scap.get('scap_content_id'))
                print('SCAP Content Profile ID: ', scap.get('scap_content_profile_id'))
                print(helper.reset + helper.greentext + 'Interval: ', scap.get('period'))
                print('Weekday: ', scap.get('weekday'))
                print('Day of the Month: ', scap.get('day_of_month'))
                print('Cron Line: ', scap.get('cron_line'))
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
