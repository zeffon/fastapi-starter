# merge and deduplicate
def merge_and_deduplicate(array1, array2, key):
    seen = set()
    result = []
    for item in array1 + array2:
        if item[key] not in seen:
            seen.add(item[key])
            result.append(item)

    return result