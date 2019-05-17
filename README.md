Ansible Role: Maven Color
=========================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-maven-color.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-maven-color)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.maven--color-blue.svg)](https://galaxy.ansible.com/gantsign/maven-color)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-maven-color/master/LICENSE)

This role installs the [Maven Color](https://github.com/jcgay/maven-color)
extension for Maven authored by
[Jean-Christophe Gay](https://github.com/jcgay).

**Deprecation notice:** this role is no longer maintained, please upgrade to Maven >= 3.5 instead of using this role.

Requirements
------------

* Ansible >= 2.5

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Trusty (14.04)
            * Xenial (16.04)
            * Bionic (18.04)

    * RedHat Family

        * CentOS

            * 6
            * 7

        * Fedora

            * 28

    * SUSE Family

        * openSUSE

            * 15.0

    * Note: other versions are likely to work but have not been tested.

* Maven >= 3.1

    * **Warning:** Maven must be installed from a standard `tar.gz` binary
      package; using this role to modify a copy of Maven installed by your
      Linux distributions package management tool (e.g. `apt-get install`) is
      not recommended.

    * **Recommendation:** use the
      [gantsign.maven](https://galaxy.ansible.com/gantsign/maven) role to
      install Maven.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Maven Color version number
maven_color_version: '1.6.0'

# Location of the Maven installation to add the Maven Color extension to.
maven_color_maven_home: '{{ ansible_local.maven.general.home }}'

# Mirror where to download Maven Color redistributable package from.
maven_color_mirror: 'http://dl.bintray.com/jcgay/maven/com/github/jcgay/maven/color/maven-color-logback/{{ maven_color_version }}'

# Directory to store files downloaded for Maven Color installation
maven_color_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

### Supported Maven Color Versions

The following versions of Maven Color are supported without any additional
configuration (for other versions follow the Advanced Configuration
instructions):

* `1.6.0`
* `1.4.1`

Advanced Configuration
----------------------

The following role variable is dependent on the Maven Color version; to use a
Maven Color version **not pre-configured by this role** you must configure the
variable below:

```yaml
# SHA256 sum for the redistributable package (i.e. maven-color-logback-{{ maven_color_version }}-bundle.tar.gz)
maven_color_redis_sha256sum: 'f5fd594d1cbeba136bc79dfb43a876c5fa49083f97e37fbec81df65dfc87a25b'
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.maven-color
      maven_color_maven_home: /opt/maven/apache-maven-3.3.9
```

Related Roles
-------------

You may find the following related roles useful:

* [gantsign.java](https://galaxy.ansible.com/gantsign/java) for installing the
  Oracle JDK.

* [gantsign.maven](https://galaxy.ansible.com/gantsign/maven) for installing
  Apache Maven.

* [gantsign.maven-notifier](https://galaxy.ansible.com/gantsign/maven-notifier)
  for providing a GUI notification when a build ends.

    * Installs the [Maven Notifier](https://github.com/jcgay/maven-notifier)
      extension for Maven authored by
      [Jean-Christophe Gay](https://github.com/jcgay).

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
