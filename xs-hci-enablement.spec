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
* force-umount-unreachable-nfs: Service that forces the umount of unreachable
                                NFS shares during shutdown

%prep
%setup -q

%install
mkdir -p %{buildroot}/usr/bin/
cp force-umount-unreachable-nfs/force-umount-unreachable-nfs %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/lib/systemd/system/
cp force-umount-unreachable-nfs/force-umount-unreachable-nfs.service %{buildroot}/usr/lib/systemd/system/

%post
%systemd_post force-umount-unreachable-nfs.service
systemctl enable force-umount-unreachable-nfs.service
systemctl start force-umount-unreachable-nfs.service

%preun
%systemd_preun force-umount-unreachable-nfs.service

%postun
%systemd_postun force-umount-unreachable-nfs.service


%files
/usr/bin/force-umount-unreachable-nfs
/usr/lib/systemd/system/force-umount-unreachable-nfs.service

%changelog
* Mon May 01 2017 Robert Breker <robert.breker@citrix.com> 1.0.0-1
- Initial release
