from todoist.api import TodoistAPI

api = TodoistAPI('5cf5917694bdefcce55c52f3b21d5ef4f3778736')
api.sync()
projects = api.state['projects']


for project in projects:
    print(project['name'])
