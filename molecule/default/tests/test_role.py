import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_maven_color(host):
    assert host.run("mvn help:help").rc == 0

    # Need to run with bash for ANSI-C Quoting support
    cmd = host.run("bash -c %s",
                   "mvn help:help -Dmaven.color=true | grep -Eq $'\e'")
    assert cmd.rc == 0
