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


def test_pip_list_shows_jinja(PipPackage):
    packages = PipPackage.get_packages()
    assert "Jinja2" in packages.keys()


def test_ansible_service_enabled(Service):
    svc = Service("redis")
    assert svc.is_enabled


def test_ansible_with_redis_caching_runs(Command):
    write_ansible_cfg = Command("echo -e '[defaults]\nfact_caching = redis' > /tmp/ansible_with_fact_caching.cfg")
    assert write_ansible_cfg.rc == 0
    run_ansible = Command("ANSIBLE_CONFIG=/tmp/ansible_with_fact_caching.cfg ansible localhost -a 'true'")
    assert run_ansible.rc == 0


def test_ansible_with_route53_runs(Command):
    cmd = Command("ansible localhost -m route53 -a 'zone=example.com command=get type=A record='")
    assert "boto required for this module" not in cmd.stdout
    # I don't want to bother with a one-off set of powerless credentials for
    # this test. I also don't want to really talk to AWS every time this test
    # runs. If we get as far as importing boto and trying to authenticate,
    # that's pretty good for an integration test.
    assert "boto.exception.NoAuthHandlerFound" in cmd.stdout
