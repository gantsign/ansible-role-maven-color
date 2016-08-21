def test_maven_color(Command):
    assert Command("mvn help:help").rc == 0

    # Need to run with bash for ANSI-C Quoting support
    cmd = Command("bash -c \"mvn help:help -Dmaven.color=true | grep -Eq $'\\e'\"")
    assert cmd.rc == 0
