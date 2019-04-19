# from todoist import TodoistAPI
# api = TodoistAPI('5cf5917694bdefcce55c52f3b21d5ef4f3778736')
# api.sync()
# print(api.state['projects'])
#
# [
#   Project({
#     'collapsed': 0,
#     'color': 7,
#     'id': 176637162,
#     'inbox_project': True,
#     'indent': 1,
#     'is_archived': 0,
#     'is_deleted': 0,
#     'item_order': 0,
#     'name': 'Inbox',
#     'shared': False
#   })
# ]

import todoist
api = todoist.TodoistAPI('0123456789abcdef0123456789abcdef01234567')
api.sync()
full_name = api.state['user']['full_name']
print(full_name)
