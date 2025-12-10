
import random
import time


def test_simulated_network_call():
    """
    Example 1: Simulated network/API call flakiness
    
    Real-world scenario: Tests that make actual network calls can fail due to:
    - Network timeouts
    - API rate limits
    - Service downtime
    - DNS issues
    
    SOLUTION: Always mock external dependencies in unit tests!
    Use integration tests with retries for actual network testing.
    """
    # Simulate network call with 70% success rate
    responses = ['200 OK'] * 7 + ['timeout'] * 2 + ['503 Error'] * 1
    response = random.choice(responses)
    
    print(f"API Response: {response}")
    print("In real tests: Use requests-mock or responses library")
    print("See: pytest-vcr, responses, requests-mock")
    
    assert response == '200 OK', (
        f"API call failed: {response}. "
        f"Mock external calls to make tests deterministic!"
    )


def test_floating_point_comparison_issue():
    """
    Example 2: Floating-point precision problems
    
    Classic flakiness: Comparing floats with == can fail due to
    precision issues. The behavior can vary based on:
    - Compiler optimizations
    - CPU architecture
    - Order of operations
    
    SOLUTION: Use pytest.approx() or math.isclose() for float comparisons.
    """
    # Perform floating-point operations
    values = [random.random() * 0.1 for _ in range(5)]
    result = sum(values)
    
    expected_range = (0.2, 0.6)
    
    print(f"Sum of random values: {result}")
    print(f"Expected range: {expected_range}")
    print("\nFor float comparisons, use:")
    print("  assert result == pytest.approx(expected, rel=1e-3)")
    
    # This is flaky due to randomness
    assert expected_range[0] < result < expected_range[1], (
        f"Result {result} outside expected range {expected_range}"
    )


def test_resource_contention():
    """
    Example 3: Resource contention and state pollution
    
    Tests can be flaky when they:
    - Share resources (files, databases, ports)
    - Don't clean up after themselves
    - Run in parallel and interfere with each other
    
    SOLUTION: Use fixtures with proper setup/teardown, tmp_path, and isolation.
    """
    # Simulate multiple operations competing for resources
    success_count = 0
    
    for _ in range(5):
        # Simulate operation that might fail under contention
        if random.random() > 0.3:
            success_count += 1
    
    print(f"Successful operations: {success_count}/5")
    print("In real tests: Use fixtures, tmp_path, and proper isolation")
    print("See: tests/03_simple_fixture_test.py, tests/16_scoped_fixtures_test.py")
    
    assert success_count >= 4, (
        f"Only {success_count}/5 operations succeeded. "
        f"Resource contention simulation. Use fixtures for isolation!"
    )


def test_probability_based_assertion():
    """
    Example 4: Probability-based assertions (ANTIPATTERN)
    
    Never write assertions that "should usually pass" based on probability.
    If you need to test probabilistic behavior, test the underlying
    distribution or randomness properly with statistical tests.
    
    This test "should" pass 60% of the time - terrible practice!
    """
    attempts = [random.random() > 0.5 for _ in range(5)]
    successes = sum(attempts)
    
    print(f"Random attempts: {attempts}")
    print(f"Successes: {successes}/5")
    print("\nDon't test probability with assertions!")
    print("Instead: Mock the random behavior or use statistical tests")
    
    # Bad: Probabilistic assertion (passes ~66% of time)
    assert successes >= 3, (
        f"Only {successes}/5 attempts succeeded. "
        f"Probabilistic assertions are always flaky!"
    )


def test_order_dependency_simulation():
    """
    Example 5: Test order dependencies
    
    Tests should be independent and work in any order.
    This test demonstrates how order-dependent tests become flaky
    when test execution order changes.
    
    SOLUTION: Use fixtures, avoid shared state, use pytest-randomly.
    """
    # Simulate checking some "state" that might be set by another test
    # In reality, test order shouldn't matter!
    
    # Random simulation of whether "setup" happened
    was_setup = random.choice([True, False])
    
    print(f"Required setup detected: {was_setup}")
    print("\nMake tests independent!")
    print("Run with: pytest --random-order")
    
    assert was_setup, (
        "Test failed due to setup not running. "
        "Tests must be independent of execution order!"
    )