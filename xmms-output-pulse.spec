Summary:	PulseAudio output plugin for XMMS
Summary(pl.UTF-8):	Wtyczka wyjściowa PulseAudio dla XMMS-a
Name:		xmms-output-pulse
Version:	0.9.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://0pointer.de/lennart/projects/xmms-pulse/xmms-pulse-%{version}.tar.gz
# Source0-md5:	9fe94d5af0d4e5b9663d29afa52c3706
URL:		http://0pointer.de/lennart/projects/xmms-pulse/
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.2
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.0
Requires:	xmms >= 1.2.0
Obsoletes:	libao-polyp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS output plugin for the PulseAudio sound server.

%description -l pl.UTF-8
Wtyczka wyjściowa XMMS-a dla serwera dźwięku PulseAudio.

%prep
%setup -q -n xmms-pulse-%{version}

%build
%configure \
	--disable-lynx \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{xmms_output_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{xmms_output_plugindir}/libxmms-pulse.so
