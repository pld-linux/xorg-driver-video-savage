Summary:	X.org video driver for S3 Savage family video chips
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych z rodziny S3 Savage
Name:		xorg-driver-video-savage
Version:	2.0.1.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-savage-%{version}.tar.bz2
# Source0-md5:	306f4209765a73102419fdfe2ef3481b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/savage_drv.so
%{_mandir}/man4/savage.4x*
