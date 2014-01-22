#
# Conditional build:
%bcond_with	bmp	# BMP plugin
%bcond_without	xmms	# XMMS plugin
#
Summary:	PulseAudio output plugin for XMMS
Summary(pl.UTF-8):	Wtyczka wyjściowa PulseAudio dla XMMS-a
Name:		xmms-output-pulse
Version:	0.9.4
Release:	2
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://0pointer.de/lennart/projects/xmms-pulse/xmms-pulse-%{version}.tar.gz
# Source0-md5:	c879939a6242f07b69298b30bcdeb6c5
URL:		http://0pointer.de/lennart/projects/xmms-pulse/
%if %{with bmp}
BuildRequires:	bmp-devel >= 1:0.9.7
%endif
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.2
BuildRequires:	rpmbuild(macros) >= 1.125
%if %{with xmms}
BuildRequires:	xmms-devel >= 1.2.0
%endif
Requires:	xmms >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS output plugin for the PulseAudio sound server.

%description -l pl.UTF-8
Wtyczka wyjściowa XMMS-a dla serwera dźwięku PulseAudio.

%package -n bmp-output-pulse
Summary:	PulseAudio output plugin for BMP media player
Summary(pl.UTF-8):	Wtyczka wyjściowa PulseAudio dla odtwarzacza multimedialnego BMP
Group:		X11/Applications/Sound
Requires:	bmp >= 1:0.9.7

%description -n bmp-output-pulse
PulseAudio output plugin for BMP media player.

%description -n bmp-output-pulse -l pl.UTF-8
Wtyczka wyjściowa PulseAudio dla odtwarzacza multimedialnego BMP.

%prep
%setup -q -n xmms-pulse-%{version}

%build
%configure \
	--disable-lynx \
	--disable-static \
	%{!?with_xmms:--disable-xmms} \
	%{?with_bmp:--enable-bmp}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with xmms}
rm -f $RPM_BUILD_ROOT%{xmms_output_plugindir}/*.la
%endif
%if %{with bmp}
rm -f $RPM_BUILD_ROOT%{_libdir}/bmp/Output/libbmp-pulse.so
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with xmms}
%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{xmms_output_plugindir}/libxmms-pulse.so
%endif

%if %{with bmp}
%files -n bmp-output-pulse
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/bmp/Output/libbmp-pulse.so
%endif
