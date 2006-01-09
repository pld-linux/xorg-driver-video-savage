Summary:	X.org video driver for S3 Savage family video chips
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych z rodziny S3 Savage
Name:		xorg-driver-video-savage
Version:	2.0.2.3
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/driver/xf86-video-savage-%{version}.tar.bz2
# Source0-md5:	28ec4e07bda55ab8b35b4735405ac5a3
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for S3 Savage family video chips. It supports PCI
and AGP boards with the following chips: Savage3D, Savage4,
Savage2000, Savage/MX, Savage/IX, SuperSavage/MX, SuperSavage/IX,
ProSavage PM133, ProSavage KM133, Twister (ProSavage PN133), TwisterK
(ProSavage KN133), ProSavage DDR, ProSavage DDR-K. Savage2000 support
has acceleration limited to 2D only. Dualhead operation is supported
on MX, IX and SuperSavage chips.

%description -l pl
Sterownik obrazu X.org dla uk³adów graficznych z rodziny S3 Savage.
Obs³uguje karty PCI i AGP oparte na nastêpuj±cych uk³adach: Savage3D,
Savage4, Savage2000, Savage/MX, Savage/IX, SuperSavage/MX,
SuperSavage/IX, ProSavage PM133, ProSavage KM133, Twister (ProSavage
PN133), TwisterK (ProSavage KN133), ProSavage DDR, ProSavage DDR-K.
Obs³uga Savage2000 ma akceleracjê ograniczon± do operacji 2D. Tryb
dualhead jest obs³ugiwany na uk³adach MX, IX i SuperSavage. 

%prep
%setup -q -n xf86-video-savage-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/savage_drv.so
%{_mandir}/man4/savage.4*
