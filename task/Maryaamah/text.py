def get_text(prompt, field_name):
    """Get valid text input from the user."""

    while True:
        value = input(prompt).strip()

        # Check if input is empty
        if not value:
            print(f"Error: {field_name} cannot be empty.")
            continue

        # Check if input contains only numbers
        if value.isdigit():
            print(f"Error: {field_name} must contain text, not numbers.")
            continue

        return value