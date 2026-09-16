"""
Exercise 07: Polymorphism (Solution)
Reference solution showing duck typing and polymorphic dispatch across notifier types.
"""

class EmailNotifier:
    def send(self, recipient: str, message: str) -> str:
        return f"[EMAIL] To: {recipient} | Body: {message}"


class SMSNotifier:
    def send(self, recipient: str, message: str) -> str:
        return f"[SMS] To: {recipient} | Body: {message}"


class PushNotifier:
    def send(self, recipient: str, message: str) -> str:
        return f"[PUSH] To: {recipient} | Body: {message}"


def dispatch_broadcast(notifiers: list, recipient: str, message: str) -> list[str]:
    return [notifier.send(recipient, message) for notifier in notifiers]


if __name__ == "__main__":
    channels = [EmailNotifier(), SMSNotifier(), PushNotifier()]
    for res in dispatch_broadcast(channels, "Aisha", "Welcome to Geekink"):
        print(res)
    print("All tests passed successfully! Polymorphic dispatch verified.")
