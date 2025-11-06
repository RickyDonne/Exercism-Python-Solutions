def response(hey_bob):
    statement = hey_bob.strip()

    if statement == "":
        return "Fine. Be that way!"

    is_question = statement.endswith("?")

    has_letters = any(char.isalpha() for char in statement)
    is_yelling = statement.isupper() and has_letters

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."
