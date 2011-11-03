# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-blur
# catalog-date 2006-12-19 19:38:44 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-pst-blur
Version:	2.0
Release:	1
Summary:	PSTricks package for "blurred" shadows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-blur
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-blur.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-blur.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-blur.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Pst-blur is a package built for use with PSTricks. It provides
macros that apply blurring to the normal shadow function of
PSTricks.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
