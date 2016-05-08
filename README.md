# Simple task parser

This is a simple task parser for [Taskwarrior](https://taskwarrior.org/), that extracts the description of each task
and prints them all separated by a semicolon. It only works with the JSON exporter of Taskwarrior.

# Usage

```bash
task [filters] export | python task-parser.py
```

## Print all pending tasks

```bash
task status:pending export | python task-parser.py
```

## Print all pending tasks with due for today

```bash
task status:pending due:today export | python task-parser.py
```

## Print all tasks, even those already finished

```bash
task status:pending | python task-parser.py
```