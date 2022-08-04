#!/usr/bin/python3

import satellite_maps.helper as helper
import json


class PulpTasks:

    def display(self):
        for file in helper.directory_content('pulp_tasks.json'):
            with open(file) as data:
                detail = json.load(data)
            for task in detail:
                print(helper.reset + helper.magentatext + 'ID: ', task.get('id'))
                print('Href/API reference: ', task.get('_href'))
                print('Task ID: ', task.get('task_id'))
                print('Worker ID: ', task.get('worker_name'))
                print('Start Time: ', task.get('start_time'))
                print('Finish Time: ', task.get('finish_time'))
                print(helper.reset + helper.redtext + 'Error: ', json.dumps(task.get('error'), indent=4, sort_keys=True))
                print('Exception: ', task.get('exception'))
                print('Traceback: ', task.get('traceback'))
                print(helper.reset + helper.greentext + 'State: ', task.get('state'))
                print('Task ID: ', task.get('task_id'))
                print('Task Type: ', task.get('task_type'))
                print(helper.reset + '')
                print(helper.bluetext + 'Task Tags:')
                for tag in task.get('tags'):
                    print('\t', tag)
                print(helper.reset + '')
                print(helper.orangetext + 'Progress Report:')
                try:
                    for key in task.get('progress_report'):
                        print('\t', key)
                        for report in task.get('progres_report').get(key):
                            print('\t\t + Step ID: ', report.get('step_id'))
                            print('\t\t + Step Type: ', report.get('step_type'))
                            print('\t\t + Description: ', report.get('description'))
                            print('\t\t + State: ' , report.get('state'))
                            print('\t\t + Details: ', report.get('details'))
                            print('\t\t + Error Details: ', report.get('error_details'))
                            print('\t\t + Failures: ', report.get('num_failures'))
                            print('\t\t + Processed: ', report.get('num_processed'))
                            print('\t\t + Success: ', report.get('num_success'))
                except AttributeError:
                    pass
                print(helper.reset + '')
                print(helper.yellowtext + 'Result: ', json.dumps(task.get('result'), indent=4, sort_keys=True))
                print('')
                print(helper.redtext + '#' * 50 + 'END OF TASK' + '#' * 50 + '\n' + helper.reset)
