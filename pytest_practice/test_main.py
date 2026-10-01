
#* Pytest fundamentals

#* What is pytest?
# pytest is a third-party testing framework for Python. It lets you
# write automated tests as plain functions (no boilerplate classes or
# imports required) and gives clear, detailed output when something
# fails. It's not part of the standard library - the built-in
# alternative is `unittest`, but pytest is simpler to write and is the
# most widely used testing tool in the Python ecosystem.

#* How it's used
# - Write test functions/files following pytest's naming conventions
#   (see "File & function naming rules" below) - no manual registration.
# - Run the `pytest` command in your terminal; it auto-discovers and
#   runs every matching test file in the project.
# - Use plain `assert` statements - pytest rewrites them to show exactly
#   which values differed on failure (no need for assertEqual, assertIn,
#   etc. like in unittest).
# - Extend behavior with fixtures (reusable setup/teardown), marks
#   (skip/xfail/custom tags), and parametrization (run one test with
#   many inputs) - all covered with examples below.

#* Where / when it's used
# - Unit testing: verifying individual functions/classes behave correctly.
# - Integration testing: checking that multiple components work together
#   (e.g. a function that calls a database or an API).
# - Regression testing: rerunning the full suite after changes to catch
#   anything that broke.
# - CI/CD pipelines: automatically run on every commit/PR (GitHub Actions,
#   GitLab CI, Jenkins, etc.) to catch bugs before they reach production.
# - Test-driven development (TDD): writing the test first, then the code
#   that makes it pass.
# - Used heavily for testing web apps/APIs (Flask, FastAPI, Django),
#   data pipelines, CLI tools, and general Python libraries.

#* Why pytest over plain assert scripts or unittest
# - Auto-discovery: no need to manually list which tests to run.
# - Rich plugin ecosystem: e.g. pytest-cov (coverage), pytest-mock
#   (mocking), pytest-django, pytest-asyncio.
# - Fixtures are more flexible/composable than unittest's setUp/tearDown.
# - Readable failure output out of the box.

# Install (if not already installed): pip install pytest
# Run all tests in this folder from the terminal:      pytest
#                                            (or):      python3 -m pytest
# Extra useful flags:
    # pytest -v                 - verbose, shows each test name + pass/fail
    # pytest -q                 - quiet, minimal output
    # pytest -k "divide"        - only run tests whose name matches "divide"
    # pytest test_main.py       - run only this file
    # pytest test_main.py::test_add   - run a single test function
    # pytest -x                 - stop after the first failing test
    # pytest --maxfail=2        - stop after 2 failures
    # pytest -s                 - don't capture print() output, show it live

#* File & function naming rules (test discovery)
    # - Test files must be named test_*.py or *_test.py
    # - Test functions must start with test_
    # - Test classes must start with Test (and must NOT define __init__)
    # - Methods inside a test class must also start with test_
    # pytest auto-discovers anything matching these patterns - no manual
    # registration needed.


import pytest
from main import add, subtract, divide, is_even, greet, Counter


#* Basic test - just use plain `assert`
# No special assertEqual/assertTrue methods like unittest - pytest
# rewrites plain `assert` statements to give detailed failure output.
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 2) == 3


#* Testing multiple related things in one test is fine as long as
    # - they're testing the same behavior/unit - keep unrelated checks in
    # - separate test functions so failures are easy to pinpoint.
def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False


#* Testing that an exception is raised: pytest.raises()
    # - Use it as a context manager. The test FAILS if the exception is not
    # - raised inside the `with` block.
def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_divide():
    assert divide(10, 2) == 5


# You can also inspect the exception message via `as excinfo`
def test_greet_empty_name_raises():
    with pytest.raises(ValueError, match="must not be empty"):
        greet("")


#* Comparing floats: use pytest.approx
    # Floating point math is imprecise (0.1 + 0.2 != 0.3 exactly), so
    # never compare floats with plain ==.
def test_float_division_approx():
    assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)


#* Fixtures - reusable setup (and teardown) for tests
    # A fixture is a function decorated with @pytest.fixture. Any test that
    # takes a parameter with the SAME NAME as the fixture will automatically
    # receive its return value. Pytest handles the wiring - no manual calls.
@pytest.fixture
def counter():
    # --- setup ---
    c = Counter(start=0)
    yield c  # this is the value injected into the test
    # --- teardown (runs after the test, even if it fails) ---
    # anything after `yield` runs as cleanup, e.g. closing files/connections.
    c.reset()


def test_counter_increment(counter):
    # `counter` here is the fresh Counter instance from the fixture above
    assert counter.value == 0
    counter.increment()
    counter.increment(step=5)
    assert counter.value == 6


#* Fixture scope
# By default a fixture runs fresh for every test (scope="function").
# Other scopes: "class", "module", "session" - use them to share
# expensive setup (e.g. a DB connection) across multiple tests instead
# of recreating it every time.
#   @pytest.fixture(scope="module")
#   def db_connection():
#       ...

#* conftest.py
# If multiple test files need the same fixture, don't redefine it in
# every file - put it in a file named conftest.py in this folder.
# Pytest automatically discovers conftest.py and makes its fixtures
# available to every test file in the same directory (and subdirectories),
# with no import needed.


#* Parametrize - run the same test with multiple sets of inputs
# Avoids copy-pasting near-identical test functions. Each tuple becomes
# a separate, individually reported test case.
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, -1, -2),
        (100, -50, 50),
    ],
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


#* Marks - tagging tests with special behavior

# Skip a test unconditionally (e.g. feature not implemented yet)
@pytest.mark.skip(reason="not implemented yet")
def test_future_feature():
    assert False


# Skip conditionally
@pytest.mark.skipif(1 > 0, reason="example condition")
def test_skip_example():
    assert False


# Mark a test as "expected to fail" - it still runs, but a failure
# doesn't count against the test suite (shown as "xfail" not "FAILED").
# If it unexpectedly passes, pytest reports "XPASS".
@pytest.mark.xfail(reason="known bug, fix pending")
def test_known_bug():
    assert 1 == 2


#* Capturing printed output: the `capsys` built-in fixture
# pytest ships several built-in fixtures you can use without defining
# them yourself. capsys captures stdout/stderr so you can assert on
# what a function printed.
def test_print_output(capsys):
    print("hello from a test")
    captured = capsys.readouterr()
    assert captured.out == "hello from a test\n"


#* Grouping tests in a class (optional)
# Useful for organizing related tests together. Class must start with
# "Test", methods must start with "test_", and `self` is NOT a fixture -
# don't rely on instance state persisting between tests (a new instance
# is created per test method).
class TestGreet:
    def test_valid_name(self):
        assert greet("Dheeraj") == "Hello, Dheeraj!"

    def test_empty_name_raises(self):
        with pytest.raises(ValueError):
            greet("")
