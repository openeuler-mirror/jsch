Name:           jsch
Version:        0.1.55
Release:        1
Summary:        A Pure Java implementation of SSH2
License:        BSD
URL:            http://www.jcraft.com/jsch/
BuildArch:      noarch
Source0:        http://download.sourceforge.net/sourceforge/jsch/jsch-%{version}.zip
Source1:        MANIFEST.MF
Source2:        plugin.properties
BuildRequires:  maven-local mvn(com.jcraft:jzlib) mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:) zip
Requires:       jzlib >= 0:1.0.5
Obsoletes:      %{name}-demo < %{version}

%description
JSch is a pure Java implementation of SSH2. JSch allows you to
connect to an sshd server and use port forwarding, X11 forwarding,
file transfer, etc., and you can integrate its functionality
into your own Java programs. JSch is licensed under BSD style license.

%package        help
Summary:        This package contains help documents
Requires:       %{name} = %{version}-%{release}
Provides:       jsch-javadoc = %{version}-%{release}
Obsoletes:      jsch-javadoc < %{version}-%{release}

%description      help
Files for help with jsch.

%prep
%autosetup -n %{name}-%{version} -p1
%mvn_file : jsch
%pom_remove_plugin :maven-javadoc-plugin
%pom_xpath_remove pom:project/pom:build/pom:extensions
%pom_xpath_set pom:project/pom:version %{version}
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]//pom:target'

%build
%mvn_build
install -d META-INF
install -D %{SOURCE1} META-INF
install -D %{SOURCE2} plugin.properties
touch META-INF/MANIFEST.MF
touch plugin.properties
zip target/%{name}-%{version}.jar META-INF/MANIFEST.MF
zip target/%{name}-%{version}.jar plugin.properties

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files help -f .mfiles-javadoc

%changelog
* Wed Jun 15 2022 SimpleUpdate Robot <tc@openeuler.org> - 0.1.55-1
- Upgrade to version 0.1.55

* Thu Dec 12 2019 gulining<gulining1@huawei.com> - 0.1.54-8
- Pakcage init
