
calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    string = string.lower()
    return len(string), string.lower(), string.upper()
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for item in list_to_search:
        if item.lower() == string:
            return True
    return False
print(string_info('Картофель'))
print(string_info('Томат'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

