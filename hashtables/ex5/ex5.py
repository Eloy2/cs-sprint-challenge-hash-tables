# Your code here
def get_file(x): # reads file name backwards until it reaches "/". then returns file name
    file = ""
    for i in reversed(x):
        if i == "/":
            return "".join(reversed(file))
        else:
            file += i


def finder(files, queries):
    """
    The function simply adds all queries to a table. Then it checks if the path contains the query.
    If it does it will add it to the result array.
    """
    table = {}
    result = []
    for i in queries: # Add all values to table so we can make quick checks in line 20
        table[i] = None
    for i in files:
        if get_file(i) in table:    # Since we have our values in a hash table the checks on this line are quick.
            result.append(i)        # They would be extremely slow if we placed them in an array.

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
