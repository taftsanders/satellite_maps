#!/usr/bin/python3

import helper as helper


class UserList:

    def display(self):
            information = helper.convert('user_list.json')
            for user in information:
                print(helper.magentatext + 'Username: ', user.get('login'))
                print(helper.reset + helper.redtext + 'Sat Admin: ', user.get('admin'))
                print(helper.reset + helper.bluetext +'ID: ', user.get('id'))
                print('Created: ', user.get('created_at'))
                print('Updated: ', user.get('updated_at'))
                print('Auth Source: ', user.get('auth_source_name'))
                print(helper.reset + helper.greentext + 'First Name: ', user.get('firstname'))
                print('Last Name: ', user.get('lastname'))
                print('Email: ', user.get('mail'))
                print('Last Login: ', user.get('last_login_on'))
                try:
                    print(helper.reset + helper.orangetext + 'Default Organization: ', user.get('default_organization').get('name'))
                    print('Default Organization ID: ', user.get('default_organization').get('id'))
                except AttributeError:
                    print(helper.reset + helper.orangetext + 'Default Organization: None')
                try:
                    print('Default Location: ', user.get('default_location'))
                except AttributeError:
                    print('Default Location: None')
                print('Timezone: ', user.get('timezone'))
                try:
                    print('Locale: ', user.get('locale'))
                except AttributeError:
                    print('Locale: Null')
                print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
