from __future__ import annotations

import importlib
import sys
from typing import TYPE_CHECKING, Callable, Dict, Iterable, Optional

if TYPE_CHECKING:
    from pathlib import PosixPath


def task(task_name):
    """
    Tag decorated functions so list_tasks() can identify them
    """

    def outer(fn):
        def inner(*args, **kwargs):
            fn(*args, **kwargs)

        inner._task_name = task_name
        return inner

    return outer


def find_task_files(task_dir: PosixPath) -> Iterable[PosixPath]:
    """
    Build a list of all the files which might contain task definitions

    NB! this will return __init__.py files, but perhaps that is fine
    """

    return [ent for ent in task_dir.rglob("*") if ent.is_file() and ent.name.endswith(".py")]


def _find_task_functions(task_dir: PosixPath) -> Dict[str, Callable]:
    """
    Given the directory where tasks are defined, generate a dictionary of
    {task_name: function obj}
    for each function been decorated with @task(task_name)
    """
    ret = {}
    for f in find_task_files(task_dir):
        modname = str(f.relative_to(task_dir)).replace("/", ".").strip(".py")

        # handle the (unwanted) case of tasks/__init__.py
        if modname == "__init__":
            continue

        importlib.import_module(modname)

        for k in sys.modules[modname].__dict__.keys():
            fn = getattr(sys.modules[modname], k, None)  # get the func obj
            maybe = getattr(fn, "_task_name", None)  # see if it has the @task() decoration
            if maybe:
                ret[maybe] = fn

    return ret


def find_task_to_run(task_name: str, task_dir: PosixPath) -> Optional[Callable]:
    """
    Given a task name from the bb invocation, look in the files
    for the function
    """

    tasks = _find_task_functions(task_dir)
    return tasks.get(task_name)


def list_tasks(task_dir: PosixPath) -> str:
    """
    Build a listing of task functions (those decorated with @task("..."))
    """

    tasks = _find_task_functions(task_dir)

    out = "\nAvailable tasks\n\n"

    for name in sorted(tasks):
        out += f"    {name}\n"

    out += "\n"

    return out
