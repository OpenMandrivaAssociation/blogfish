%define name	blogfish
%define version	1.0
%define release %mkrel 6

Name: 	 	%{name}
Summary: 	Evolutionary meme spreader from the GNOME panel
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/blogfish/%{name}-%{version}.tar.bz2
URL:		http://blogfish.sourceforge.net/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

Requires:	pygtk2.0 pygtk2.0-libglade
Requires:	gnome-python gnome-python-gconf gnome-python-applet
Requires:	gnome-python-gnomevfs
Requires(post):		GConf2
Requires(postun):		GConf2

%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/%{_lib}/python' + sys.version[:3] + '/site-packages/')"`)

%description
Blogfish is a Gnome panel applet which allows you to spread your blog URL,
website URL or random thoughts to other users.  Good memes survive; bad
ones are voted down and go belly up.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_libdir/bonobo/servers
cp servers/*.server %buildroot/%_libdir/bonobo/servers
mkdir -p %buildroot/%_datadir/%name
cp images/*.png %buildroot/%_datadir/%name
cp src/*.glade %buildroot/%_datadir/%name
mkdir -p %buildroot/%python_sitepkgsdir/%name
cp src/*.py %buildroot/%python_sitepkgsdir/%name
mkdir -p %buildroot/%_bindir
cp src/%name %buildroot/%_bindir
mkdir -p %buildroot/%_sysconfdir/gconf/schemas
cp %name.schemas %buildroot/%_sysconfdir/gconf/schemas

%post
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 \
  --makefile-install-rule %{_sysconfdir}/gconf/schemas/blogfish.schemas \
  > /dev/null

%postun
gconftool-2 --recursive-unset /apps/blogfish

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS README MARKETING TODO
%{_bindir}/%name
%{_libdir}/bonobo/servers/*
%{_datadir}/%name
%python_sitepkgsdir/%name
%{_sysconfdir}/gconf/schemas/*


