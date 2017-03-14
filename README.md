Role Name
=========

Minimal Ansible role to manage Ansible (and Jinja) with Pip on CentOS 7.3. This includes:

  * redis, the datastore, from yum installed, enabled, and started
  * redis, the python library, from pip
  * boto, the python library, for AWS (Route53) plays

Requirements
------------

 * CentOS 7.x
 * Ansible 2.x
 * systemd

Role Variables
--------------
Pip packages (and version numbers) to provide all the ansible functionality we need

ansible_pip_packages:
  - ansible==2.2.1.0
  - boto==2.46.1
  - dnspython==1.15.0  # For ansible "lookup('dig', ...)"
  - redis==2.10.5

Pip package (and supporting packages) to install from yum

    ansible_rpm_packages:
      - python2-pip-8.1.2
      - redis-3.2.3  # For fact caching
      - gcc-4.8.5  # Needed for 'pip install cryptography'
      - python-devel-2.7.5  # Needed for 'pip install cryptography'
      - openssl-devel-1.0.1e-60.el7_3.1  # Needed for 'pip install cryptography'

Example Playbook
----------------

    - hosts: servers
      roles:
         - ansible-ansible

Tests
-----

Use [molecule](https://github.com/metacloud/molecule) to test this role.

Because this role depends on systemd and might one day need SELinux (as related role ansible-influxdb does), only a Vagrant provider is configured at the moment.

License
-------

MIT

Author Information
------------------

Raising the Floor - US
