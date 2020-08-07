# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    lookup = {}
    result = []

    for x in files:
        filename = x.split("/")[-1]
        if filename not in lookup:
            lookup[filename] = []
        lookup[filename].append(x)

    for x in queries:
        if x in lookup:
            result.extend(lookup[x])

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
