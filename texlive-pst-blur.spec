%global tl_name pst-blur
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	PSTricks package for blurred shadows
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-blur
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-blur.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-blur.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-blur.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Pst-blur is a package built for use with PSTricks. It provides macros
that apply blurring to the normal shadow function of PSTricks.

