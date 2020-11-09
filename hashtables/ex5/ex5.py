def finder(files, queries):
    result = []
    only_files = {}
    duplicates = {}
    for f in files:
        if f.find("/") == -1:
            only_files[f] = f
        split_f = f.split("/")
        last = len(split_f) - 1

        if split_f[last] not in only_files:
            only_files[split_f[last]] = f
        else:
            duplicates[split_f[last]] = f
    
    for q in queries:
        if q in only_files:
            result.append(only_files[q])
        if q in duplicates:
            result.append(duplicates[q])

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
