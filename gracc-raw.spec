%define debug_packages ${nil}
%define debug_package ${nil}

Name:           gracc-raw
Version:        0.02.00
Release:        1%{?dist}
Summary:        GRACC RAW Record Processor
License:        MIT

URL:            https://opensciencegrid.github.io/gracc
Source:         %{name}.tar.gz

BuildArch: noarch
BuildRequires:  systemd-units
Requires(pre): shadow-utils
Requires: logstash

%description
The gracc-raw agent processes raw accounting records (e.g. from the 
gracc-collector) from a RabbitMQ queue, enriches and normalizes them,
and indexes them into Elasticsearch.

%prep
%autosetup -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_unitdir}/
cp -p gracc-raw.service %{buildroot}%{_unitdir}/
cp -p gracc-raw@.service %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/gracc-stash
cp -p gracc-raw.conf %{buildroot}%{_sysconfdir}/gracc-stash/
cp -p gracc-raw-template.json %{buildroot}%{_sysconfdir}/gracc-stash/
cp -p defaults.env %{buildroot}%{_sysconfdir}/gracc-stash/


%files
%doc README.md
%{_unitdir}/gracc-raw.service
%{_unitdir}/gracc-raw@.service
%dir %{_sysconfdir}/gracc-stash
%{_sysconfdir}/gracc-stash/gracc-raw.conf
%{_sysconfdir}/gracc-stash/gracc-raw-template.json
%config(noreplace) %{_sysconfdir}/gracc-stash/defaults.env


%pre
getent group gracc >/dev/null || groupadd -r gracc
getent passwd gracc >/dev/null || \
    useradd -r -g gracc -d /etc/gracc -s /sbin/nologin \
    -c "Account used to run the GRACC collector" gracc
exit 0

%changelog
* Tue Aug 30 2016 Kevin Retzke <kretzke@fnal.gov> - 0.02.00-1
- Use environment variables in logstash config

* Tue Jun 07 2016 Kevin Retzke <kretzke@fnal.gov> - 0.01.00-1
- Initial release
