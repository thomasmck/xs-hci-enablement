%global srcname xs-hci-enablement
Name: %{srcname}		
Version: 1.0.0
Release: 1%{?dist}
Summary: XS HCI enablement

License: BSD	
Source0: xs-hci-enablement-1.0.0.tar.gz

BuildArch: noarch
%{?systemd_requires}
BuildRequires: systemd
Requires: python

%description
Tools for HCI enablement on XenServer:
* hci-unplug-pbds: Service that unplugs PBDs of SRs marked using
                   other-config:hci-unplug-pbds during shutdown.
                   Forces umount of unreachable NFS shares
                   during shutdown to avoid shutdown timeouts.

%prep
%setup -q

%install
mkdir -p %{buildroot}/usr/bin/
cp hci-unplug-pbds/hci-unplug-pbds %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/lib/systemd/system/
cp hci-unplug-pbds/hci-unplug-pbds.service %{buildroot}/usr/lib/systemd/system/

%post
%systemd_post hci-unplug-pbds.service
systemctl enable hci-unplug-pbds.service
systemctl start hci-unplug-pbds.service

%preun
%systemd_preun hci-unplug-pbds.service

%postun
%systemd_postun hci-unplug-pbds.service


%files
/usr/bin/hci-unplug-pbds
/usr/lib/systemd/system/hci-unplug-pbds.service

%changelog
* Mon May 01 2017 Robert Breker <robert.breker@citrix.com> 1.0.0-1
- Initial release
