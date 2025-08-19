from pendragondi_api_pro import duplicate_guard, get_event_log

@duplicate_guard
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeted {name}"

# First call - normal
greet('Jin')

# Second call - DUPLICATE DETECTED!
greet('Jin')  

# Show what was captured
events = get_event_log().snapshot()
if events:
    print(f"\n⚠️ Detected {len(events)} duplicate calls!")
    print(f"Function: {events[0]['function']}")
    print(f"Location: {events[0]['file']}:{events[0]['def_line']}")
