Summary:	Midnight Commander visual shell
Summary(de):	Visuelle Shell Midnight Commander 
Summary(fr):	Le shell Midnight Commander
Summary(pl):	Midnight Commander - pow�oka wizualna
Summary(tr):	Midnight Commander g�rsel kabu�u
Name:		mc
Version:	4.5.33
Release:	2
Copyright:	GPL
Group:		Shells
Group(pl):	Pow�oki
########	ftp://peyote-asesino.nuclecu.unam.mx/linux/local/devel
Source0:	%{name}-%{version}.tar.gz
Source1:	mcserv.pamd
Source2:	mcserv.init
Source3:	%{name}.sh
Source4:	mcserv.sysconfig
URL:		http://mc.blackdown.org/mc/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Midnight Commander is a visual shell much like a file manager, only with way
more features. It is text mode, but also includes mouse support if you are
running GPM. Its coolest feature is the ability to ftp, view tar, zip files,
and poke into RPMs for specific files.  :-)

%description -l de
Midnight Commander ist ein Visual-Shell, �hnlich einem Dateimanager, aber
mit zus�tzlichen Funktionen. Es l�uft im Textmodus, kann jedoch eine Maus
unterst�tzen, wenn GPM betrieben wird. Seine coolsten F�higkeiten sind die
ftp-Option, das Einsehen von tar- und zip-Dateien und das Herausfischen von
spezifischen Dateien aus RPMs.

%description -l fr
Midnight Commander est un shell visuel un peu comme un gestionnaire de
fichiers mais avec plus de possibilit�s. Ceci est la version texte mais elle
int�gre aussi la gestion de la souris si vous ex�cutez gpm. Sa
caract�ristique la plus agr�able est la possibilit� de faire du ftp, de
visualiser les fichiers tar et zip et de parcourir les RPMs pour rechercher
des fichiers pr�cis. :-)

%description -l pl
Midnight Commander jest wizualnym shellem podobnym do Norton Commandera.
Pracuje w trybie tekstowym, ale ma tak�e wspomaganie dla myszki. Jest super
;) MC ma wbudowanego klienta ftp, mo�e zagl�da� do skompresowanego archiwum
tarowego, do *.zip oraz *.rpm. Teraz r�wnie� ma wspomaganie dla urz�dze�
/dev/pts/{0-2048} - standard Unix98.  

%description -l tr
Midnight Commander bir dosya y�neticisine �ok benzeyen ancak daha yetenekli
bir g�rsel kabuktur. Metin ekranda �al���r ve GPM �al���yorsa fare deste�i
vard�r. En ho� �zellikleri ftp yapabilmesi, tar, zip ve RPM dosyalar�n�n
i�eriklerini g�sterebilmesidir.

%package -n	mcserv
Summary:	Midnight Commander file server
Summary(de):	Midnight Commander File-Server 
Summary(fr):	Serveur de fichier de Midnight Commander
Summary(pl):	Serwer plik�w Midnight Commandera
Summary(tr):	Midnight Commander dosya sunucusu
Group:		Daemons
Group(pl):	Serwery
Requires:	portmap
Requires:	pam >= 0.66

%description -n mcserv
mcserv is the server program for the Midnight Commander networking file
system. It provides access to the host file system to clients running the
Midnight file system (currently, only the Midnight Commander file manager).

%description -l de -n mcserv
mcserv ist das Server-Programm f�r das Netzwerkdateisystem Midnight Commander.
Es erm�glicht den Zugriff auf das Host-Dateisystem f�r Clients, die das
Midnight-Dateisystem ausf�hren (z.Zt. nur Midnight Commander file manager).

%description -l pl -n mcserv
Mcserv jest aplikacj� dla sieciowego systemy plik�w Midnight Commandera.
Pozwala na dost�p do systemu plik�w dla klienta pracuj�cego pod MC i 
u�ywaj�cego jego systemu plik�w.

%description -l de -n mcserv
mcserv ist das Server-Programm f�r das Netzwerkdateisystem Midnight Commander.
Es erm�glicht den Zugriff auf das Host-Dateisystem f�r Clients, die das
Midnight-Dateisystem ausf�hren (z.Zt. nur Midnight Commander file manager).

%description -l de -n mcserv
mcserv ist das Server-Programm f�r das Netzwerkdateisystem Midnight Commander.
Es erm�glicht den Zugriff auf das Host-Dateisystem f�r Clients, die das
Midnight-Dateisystem ausf�hren (z.Zt. nur Midnight Commander file manager).

%description -l fr -n mcserv
mcserv est un programme pour les syst�me de fichiers r�seau de
Midnight Commander. Il fournit un acc�s au syst�me de fichiers de l'h�te
aux clients sur lesquelles tourne le syst�me de fichiers Midnight
(actuellement, Midnight Commander est le seul).

%description -l tr -n mcserv
mcserv, Midnight Commander a� dosya sisteminin sunucu program�d�r. Midnight
dosya sistemini �al��t�ran istemcilerin sunucu dosya sistemine eri�imini
sa�lar.
 
%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
        --sysconfdir=/etc \
	--with-ext2undel \
	--with-netrc \
	--with-x \
	--without-debug \
	--without-gnome \
	--mandir=%{_mandir} \
	--with-terminfo \
	--with-edit \
	--with-included-slang 

make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/{rc.d/init.d,pam.d,sysconfig,profile.d}}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/mcserv
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/mcserv
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/mcserv

make install \
	DESTDIR=$RPM_BUILD_ROOT

install lib/mc.csh	$RPM_BUILD_ROOT/etc/profile.d
install %{SOURCE3}	$RPM_BUILD_ROOT/etc/profile.d

mv $RPM_BUILD_ROOT%{_bindir}/mcserv $RPM_BUILD_ROOT%{_sbindir} 

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[18]/* FAQ NEWS README

%find_lang %{name}

%post -n mcserv
/sbin/chkconfig --add mcserv
if [ -f /var/lock/subsys/mcserv ]; then
     /etc/rc.d/init.d/mcserv restart >&2
else
	echo "Run \"/etc/rc.d/init.d/mcserv start\" to start mcserv daemon."
fi

%preun -n mcserv
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del mcserv
	/etc/rc.d/init.d/mcserv stop &>/dev/null
fi

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/mc
%attr(755,root,root) %{_bindir}/mcedit
%attr(755,root,root) %{_bindir}/mcmfmt

%{_libdir}/mc/mc.ext
%{_libdir}/mc/mc.hint
%{_libdir}/mc/mc.hlp
%{_libdir}/mc/mc.lib
%{_libdir}/mc/mc.menu

%attr(755,root,root) %{_libdir}/mc/bin/cons.saver

%attr(755,root,root) %{_libdir}/mc/extfs/a
%attr(755,root,root) %{_libdir}/mc/extfs/deb
%attr(755,root,root) %{_libdir}/mc/extfs/ftplist
%attr(755,root,root) %{_libdir}/mc/extfs/hp48
%attr(755,root,root) %{_libdir}/mc/extfs/lslR
%attr(755,root,root) %{_libdir}/mc/extfs/mailfs
%attr(755,root,root) %{_libdir}/mc/extfs/patchfs
%attr(755,root,root) %{_libdir}/mc/extfs/rpm
%attr(755,root,root) %{_libdir}/mc/extfs/uar
%attr(755,root,root) %{_libdir}/mc/extfs/uarj
%attr(755,root,root) %{_libdir}/mc/extfs/ucpio
%attr(755,root,root) %{_libdir}/mc/extfs/ulha
%attr(755,root,root) %{_libdir}/mc/extfs/urar
%attr(755,root,root) %{_libdir}/mc/extfs/uzip
%attr(755,root,root) %{_libdir}/mc/extfs/uzoo

%{_libdir}/mc/extfs/extfs.ini
%{_libdir}/mc/extfs/sfs.ini
%{_libdir}/mc/syntax

%{_mandir}/man1/*
%attr(755,root,root) %config /etc/profile.d/*

%dir %{_libdir}/mc
%dir %{_libdir}/mc/bin
%dir %{_libdir}/mc/extfs

%files -n mcserv
%defattr(644,root,root,755)

%attr(640,root,root) %config %verify(not size mtime md5) /etc/pam.d/*
%attr(640,root,root) %config %verify(not size mtime md5) /etc/sysconfig/*
%attr(755,root,root) %config /etc/rc.d/init.d/mcserv

%{_mandir}/man8/mcserv.8*

%attr(755,root,root) %{_sbindir}/mcserv

%changelog
* Fri May 21 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.5.31-1]
- spec written by me,
- pl translation by Wojtek �lusarczyk <wojtek@shadow.eu.org>.
- package is FHS 2.0 compliant.
