#!/usr/bin/python3

import os
import tarfile
import sys
import helper as helper


class Maps(object):

    def __init__(self):
        self.file_name = input('Please input the name of the file: ')

    def open_file(self):
        if tarfile.is_tarfile(self.file_name):
            tar = tarfile.open(self.file_name)
            tar.extractall()
            tar.close()
            extract_dir = self.file_name[:-7]
            os.chdir(extract_dir)
        else:
            print('This file is not a valid tar file')
            sys.exit(0)

    def header(self, message):
        print((helper.greenbluetext + '#' * 100 + '\n') * 2 + helper.reset)
        print(message)
        print((helper.greenbluetext + '#' * 100 + '\n') * 2 + helper.reset)

    def main(self):
        self.open_file()
        print('Welcome to Satellite Maps!')
        try:
            print('\t 1. Organizations')
            print('\t 2. Locations')
            print('\t 3. Activation Keys')
            print('\t 4. Architectures')
            print('\t 5. Bookmarks')
            print('\t 6. Capsule LifeCycle Env. Assignment')
            print('\t 7. Capsule LifeCycle Env. Available')
            print('\t 8. Capsule List')
            print('\t 9. Compute Profiles')
            print('\t 10. Compute Resource')
            print('\t 11. Config Templates')
            print('\t 12. Content View Filter')
            print('\t 13. Content View')
            print('\t 14. Content Views by Version')
            print('\t 15. Content View History by Content View')
            print('\t 16. Puppet Modules by Content View')
            print('\t 17. Dashboard')
            print('\t 18. Discovery Rules')
            print('\t 19. Discovered Hosts')
            print('\t 20. Docker Containers')
            print('\t 21. Docker Manifest')
            print('\t 22. Docker Registry')
            print('\t 23. Docker Tags')
            print('\t 24. Domain List')
            print('\t 25. Hammer Ping')
            print('\t 26. Host Collections')
            print('\t 27. Hosts')
            print('\t 28. Life Cycle Environments')
            print('\t 29. Manifest History')
            print('\t 30. Media')
            print('\t 31. OpenSCAP Content')
            print('\t 32. OpenSCAP Policies')
            print('\t 33. OS List')
            print('\t 34. Products')
            print('\t 35. Provisioning Templates')
            print('\t 36. Puppet Environments')
            print('\t 37. Recurring Logics')
            print('\t 38. Rex Features')
            print('\t 39. Rex History')
            print('\t 40. Satellite Task Summary')
            print('\t 41. Statistics')
            print('\t 42. Settings')
            print('\t 43. Subscription-Manager Facts')
            print('\t 44. Subnet List')
            print('\t 45. Subscriptions')
            print('\t 46. Sync Plans')
            print('\t 47. Template Type')
            print('\t 48. User List')


            selection = int(input('Choose your own adventure: '))
            if selection == 1:
                from organization import Organization
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Organizations page. Below you will find the '
                                               'Organizations from the Satellite: ')
                org = Organization()
                org.display()

            elif selection == 2:
                from location import Location
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Locations page. Below you will find the Locations from '
                                               'the Satellite')
                loc = Location()
                loc.display()

            elif selection == 3:
                from activation_key import ActivationKey
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Activation Keys page. Below you will find the '
                                               'Activation Keys from the Satellite')
                ak = ActivationKey()
                ak.display()

            elif selection == 4:
                from arch_list import Arch_List
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Architecture page. Below you will find the Architecture '
                                               'types from the Satellite')
                arch = Arch_List()
                arch.display()

            elif selection == 5:
                from bookmark import Bookmark
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Bookmarks page. Below you will find the Bookmarked '
                                               'search strings from the Satellite')
                book = Bookmark()
                book.display()

            elif selection == 6:
                from capsule_lce_assigned import Capsule_LCE_Assigned
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Capsule LCE Assignment page. Below you will find the '
                                               'various lifecycles assigned to each Capsule server')
                cap_lce_asg = Capsule_LCE_Assigned()
                cap_lce_asg.display()

            elif selection == 7:
                from capsule_lce_available import Capsule_LCE_Available
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Capsule LCE Available page. Below you will find the '
                                               'various lifecycle available to each Capsule')
                cap_lce_aval = Capsule_LCE_Available()
                cap_lce_aval.display()

            elif selection == 8:
                from capsule_list import CapsuleList
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Capsule list page. Below you will find the list of '
                                               'all capsules and internal Capsule.')
                capsule = CapsuleList()
                capsule.display()

            elif selection == 9:
                from compute_profile import ComputeProfile
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Compute Profiles page. Below you will find the list of'
                                               ' compute profiles for the Satellite.')
                profile = ComputeProfile()
                profile.display()

            elif selection == 10:
                from compute_resource import ComputeResource
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Compute Resources page. Below you will find the list of'
                                               ' all configured compute resources on the Satellite.')
                resource = ComputeResource()
                resource.display()

            elif selection == 11:
                from config_template import ConfigTemplate
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Configuration Template page. Below you will find a list'
                                               ' of all configuration templates on the Satellite.')
                template = ConfigTemplate()
                template.display()

            elif selection == 12:
                from contentviewfilter import ContentViewFilter
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Content View Filter page. Below is all the content view'
                                               ' filters on the Satellite')
                cvfilter = ContentViewFilter()
                cvfilter.display()

            elif selection == 13:
                from content_view import ContentView
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Content View page. Below is all the content views by '
                                                'Organization from the Satellite.')
                cv = ContentView()
                cv.display()

            elif selection == 14:
                from contentviewversion import ContentViewVersion
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Content View Version page. Below is all content view'
                                               ' by versions on the Satellite.')
                ver = ContentViewVersion()
                ver.display()

            elif selection == 15:
                from cv_history import ContentViewHistory
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Content View History page. Below is the history of each'
                                               ' content view.')
                cvhist = ContentViewHistory()
                cvhist.display()

            elif selection == 16:
                from cv_puppet_modules import ContentViewPuppetMods
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Puppet Modules by Content View page. Below is a list of '
                                               'all puppet modules included in each Content View')
                mod = ContentViewPuppetMods()
                mod.display()

            elif selection == 17:
                from dashboard import Dashboard
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Dashboard Page. All those little graphics on the page '
                                               'after logging in can be found here in text format.')
                dash = Dashboard()
                dash.display()

            elif selection == 18:
                from discovery_rules import DiscoveryRules
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Discovery Rules page. Here you can find the discovery '
                                               'rules from the Satellite.')
                rule = DiscoveryRules()
                rule.display()

            elif selection == 19:
                from discovered_hosts import DiscoveredHosts
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Discovered Hosts page. Here you can find all discovered '
                                               'hosts from the Satellite.')
                dhost = DiscoveredHosts()
                dhost.display()

            elif selection == 20:
                from docker_containers import DockerContainers
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Docker Containers page. Here you can find all Docker '
                                               'containers associated with the Satellite.')
                container = DockerContainers()
                container.display()

            elif selection == 21:
                from dockermanifests import DockerManifest
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Docker Manifests page. Here you can find all Docker '
                                               'manifests associated with the Satellite.')
                manifest = DockerManifest()
                manifest.display()

            elif selection == 22:
                from docker_registries import DockerRegistry
                os.system('clear')
                self.header(helper.boldwhite + "Welcome to the Docker Registries page. Here you can find all Docker "
                                               "registries associated with the Satellite's Docker content.")
                reg = DockerRegistry()
                reg.display()

            elif selection == 23:
                from dockertags import DockerTag
                os.system('clear')
                self.header(helper.boldwhite + "Welcome to the Docker Tags page. Here you can find all Docker tags "
                                               "associated with the Satellite's Docker content.")
                tag = DockerTag()
                tag.display()

            elif selection == 24:
                from domainlist import DomainList
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Domain List page. Here you can find all '
                                               'domains associated with the Satellite ')
                domain = DomainList()
                domain.display()

            elif selection == 25:
                from hammer_ping import HammerPing
                os.system('clear')
                self.header(helper.boldwhite + "Welcome to the Hammer Ping page. Here you will find the same "
                                               "information you would find if you asked for a '#hammer ping' from the "
                                               "customer. So your welcome!")
                hammer = HammerPing()
                hammer.display()

            elif selection == 26:
                from host_collections import HostCollection
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Host Collections page. Here you will find all host '
                                               'collections by Organization.')
                hostcol = HostCollection()
                hostcol.display()

            elif selection == 27:
                from hosts import Hosts
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Hosts page of the Satellite. Here you will find all '
                                               'hosts from the Satellite.')
                host = Hosts()
                host.display()

            elif selection == 28:
                from lce import LCE
                os.system('clear')
                self.header(helper.boldwhite + "Welcome to the Lifecycle Environments page. Here you will find all "
                                               "LCE's associated with the Satellite.")
                lce = LCE()
                lce.display()

            elif selection == 29:
                from manifest_history import ManifestHistory
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Manifest History page. Here you will find the results '
                                               'of all manifest upload attempts.')
                manifest = ManifestHistory()
                manifest.display()

            elif selection == 30:
                from media import Media
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Media page. Here you will find all synced '
                                               'media to the satellite.')
                media = Media()
                media.display()

            elif selection == 31:
                from openscap_contents import OpenscapContent
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite OpenSCAP content page. Here you will find all '
                                               'OpenSCAP modules loaded into the Satellite.')
                scap = OpenscapContent()
                scap.display()

            elif selection == 32:
                from openscap_policies import OpenscapPolicy
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite OpenSCAP profile page. Here you will find all '
                                               'OpenSCAP profiles created on the Satellite.')
                profile = OpenscapPolicy()
                profile.display()

            elif selection == 33:
                from os_list import OSList
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite OS List page. Here you will find all the '
                                               'Operating Systems associated with the Satellite.')
                obj = OSList()
                obj.display()

            elif selection == 34:
                from products import Product
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Products page. Here you will find all products'
                                               'eligible on the Satellite based on the currently uploaded manifest.')
                prod = Product()
                prod.display()

            elif selection == 35:
                from provisioning_template import ProvisionTemplate
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Provisioning Template page. This is exactly '
                                               'what it sounds like, so you know what to do.')
                temp = ProvisionTemplate()
                temp.display()

            elif selection == 36:
                from puppet_environment import PuppetEnviornment
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Puppet Environment page. Here you can find all'
                                               ' configured/created puppet environments from the Satellite.')
                pupenv = PuppetEnviornment()
                pupenv.display()

            elif selection == 37:
                from recurring_logic import RecurringLogic
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Recurring Logic page. If you know what this '
                                               'is for, please let Taft know so he can set an accurate description '
                                               'here.')
                logic = RecurringLogic()
                logic.display()

            elif selection == 38:
                from rex_features import RexFeatures
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite REX Features page. Here you will find all the '
                                               'features from the list on the REX page from the Satellite.')
                feat = RexFeatures()
                feat.display()

            elif selection == 39:
                from rex_history import RexHistory
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite REX History page. Here you will find the '
                                               'history of all the Satellite REX jobs run.')
                hist = RexHistory()
                hist.display()

            elif selection == 40:
                from satellite_tasks_summary import TaskSummary
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Task Summary page. Here you will find a count '
                                               'of all the tasks on the Satellite by State/Result. This is the same '
                                               'information you can get from querying the database with that '
                                               'overcomplicated looking SQL query. So why not use gps-satellite')
                task = TaskSummary()
                task.display()

            elif selection == 41:
                from statistics import Statistics
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Statistics page. Here you will find '
                                               'statistical data on the hosts registered to the Satellite. Not sure why'
                                               ' this would be useful, but its offered.')
                stat = Statistics()
                stat.display()

            elif selection == 42:
                from settings import Settings
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Settings page. Here you can find all the '
                                               'settings from the Satellite settings page in the webui.')
                set = Settings()
                set.display()

            elif selection == 43:
                from sub_man_facts import SubManFacts
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Sub-Man Facts page. Here you will find a GIANT'
                                               ' list of facts about each host collected from subscription-manager and '
                                               'reported to the Satellite.')
                fact = SubManFacts()
                fact.display()

            elif selection == 44:
                from subnet_list import SubnetList
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Subnet page. Here you can find all configured '
                                               'subnets on the Satellite.')
                subnet = SubnetList()
                subnet.display()

            elif selection == 45:
                from subscriptions import Subscriptions
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Satellite Subscriptions page. Here you can find '
                                               'information on all subscriptions attached to each manifest of each '
                                               'organization on the Satellite.')
                subscription = Subscriptions()
                subscription.display()

            elif selection == 46:
                from sync_plan import SyncPlan
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Sync Plan page. Here you will find all configured sync '
                                               'plans from the Satellite.')
                plan = SyncPlan()
                plan.display()

            elif selection == 47:
                from template_kinds import TemplateKind
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the Template Type page. Here you can find all associated '
                                               'types of templates supported by the Satellite.')
                template = TemplateKind()
                template.display()

            elif selection == 48:
                from user_list import UserList
                os.system('clear')
                self.header(helper.boldwhite + 'Welcome to the User List page. Here you can find all users for the '
                                               'Satellite.')
                user = UserList()
                user.display()

        except ValueError:
            print("That's not a number, try again later")


maps = Maps()
maps.main()
