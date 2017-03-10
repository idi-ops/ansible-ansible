Role Name
=========

Minimal Ansible role to manage Ansible (and Jinja) with Pip on CentOS 7.3.

Requirements
------------

 * CentOS 7.x
 * Ansible 2.x

Role Variables
--------------
Name of ansible package in pip

    ansible_pip_ansible_package_name: ansible

Version of ansible package to install from pip

    ansible_pip_ansible_package_version: 2.2.1.0

Version of pip package to install from yum

    ansible_yum_pip_package_version: 8.1.2

Pip package (and supporting packages) to install from yum

    ansible_yum_pip_packages:
      - "python2-pip-{{ ansible_yum_pip_package_version }}"
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

License
-------

MIT

Author Information
------------------

Raising the Floor - US
