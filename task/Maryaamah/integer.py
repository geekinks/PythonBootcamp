def get_integer(prompt, field_name, minimum=None, maximum=None):
    """Get a valid integer from the user."""

    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Error: {field_name} must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Error: {field_name} must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print(f"Error: Please enter a valid number for {field_name}.")
