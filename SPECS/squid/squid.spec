Summary:        Caching and forwarding HTTP web proxy
Name:           squid
Version:        5.6
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.squid-cache.org
Group:          Networking/Web/Proxy
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        http://www.squid-cache.org/Versions/v5/%{name}-%{version}.tar.xz
%define sha512 %{name}=940a4d21ea8e3384642951d80c501a192178d1220f06a59a7bc54ce86d49caea0a86b6e789e28bcb7125ffa2a564ca1aca886a96cccf6356314121a81f38221a

Patch0:         squid-5.6-openssl3.patch

Source1:        squid.sysconfig
Source2:        squid.pam
Source3:        squid.service
Source4:        cache_swap.sh
Source5:        squid.logrotate

BuildRequires:  Linux-PAM-devel
BuildRequires:  autoconf
BuildRequires:  ed
BuildRequires:  expat
BuildRequires:  expat-devel
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gnupg
BuildRequires:  krb5-devel
BuildRequires:  libcap-devel
BuildRequires:  libecap-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  nettle
BuildRequires:  openldap
BuildRequires:  openssl-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros

Requires:       openssl
Requires:       shadow
Requires:       perl-URI
Requires:       systemd

%description
Squid is a high-performance proxy caching server for Web clients,
supporting FTP, gopher, and HTTP data objects. Unlike traditional
caching software, Squid handles all requests in a single,
non-blocking, I/O-driven process. Squid keeps meta data and especially
hot objects cached in RAM, caches DNS lookups, supports non-blocking
DNS lookups, and implements negative caching of failed requests.

Squid consists of a main server program squid, a Domain Name System
lookup program (dnsserver), a program for retrieving FTP data
(ftpget), and some management and client tools.

%prep
%autosetup -p1

%define _confdir %{_sysconfdir}
%define _squiddatadir /usr/share/squid

%build
%define _lto_cflags %{nil}

sh ./configure --host=%{_host} --build=%{_build} \
      --program-prefix= \
      --disable-dependency-tracking \
      --bindir=%{_bindir} \
      --sbindir=%{_sbindir} \
      --includedir=%{_includedir} \
      --libdir=%{_libdir} \
      --localstatedir=%{_localstatedir} \
      --sharedstatedir=%{_sharedstatedir} \
      --mandir=%{_mandir} \
      --infodir=%{_infodir} \
      --prefix=%{_sysconfdir}/squid \
      --sysconfdir=%{_confdir}/squid \
      --libexecdir=%{_libdir}/squid \
      --datadir=%{_squiddatadir} \
      --exec-prefix=%{_prefix} \
      --with-logdir='%{_localstatedir}/log/squid' \
      --with-pidfile='/run/squid.pid' \
      --disable-dependency-tracking \
      --enable-eui \
      --enable-follow-x-forwarded-for \
      --enable-auth \
      --enable-auth-basic="DB,fake,getpwnam,LDAP,NCSA,PAM,POP3,RADIUS,SASL,SMB,SMB_LM" \
      --enable-auth-ntlm="SMB_LM,fake" \
      --enable-auth-digest="file,LDAP" \
      --enable-external-acl-helpers="LDAP_group,unix_group,wbinfo_group" \
      --enable-cache-digests \
      --enable-cachemgr-hostname=localhost \
      --enable-delay-pools \
      --enable-epoll \
      --enable-ecap \
      --enable-icap-client \
      --enable-ident-lookups \
      --enable-linux-netfilter \
      --enable-removal-policies="heap,lru" \
      --enable-ssl \
      --enable-ssl-crtd \
      --enable-diskio \
      --enable-wccpv2 \
      --enable-esi \
      --with-aio \
      --with-default-user="squid" \
      --with-dl \
      --with-openssl \
      --with-pthreads \
      --without-mit-krb5 \
      --without-heimdal-krb5 \
      --disable-arch-native \
      --disable-security-cert-validators \
      --disable-strict-error-checking \
      --with-swapdir=%{_localstatedir}/spool/squid

mkdir -p src/icmp/tests
mkdir -p tools/squidclient/tests
mkdir -p tools/tests

%make_build DEFAULT_SWAP_DIR=%{_localstatedir}/spool/squid

%install
%make_install %{?_smp_mflags}

mkdir -p %{buildroot}%{_sysconfdir}/squid
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_sysconfdir}/pam.d/
mkdir -p %{buildroot}%{_libexecdir}/squid
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_datadir}/squid
mkdir -p %{buildroot}/run/squid

rm -rf %{buildroot}%{_datadir}/man/

install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/squid
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/
install -m 644 %{SOURCE3} %{buildroot}%{_unitdir}
install -m 755 %{SOURCE4} %{buildroot}%{_libexecdir}/squid
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/

mkdir -p %{buildroot}%{_localstatedir}/log/squid
mkdir -p %{buildroot}%{_localstatedir}/spool/squid
mkdir -p %{buildroot}/run/squid

chmod 644 contrib/url-normalizer.pl contrib/user-agents.pl

%files
%defattr(-,root,root)
%license COPYING
%doc CONTRIBUTORS README ChangeLog QUICKSTART src/squid.conf.documented
%doc contrib/url-normalizer.pl contrib/user-agents.pl

%{_unitdir}/squid.service
%attr(755,root,root) %dir %{_libexecdir}/squid
%attr(755,root,root) %{_libexecdir}/squid/cache_swap.sh
%attr(755,root,root) %dir %{_sysconfdir}/squid
%attr(755,root,root) %dir %{_libdir}/squid
%attr(770,squid,root) %dir %{_localstatedir}/log/squid
%attr(750,squid,squid) %dir %{_localstatedir}/spool/squid
%attr(755,squid,squid) %dir /run/squid

%config(noreplace) %{_sysconfdir}/pam.d/squid.pam
%config(noreplace) %{_sysconfdir}/squid/cachemgr.conf.default
%config(noreplace) %{_sysconfdir}/squid/errorpage.css.default
%config(noreplace) %{_sysconfdir}/squid/mime.conf.default
%config(noreplace) %{_sysconfdir}/squid/squid.conf.documented
%config(noreplace) %{_sysconfdir}/squid/squid.conf.default
%config(noreplace) %{_sysconfdir}/logrotate.d/squid.logrotate

%{_sysconfdir}/squid/cachemgr.conf
%{_sysconfdir}/squid/errorpage.css
%{_sysconfdir}/squid/mime.conf
%{_sysconfdir}/squid/squid.conf
%{_sysconfdir}/sysconfig/squid
%{_datadir}/squid/mib.txt

%dir %{_datadir}/squid
%attr(-,root,root) %{_datadir}/squid/errors
%{_datadir}/squid/icons
%{_sbindir}/squid
%{_bindir}/squidclient
%{_bindir}/purge
%{_libdir}/squid/*

%pre
if ! getent group squid >/dev/null 2>&1; then
    /usr/sbin/groupadd -g 53 squid
fi

if ! getent passwd squid >/dev/null 2>&1 ; then
    /usr/sbin/useradd -g 53 -u 53 -d /var/spool/squid -r -s /sbin/nologin squid >/dev/null 2>&1 || exit 1
fi

for i in /var/log/squid /var/spool/squid ; do
    if [ -d $i ] ; then
        for adir in `find $i -maxdepth 0 \! -user squid`; do
            chown -R squid:squid $adir
        done
    fi
done

%post
%systemd_post squid.service

%preun
%systemd_preun squid.service

%postun
%systemd_postun_with_restart squid.service

%changelog
* Mon Jul 25 2022 Susant Sahani <ssahani@vmware.com> 5.6-1
- Version bump.
* Wed Nov 10 2021 Satya Naga Vasamsetty <svasamsetty@vmware.com> 5.0.5-4
- Openssl 3.0.0 compatibility
* Fri Aug 20 2021 Shreenidhi Shedi <sshedi@vmware.com> 5.0.5-3
- Bump version as a part of rpm upgrade
* Tue Aug 17 2021 Shreenidhi Shedi <sshedi@vmware.com> 5.0.5-2
- Bump version as a part of nettle upgrade
* Fri Apr 30 2021 Susant Sahani <ssahani@vmware.com> 5.0.5-1
- Initial rpm release.
