def generate_hashtag(s):
    # Step 1: Split the string into words
    words = s.split()
    if not words:   # if list is empty, return False
        return False

    # Step 2: Capitalize each word
    capitalized = [w.capitalize() for w in words]

    # Step 3: Join them and add '#'
    result = "#" + "".join(capitalized)

    # Step 4: Check length condition
    return result if len(result) <= 140 else False

print(generate_hashtag("hello world"))
print(generate_hashtag(""))
print(generate_hashtag("this is a really really long sentence that just keeps going and going and does not stop at all because we want to make sure it is longer than one hundred and forty characters for testing"))


