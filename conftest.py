from __future__ import print_function
from pytest import fixture


@fixture
def global_fixture():
    print("\n(Doing global fixture setup stuff!)")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "db: Example marker for tagging Database related tests"
    )
    config.addinivalue_line(
        "markers", "slow: Example marker for tagging extremely slow tests"
    )
    # Include flaky.py in test collection
    config.option.python_files = "test_*.py *_test.py flaky.py"
