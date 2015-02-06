%define name	blogfish
%define version	1.0
%define release 10

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




%changelog
* Sat Nov 06 2010 Jani Välimaa <wally@mandriva.org> 1.0-9mdv2011.0
+ Revision: 594295
- rebuild for python 2.7

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2010.0
+ Revision: 436827
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 1.0-7mdv2009.1
+ Revision: 323366
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0-6mdv2009.0
+ Revision: 243353
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.0-4mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - convert prereq


* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-4mdv2007.0
+ Revision: 96491
- Rebuild against new python
- Import blogfish

* Fri Jun 10 2005 Austin Acton <austin@mandriva.org> 1.0-3mdk
- requires gnome-python-gnomevfs (Eskild Hustvedt)

* Thu Jun 09 2005 Austin Acton <austin@mandriva.org> 1.0-2mdk
- whoops, can run without panel

* Thu Jun 09 2005 Austin Acton <austin@mandriva.org> 1.0-1mdk
- initial package

