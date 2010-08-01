# TODO:
# - check spec-syntax,mo patches
#
# Conditional build:
%bcond_with	ext2undel	# with ext2 undelete fs
%bcond_without	perl_vfs	# without perl depending vfs'es -- to avoid perl autoreq
%bcond_with	samba		# with SAMBA vfs support
%bcond_without	x		# without text edit in X support
#
Summary:	A user-friendly file manager and visual shell
Summary(de.UTF-8):	Visuelle Shell Midnight Commander
Summary(es.UTF-8):	Interpretador de comandos visual Midnight Commander
Summary(fr.UTF-8):	Un gestionnaire de fichiers puissant et agréable en mode console
Summary(hu.UTF-8):	Egy felhasználóbarát fájlkezelő és vizuális shell
Summary(ja.UTF-8):	使いやすいファイルマネージャとビジュアルシェル
Summary(pl.UTF-8):	Midnight Commander - powłoka wizualna
Summary(pt_BR.UTF-8):	Interpretador de comandos visual Midnight Commander
Summary(ru.UTF-8):	Диспетчер файлов Midnight Commander
Summary(tr.UTF-8):	Midnight Commander görsel kabuğu
Summary(uk.UTF-8):	Диспетчер файлів Midnight Commander
Summary(zh_CN.UTF-8):	一个方便实用的文件管理器和虚拟Shell
Name:		mc
Version:	4.7.3
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/Shells
Source0:	http://www.midnight-commander.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	42eb806d733b11d0d13ff7ee5fd1a03c
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	17d7b574e1b85ad6f8ddceda9e841f19
Source7:	%{name}.desktop
Source8:	%{name}.png
Patch0:		%{name}-rpmfs.patch
Patch1:		slang-8bit_xterm.patch
Patch2:		%{name}-down2.diff
Patch4:		%{name}-home_etc2.patch
Patch5:		%{name}-pl.patch
Patch6:		%{name}-no-ws-visible.patch
Patch7:		changeset_rce12059b0e7c7df3b7a1ebc908d48e4eb3b454e5.diff
Patch8:		changeset_r2ac7aeadc8560e8830877677192d0c28290c6a33.diff
Patch9:		changeset_r3322964fbf59f46c49fff2f27d5be86f3d2fde84.diff
Patch11:	%{name}-noperl-vfs.patch
# at now syntax highligthing for PLD-update-TODO and CVSROOT/users
Patch12:	%{name}-pld-developerfriendly.patch
Patch17:	%{name}-nolibs.patch
Patch24:	%{name}-find_options.patch
URL:		http://www.midnight-commander.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_ext2undel:BuildRequires:	e2fsprogs-devel}
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.8
%ifnarch s390 s390x
BuildRequires:	gpm-devel
%endif
BuildRequires:	libtool
BuildRequires:	pam-devel
# Needed? %%{?with_perl_vfs:Requires:	perl-base}
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	slang-devel >= 2.2.1
%{?with_x:BuildRequires:	xorg-lib-libX11-devel}
Requires:	file
Requires:	pam >= 0.77.3
Requires:	sed
Requires:	setup >= 2.4.6-2
Suggests:	bzip2
Suggests:	cabextract
Suggests:	cdrtools-utils
Suggests:	cpio
Suggests:	dvi2tty
Suggests:	enca
Suggests:	file
Suggests:	ghostscript
Suggests:	groff
Suggests:	gzip
Suggests:	lha
Suggests:	links
Suggests:	lynx
Suggests:	lzma
Suggests:	odt2txt
Suggests:	p7zip-standalone
Suggests:	perl-tools-pod
Suggests:	rar
Suggests:	rpm-utils
Suggests:	tar
Suggests:	unarj
Suggests:	unzip
Suggests:	xdg-utils
Suggests:	xpdf-tools
Suggests:	xz
Suggests:	zoo
Obsoletes:	mc46
Obsoletes:	mc46serv
Obsoletes:	mcserv
Obsoletes:	tkmc
Conflicts:	bash < 2.05b
Conflicts:	rpm < 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	-fomit-frame-pointer

%description
Midnight Commander is a visual shell much like a file manager, only
with way more features. It is text mode, but also includes mouse
support if you are running GPM. Its coolest feature is the ability to
FTP, view tar, zip files, and poke into RPMs for specific files. :-)

%description -l de.UTF-8
Midnight Commander ist ein Visual-Shell, ähnlich einem Dateimanager,
aber mit zusätzlichen Funktionen. Es läuft im Textmodus, kann jedoch
eine Maus unterstützen, wenn GPM betrieben wird. Seine coolsten
Fähigkeiten sind die FTP-Option, das Einsehen von tar- und zip-Dateien
und das Herausfischen von spezifischen Dateien aus RPMs.

%description -l es.UTF-8
Midnight Commander es un interpretador de comandos visual que más
parece un administrador de archivos, solamente con varias
características a más. Es un programa en modo texto, pero incluye
soporte para ratón, si estuviera ejecutando GPM o en una ventana
xterm. Su característica más genial es la habilidad de cotillear en
RPMs buscando archivos específicos. :-)

%description -l fr.UTF-8
Midnight Commander est une interface pour la ligne de commande qui
tient beaucoup du gestionnaire de fichiers, mais est bien plus
puissant. Il fonctionne en mode console (texte), mais peut être
contrôlé à la souris si GPM est présent. Ses caractéristiques les plus
remarquables sont la possibilité de se connecter à un serveur FTP, de
visualiser des archives tar, de compresser des fichiers avec zip, de
récupérer des fichiers dans les packages RPM, et tout ceci simplement.

%description -l hu.UTF-8
Midnight Commander egy vizuális shell, lényegében egy fájlkezelő
sok-sok lehetőséggel. Szöveges módú, de az egeret is támogatja, ha fut
a GPM. A legjobb lehetőség az FTP elérése, tar, zip és RPM fájlok
kezelése.

%description -l ja.UTF-8
Midnight Commander はいろいろな機能を持ったファイルマネージャ兼
ビジュアルシェルです。これはテキストモードのアプリケーションですが、 GPM を使っている場合、マウスが使えます。 Midnight
Commander には、 FTP に接続できたり、 tar や zip や RPM の中が見えるなど、クールな機能 があります。

%description -l pl.UTF-8
Midnight Commander jest wizualną powłoką podobną do Norton Commandera.
Pracuje w trybie tekstowym, ale ma także obsługę myszki. Jest super ;)
MC ma wbudowanego klienta FTP, może zaglądać do skompresowanych
archiwów tar i zip, a także oglądać pliki w pakietach RPM.

%description -l pt_BR.UTF-8
Midnight Commander é um interpretador de comandos visual que mais
parece um gerenciador de arquivos, somente com várias características
a mais. Ele é um programa de modo texto, mas inclui suporte para mouse
se você estiver rodando GPM ou em uma janela xterm. Sua característica
mais legal é a habilidade de bisbilhotar em RPMs procurando arquivos
específicos. :-)

%description -l tr.UTF-8
Midnight Commander bir dosya yöneticisine çok benzeyen ancak daha
yetenekli bir görsel kabuktur. Metin ekranda çalışır ve GPM
çalışıyorsa fare desteği vardır. En hoş özellikleri FTP yapabilmesi,
tar, zip ve RPM dosyalarının içeriklerini gösterebilmesidir.

%prep
%setup -q -a3
#rpm wrapper rewritten
#%patch0 -p1
%patch1 -p1
%patch2 -p1
# doesn't apply
#%patch4 -p1
# doesn't apply
#%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p0
%patch9 -p0
%{!?with_perl_vfs:%patch11 -p1}
%patch12 -p1
%patch17 -p1
%if "%{pld_release}" == "ti"
%patch24 -p1
%endif

rm -f po/stamp-po

sed -i 's:|hxx|:|hh|hpp|hxx|tcc|:' misc/syntax/Syntax

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}

export X11_WWW="xdg-open"
%configure \
	--with%{!?debug:out}-debug \
	--with%{!?with_ext2undel:out}-ext2undel \
	--with%{!?with_x:out}-x \
	--with-vfs \
	%{?with_samba:--with-samba} \
	--with-configdir=/etc/samba \
	--with-codepagedir=/etc/samba/codepages \
	--with-gpm-mouse \
	--with-screen=slang

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_pixmapsdir},%{_desktopdir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,shrc.d,sysconfig} \
	$RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE7} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE8} $RPM_BUILD_ROOT%{_pixmapsdir}

for a in es pl ; do
	for b in man1 man8 ; do
		install -d $RPM_BUILD_ROOT%{_mandir}/{$a,$a/$b}
		for c in man/$a/$b/* ; do
			install $c $RPM_BUILD_ROOT%{_mandir}/$a/$b
		done
	done
done

install contrib/{mc.sh,mc.csh} $RPM_BUILD_ROOT/etc/shrc.d

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/be-tarask

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/mc*
%config /etc/shrc.d/*
%attr(755,root,root) %{_libdir}/mc/cons.saver
%dir %{_libdir}/mc
%attr(755,root,root) %{_libdir}/mc/*.sh
%attr(755,root,root) %{_libdir}/mc/*.csh
%dir %{_datadir}/mc

%{_datadir}/mc/skins
%{_datadir}/mc/syntax

%{_datadir}/mc/mc.hlp
%lang(es) %{_datadir}/mc/mc.hlp.es
%lang(hu) %{_datadir}/mc/mc.hlp.hu
%lang(it) %{_datadir}/mc/mc.hlp.it
%lang(pl) %{_datadir}/mc/mc.hlp.pl
%lang(ru) %{_datadir}/mc/mc.hlp.ru
%lang(sr) %{_datadir}/mc/mc.hlp.sr
%{_datadir}/mc/mc.hint
%lang(cs) %{_datadir}/mc/mc.hint.cs
%lang(es) %{_datadir}/mc/mc.hint.es
%lang(hu) %{_datadir}/mc/mc.hint.hu
%lang(it) %{_datadir}/mc/mc.hint.it
%lang(nl) %{_datadir}/mc/mc.hint.nl
%lang(pl) %{_datadir}/mc/mc.hint.pl
%lang(ru) %{_datadir}/mc/mc.hint.ru
%lang(sr) %{_datadir}/mc/mc.hint.sr
%lang(uk) %{_datadir}/mc/mc.hint.uk
%lang(zh) %{_datadir}/mc/mc.hint.zh

%dir %{_libdir}/mc/extfs.d
%{_libdir}/mc/extfs.d/README*
%if %{with perl_vfs}
%attr(755,root,root) %{_libdir}/mc/extfs.d/a+
%attr(755,root,root) %{_libdir}/mc/extfs.d/apt+
%attr(755,root,root) %{_libdir}/mc/extfs.d/deb*
%attr(755,root,root) %{_libdir}/mc/extfs.d/dpkg+
%attr(755,root,root) %{_libdir}/mc/extfs.d/mailfs
%attr(755,root,root) %{_libdir}/mc/extfs.d/patchfs
%attr(755,root,root) %{_libdir}/mc/extfs.d/rpms+
%attr(755,root,root) %{_libdir}/mc/extfs.d/uzip
%endif
%attr(755,root,root) %{_libdir}/mc/extfs.d/audio
%attr(755,root,root) %{_libdir}/mc/extfs.d/bpp
%attr(755,root,root) %{_libdir}/mc/extfs.d/hp48+
%attr(755,root,root) %{_libdir}/mc/extfs.d/iso9660
%attr(755,root,root) %{_libdir}/mc/extfs.d/lslR
%attr(755,root,root) %{_libdir}/mc/extfs.d/rpm
%attr(755,root,root) %{_libdir}/mc/extfs.d/s3+
%attr(755,root,root) %{_libdir}/mc/extfs.d/trpm
%attr(755,root,root) %{_libdir}/mc/extfs.d/u7z
%attr(755,root,root) %{_libdir}/mc/extfs.d/uace
%attr(755,root,root) %{_libdir}/mc/extfs.d/ualz
%attr(755,root,root) %{_libdir}/mc/extfs.d/uar*
%attr(755,root,root) %{_libdir}/mc/extfs.d/uc1541
%attr(755,root,root) %{_libdir}/mc/extfs.d/ucab
%attr(755,root,root) %{_libdir}/mc/extfs.d/uha
%attr(755,root,root) %{_libdir}/mc/extfs.d/ulha
%attr(755,root,root) %{_libdir}/mc/extfs.d/urar
%attr(755,root,root) %{_libdir}/mc/extfs.d/uzoo
%dir %{_libdir}/mc/fish
%{_libdir}/mc/fish/README.fish
%attr(755,root,root) %{_libdir}/mc/fish/[a-z]*
%{_desktopdir}/mc.desktop
%{_pixmapsdir}/mc.png

%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%lang(sr) %{_mandir}/sr/man1/*

%dir %{_sysconfdir}/mc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mc/Syntax
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mc/*.*
