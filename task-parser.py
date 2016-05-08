import sys, json

try:
    # Try to decode a JSON
    tasks = json.load(sys.stdin)
    tasks_description = []

    # Get description for each task
    for task in tasks:
        tasks_description.append(task['description'])

    # Print result
    print ' ; '.join(tasks_description)
except ValueError:
    pass
