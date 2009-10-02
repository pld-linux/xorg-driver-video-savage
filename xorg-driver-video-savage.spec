Summary:	X.org video driver for S3 Savage family video chips
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych z rodziny S3 Savage
Name:		xorg-driver-video-savage
Version:	2.3.1
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-savage-%{version}.tar.bz2
# Source0-md5:	66c319f610e3699c3de0f3ef630abb32
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.10
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.1.0
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-libdri >= 1.1.0
Requires:	xorg-xserver-libglx >= 1.1.0
Requires:	xorg-xserver-server >= 1.1.0
Obsoletes:	X11-driver-savage < 1:7.0.0
Obsoletes:	XFree86-driver-savage < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for S3 Savage family video chips. It supports PCI
and AGP boards with the following chips: Savage3D, Savage4,
Savage2000, Savage/MX, Savage/IX, SuperSavage/MX, SuperSavage/IX,
ProSavage PM133, ProSavage KM133, Twister (ProSavage PN133), TwisterK
(ProSavage KN133), ProSavage DDR, ProSavage DDR-K. Savage2000 support
has acceleration limited to 2D only. Dualhead operation is supported
on MX, IX and SuperSavage chips.

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych z rodziny S3 Savage.
Obsługuje karty PCI i AGP oparte na następujących układach: Savage3D,
Savage4, Savage2000, Savage/MX, Savage/IX, SuperSavage/MX,
SuperSavage/IX, ProSavage PM133, ProSavage KM133, Twister (ProSavage
PN133), TwisterK (ProSavage KN133), ProSavage DDR, ProSavage DDR-K.
Obsługa Savage2000 ma akcelerację ograniczoną do operacji 2D. Tryb
dualhead jest obsługiwany na układach MX, IX i SuperSavage. 

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
