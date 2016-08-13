Ansible Role: Maven Color
=========================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-maven-color.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-maven-color)

Role to install the Maven Color extension for Maven
[https://github.com/jcgay/maven-color](https://github.com/jcgay/maven-color).

Requirements
------------

Ubuntu with Maven >= 3.1 installed.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Maven Color version number
maven_color_version: '1.6.0'

# Location of the Maven installation to add the Maven Color extension to.
maven_color_maven_home: "{{ ansible_local.maven.general.maven_home }}"

# Mirror where to download Maven Color redistributable package from.
maven_color_mirror: "http://dl.bintray.com/jcgay/maven/com/github/jcgay/maven/color/maven-color-logback/{{ maven_color_version }}"

# SHA256 sum for the redistributable package
maven_color_redis_sha256sum: f5fd594d1cbeba136bc79dfb43a876c5fa49083f97e37fbec81df65dfc87a25b

# path for Ansible to store downloaded files
local_ansible_data_path: '/tmp/ansible/data'
```

Note: if you install Maven using `groover.maven` role it will set the fact
`ansible_local.maven.general.maven_home`, which this role uses as the default
value for the Maven installation directory. If you install Maven without setting
the fact you will have to specify `maven_color_maven_home`.

Example Playbook
----------------

If you install Maven using `groover.maven` this role can be used as follows:

```yaml
- hosts: servers
  roles:
     - { role: gantsign.maven-color }
```

If you install Maven using a different approach you'll need to specify the
Maven home:

```yaml
- hosts: servers
  roles:
     - { role: gantsign.maven-color, maven_color_maven_home: /opt/maven/apache-maven-3.3.9 }
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
