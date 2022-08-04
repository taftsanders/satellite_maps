#!/usr/bin/python3

import helper as helper


class RecurringLogic:

    def display(self):
            information = helper.convert('recurring_logics.json')
            for logic in information:
                print(helper.boldwhite + 'ID: ', logic.get('id'))
                print('Cron Line: ', logic.get('cron_line'))
                try:
                    print('End Time: ', logic.get('end_time'))
                except AttributeError:
                    continue
                print('Iteration: ', logic.get('iteration'))
                print('Task Group ID: ', logic.get('task_group_id'))
                print('State: ', logic.get('state'))
            print(helper.reset + helper.yellowtext + '#' * 100 + '\n' + helper.reset)
