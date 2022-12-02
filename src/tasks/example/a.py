import os
import time
from typing import Any, Optional

from bb.task import task


@task("example.a.foo")
def task_a_foo(a: Any, b: Any) -> None:
    """task_a_foo"""
    print(f"task_a_foo({a}, {b}) called in {os.environ['BB_ENV']}")


@task("example.a.bar")
def task_a_bar(a: Any, b: Any, x: Optional[Any] = "X") -> None:
    """task_a_bar - demonstrate optional args"""
    print(f"task_a_bar({a}, {b}, {x}) called in {os.environ['BB_ENV']}")


@task("example.a.snooze")
def task_a_snooze(a: Any, b: Any) -> None:
    """task_a_snooze"""
    print(f"task_a_snooze({a}, {b}) is snoozing in {os.environ['BB_ENV']}")
    time.sleep(3)
    print(f"task_a_snooze({a}, {b}) is awake in {os.environ['BB_ENV']}")
