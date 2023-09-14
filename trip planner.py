def print_my_name(name):
    print(name)

    print_my_name("billy bob joe")

def trip_planner(start, end, duration, mode):
    print(f"it looks like you are starting your trip from {start}")
    print(f"you are planning to go to {end}")
    print(f"it should take you about {duration} hours")
    print(f"i see you are taking a {mode}")

trip_planner('paradigm', 'disney land', 2, 'plane')