import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_yum_packages_not_installed(Package):
    ansible_pkg = Package("ansible")
    assert not ansible_pkg.is_installed

    jinja_pkg = Package("python-jinja2")
    assert not jinja_pkg.is_installed


def test_pip_installed(Package):
    pip_pkg = Package("python2-pip")
    assert pip_pkg.is_installed


def test_pip_list_shows_jinja(Command):
    cmd = Command("pip list")
    assert "Jinja2" in cmd.stdout
