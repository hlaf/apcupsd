# $Id$
# Authority: dag
# Upstream: Kern Sibbald <kern$sibbald,com>
# Upstream: <apcupsd-users$lists,sourceforge,net>

%define _sbindir /sbin

Summary: APC UPS power control daemon
Name: apcupsd
Version: 3.14.14
Release: 2%{?dist}
License: GPLv2
Group: System Environment/Daemons
URL: http://www.apcupsd.com/

Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glibc-devel
Requires: perl

%description
Apcupsd can be used for controlling most APC UPSes. During a power failure,
apcupsd will inform the users about the power failure and that a shutdown
may occur. If power is not restored, a system shutdown will follow when the
battery is exhausted, a timeout (seconds) expires, or the battery run-time
expires based on internal APC calculations determined by power consumption
rates. If the power is restored before one of the above shutdown conditions
is met, apcupsd will inform users about this fact.

Some features depend on what UPS model you have (simple or smart).

%prep
%setup -q

%{__cat} <<EOF >apcupsd.logrotate
%{_localstatedir}/log/apcupsd.events {
        missingok
        copytruncate
        notifempty
}
EOF

%build
cd %{_ebuild_root} && %{__make} Release_Linux32

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}
cp -a %{_ebuild_root}/Release_Linux32/etc %{buildroot}
cp -a %{_ebuild_root}/Release_Linux32/sbin %{buildroot}
cp -a %{_ebuild_root}/Release_Linux32/usr %{buildroot}
%{__install} -Dp -m0644 apcupsd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/apcupsd

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add apcupsd

%preun
if [ $1 -eq 0 ]; then
        /sbin/service apcupsd stop &>/dev/null || :
        /sbin/chkconfig --del apcupsd
fi

%postun
/sbin/service apcupsd condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING doc/* examples/ INSTALL
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/apcupsd/
%config(noreplace) %{_sysconfdir}/logrotate.d/apcupsd
%config %{_initrddir}/*
%{_sbindir}/*
%exclude %{_initrddir}/halt*
%{_datadir}/hal/fdi/policy/20thirdparty/80-apcupsd-ups-policy.fdi

%changelog
* Fri Nov 02 2018 Henrique Lindgren <henriquelindgren@gmail.com> - 3.14.14-2
- Fixed spelling errors in the package description.

* Thu Nov 01 2018 Henrique Lindgren <henriquelindgren@gmail.com> - 3.14.14-1
- new upstream release

* Sat Jan 21 2012 David Hrbáč <david@hrbac.cz> - 3.14.10-1
- new upstream release

* Sat Jan 21 2012 David Hrbáč <david@hrbac.cz> - 3.14.9-1
- new upstream release

* Wed Sep 08 2010 David Hrbáč <david@hrbac.cz> - 3.14.8-1
- new upstream release

* Sun Mar  2 2008 Dries Verachtert <dries@ulyssis.org> - 3.14.3-1
- Updated to release 3.14.3.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.10.18-1.2
- Rebuild for Fedora Core 5.

* Mon Sep 05 2005 Dries Verachtert <dries@ulyssis.org> - 3.10.18-1
- Updated to new release 3.10.18.

* Fri Mar 25 2005 Dag Wieers <dag@wieers.com> - 3.10.13-2
- Added --enable-snmp configure option. (Bobby Kuo)

* Wed Apr 21 2004 Dag Wieers <dag@wieers.com> - 3.10.13-1
- Updated to new release 3.10.13.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 3.10.12-1
- Added apcupsd.logrotate. (Derek Werthmuller)
- Updated to new release 3.10.12.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 3.10.11-1
- Added apcupsd.conf. (Andrew Newman)
- Fixed unsuccessful 'make install'.

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 3.10.11-0
- Initial package. (using DAR)
