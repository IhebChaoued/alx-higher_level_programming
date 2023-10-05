#!/usr/bin/python3
if __name__ == "__main__":
    """Print EVERYTHING"""
    import hidden_4

    file = dir(hidden_4)
    for i in file:
        if i[:2] != "__":
            print(i)
