%define debug_packages ${nil}
%define debug_package ${nil}

Name:           gracc-raw
Version:        0.01.00
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
mkdir -p %{buildroot}%{_sysconfdir}/gracc
cp -p gracc-raw.conf %{buildroot}%{_sysconfdir}/gracc/
mkdir -p %{buildroot}%{_datadir}/gracc
cp -p gracc-raw-template.json %{buildroot}%{_datadir}/gracc/


%files
%doc README.md
%{_unitdir}/gracc-raw.service
%{_unitdir}/gracc-raw@.service
%dir %{_sysconfdir}/gracc
%config(noreplace) %{_sysconfdir}/gracc/gracc-raw.conf
%{_datadir}/gracc


%pre
getent group gracc >/dev/null || groupadd -r gracc
getent passwd gracc >/dev/null || \
    useradd -r -g gracc -d /etc/gracc -s /sbin/nologin \
    -c "Account used to run the GRACC collector" gracc
exit 0

%changelog
* Tue Jun 07 2016 Kevin Retzke <kretzke@fnal.gov> - 0.01.00-1
- Initial release
