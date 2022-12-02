import os
from typing import Any, Optional

from bb.task import task


@task("other_example.b.foo")
def task_b_foo(a: Any, b: Any) -> None:
    """task_b_foo"""
    print(f"other_task_b_foo({a}, {b}) called in {os.environ['BB_ENV']}")


@task("other_example.b.bar")
def task_b_bar(a: Any, b: Any, x: Optional[Any] = "X") -> None:
    """task_b_bar"""
    print(f"other_task_b_bar({a}, {b}, {x}) called in {os.environ['BB_ENV']}")
