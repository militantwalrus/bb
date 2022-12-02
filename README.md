# BB tool

## bin/bb

The actual cli tool to invoke

## src/tasks

Subdirectories under here contain `.py` files which ONLY define the task functions.

## src/lib

Subdirectories under herea contain ONLY files supplying "helper" (lib) CONSTANTS, functions and classes


## Examples (runnable based on the provided files under `src/tasks`

`/path/to/bin/bb --env stg example.a.foo a=1 b=2`

`/path/to/bin/bb --env stg example.a.snooze a=1 b=2`

`/path/to/bin/bb --env stg example.a.bar a=1 b=2   # also has parameter 'x' which is optional`

See also `/path/to/bb -h`
