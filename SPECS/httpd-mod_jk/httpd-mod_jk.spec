Summary:    Apache Tomcat Connector
Name:       httpd-mod_jk
Version:    1.2.48
Release:    4%{?dist}
License:    Apache
URL:        http://tomcat.apache.org/connectors-doc
Group:      Applications/System
Vendor:     VMware, Inc.
Distribution:   Photon

Source0:	http://www.apache.org/dist/tomcat/tomcat-connectors/jk/tomcat-connectors-%{version}-src.tar.gz
%define sha1 tomcat-connectors=d5cec3b63d6b2e21b5ffc0e43102f85a177ddd89

Requires:       httpd

BuildRequires:  apr-devel
BuildRequires:  apr-util-devel
BuildRequires:  httpd-devel
BuildRequires:  httpd-tools

%description
The Apache Tomcat Connectors project is part of the Tomcat project and provides web server plugins to connect web servers with Tomcat and other backends.
mod_jk is a module connecting Tomcat and Apache

%prep
%autosetup -n tomcat-connectors-%{version}-src -p1

%build
cd native
sh ./configure --with-apxs=%{_bindir}/apxs

make %{?_smp_mflags}

%install
install -vdm 755 %{buildroot}
install -D -m 755 native/apache-2.0/mod_jk.so %{buildroot}%{_libdir}/httpd/modules/mod_jk.so
install -D -m 644 conf/workers.properties  %{buildroot}%{_sysconfdir}/httpd/conf/workers.properties
install -D -m 644 conf/httpd-jk.conf  %{buildroot}%{_sysconfdir}/httpd/conf/httpd_jk.conf

%check
make -k check %{?_smp_mflags} |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%files
%defattr(-,root,root)
%{_libdir}/httpd/modules/mod_jk.so
%config(noreplace) %{_sysconfdir}/httpd/conf/httpd_jk.conf
%config(noreplace) %{_sysconfdir}/httpd/conf/workers.properties

%changelog
* Tue Oct 19 2021 Shreenidhi Shedi <sshedi@vmware.com> 1.2.48-4
- Bump version as a part of httpd upgrade
* Thu Oct 07 2021 Dweep Advani <dadvani@vmware.com> 1.2.48-3
- Rebuild with upgraded httpd 2.4.50
* Tue Oct 05 2021 Shreenidhi Shedi <sshedi@vmware.com> 1.2.48-2
- Bump version as a part of httpd upgrade
* Wed Sep 09 2020 Gerrit Photon <photon-checkins@vmware.com> 1.2.48-1
- Automatic Version Bump
* Thu Sep 13 2018 Siju Maliakkal <smaliakkal@vmware.com> 1.2.44-1
- Upgrade to latest version
* Tue Apr 25 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.2.42-2
- Ensure non empty debuginfo
* Tue Feb 21 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.2.42-1
- Initial build. First version
