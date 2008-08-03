%define	name	tuxpuck
%define	version	0.8.2
%define	release	%mkrel 11

Summary:	Clone of ShufflePuck Cafe historical game
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.efd.lth.se/~d00jkr/tuxpuck/
License:	GPL
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL-devel png-devel oggvorbis-devel libz-devel jpeg-devel
BuildRequires:	freetype2-devel

%description
Anyone remember "Shufflepuck Cafe" for the Amiga/AtariST ?

%prep
%setup -q

%build
perl -pi -e 's/-Werror//' Makefile utils/Makefile
perl -pi -e 's/`sdl-config --cflags`/`sdl-config --cflags` `freetype-config --cflags`/' utils/Makefile
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT
install -m755 %{name} -D $RPM_BUILD_ROOT%{_gamesbindir}/%{name}


install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/applications/
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Tuxpuck
Comment=Clone of ShufflePuck Cafee
Exec=%{_gamesbindir}/%name
Icon=arcade_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF


%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING 
%{_gamesbindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop


