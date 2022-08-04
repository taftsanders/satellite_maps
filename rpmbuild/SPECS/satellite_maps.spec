Name: satellite_maps
Version: 1.0	
Release: 1%{?dist}
Summary: Satellite 6 mapping tool	
Group: Applications/File	
License: GPLv3	
URL: http://splinter.usersys.redhat.com:3000/taft/gps-satellite
Source0: satellite_maps-1.0.tar
BuildRequires: python3
Requires: python3	

%description
gps_satellite rendering tool

%global debug_package %{nil}

%prep
%setup -q

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin/
mkdir -p ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
mkdir -p $RPM_BUILD_ROOT%{_doc}


cp main.py ${RPM_BUILD_ROOT}/usr/bin/satellite_maps
cp -ar colored ${RPM_BUILD_ROOT}/usr/lib64/python3.6
cp activation_key.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp arch_list.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp bookmark.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp capsule_lce_assigned.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp capsule_lce_available.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp capsule_list.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp compute_profile.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp compute_resource.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp config_template.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp content_view.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp contentviewfilter.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp contentviewversion.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp cv_history.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp cv_puppet_modules.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp dashboard.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp discovered_hosts.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp discovery_rules.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp docker_containers.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp docker_registries.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp dockermanifests.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp dockertags.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp domainlist.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp hammer_ping.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp helper.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp host_collections.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp host_groups.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp hosts.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp lce.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp location.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp manifest_history.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp media.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp openscap_contents.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp openscap_policies.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp organization.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp os_list.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp products.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp provisioning_template.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp puppet_environment.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp recurring_logic.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp rex_features.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp rex_history.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp satellite_tasks_summary.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp settings.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp sat_statistics.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp sub_man_facts.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp subnet_list.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp subscriptions.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp sync_plan.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp template_kinds.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp user_list.py ${RPM_BUILD_ROOT}/usr/lib64/python3.6/satellite_maps
cp LICENSE CHANGELOG $RPM_BUILD_ROOT%{_doc}

chmod -R +x ${RPM_BUILD_ROOT}/usr/bin/satellite_maps

%files
/usr/bin/satellite_maps
/usr/lib64/python3.6/satellite_maps/
/usr/lib64/python3.6/colored/
%doc CHANGELOG LICENSE

%exclude /usr/lib64/python3.6/satellite_maps/__pycache__/
%exclude /usr/lib64/python3.6/colored/__pycache__/

%changelog
* Sun May 27 2018 Taft Sanders <tasander@redhat.com> - 1.0-1
- Created first package.
