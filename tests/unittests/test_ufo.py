
def test_ql_version():
    from UfoPy import qlVersion
    version = qlVersion()
    assert isinstance(version, str)
    assert version.count('.') >= 1  # Basic check for version format
