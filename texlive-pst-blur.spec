# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-blur
# catalog-date 2006-12-19 19:38:44 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-pst-blur
Version:	2.0
Release:	10
Summary:	PSTricks package for "blurred" shadows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-blur
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-blur.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-blur.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-blur.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pst-blur is a package built for use with PSTricks. It provides
macros that apply blurring to the normal shadow function of
PSTricks.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-blur/pst-blur.pro
%{_texmfdistdir}/tex/generic/pst-blur/pst-blur.tex
%{_texmfdistdir}/tex/latex/pst-blur/pst-blur.sty
%doc %{_texmfdistdir}/doc/generic/pst-blur/Changes
%doc %{_texmfdistdir}/doc/generic/pst-blur/README
%doc %{_texmfdistdir}/doc/generic/pst-blur/pst-blur.pdf
#- source
%doc %{_texmfdistdir}/source/generic/pst-blur/Makefile
%doc %{_texmfdistdir}/source/generic/pst-blur/pst-blur.dtx
%doc %{_texmfdistdir}/source/generic/pst-blur/pst-blur.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 755223
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 719336
- texlive-pst-blur
- texlive-pst-blur
- texlive-pst-blur
- texlive-pst-blur

