import satellite_maps.helper as helper
import json


class HammerPing:

    def convert(self, file_name):
        with open(file_name) as file:
            information = json.load(file)
            return information


    def display(self):
        information = self.convert('hammer_ping.json')
        print(helper.redtext + 'Overall Status: ', information.get('status'))
        print('')
        print(helper.reset + helper.yellowtext + 'Status: ')
        print('\tForeman Tasks: ', information.get('services').get('foreman_tasks').get('status'))
        print('\tCandlepin: ', information.get('services').get('candlepin').get('status'))
        print('\tCandlepin Auth: ', information.get('services').get('candlepin_auth').get('status'))
        print('\tPulp: ', information.get('services').get('pulp').get('status'))
        print('\tPulp Auth: ', information.get('services').get('pulp_auth').get('status'))
        try:
            print('\tForeman Auth: ', information.get('services').get('foreman_auth').get('status'))
        except AttributeError:
            print('\tForeman Auth: {}')
        print('')
        print(helper.reset + helper.orangetext + 'Ping Time:')
        print('\tForeman Tasks: ', information.get('services').get('foreman_tasks').get('duration_ms'))
        print('\tCandlepin: ', information.get('services').get('candlepin').get('duration_ms'))
        print('\tCandlepin Auth: ', information.get('services').get('candlepin_auth').get('duration_ms'))
        print('\tPulp: ', information.get('services').get('pulp').get('duration_ms'))
        print('\tPulp Auth: ', information.get('services').get('pulp_auth').get('duration_ms'))
        try:
            print('\tForeman Auth: ', information.get('services').get('foreman_tasks').get('duration_ms'))
        except AttributeError:
            print('\tForeman Auth: {}')
        print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)