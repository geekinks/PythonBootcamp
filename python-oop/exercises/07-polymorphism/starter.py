"""
Exercise 07: Polymorphism (Starter)
Complete the TODO items below and run this file to test your solution.
"""

# TODO 1: Implement EmailNotifier with send(self, recipient: str, message: str) -> str
class EmailNotifier:
    def send(self, recipient: str, message: str) -> str:
        return f"[EMAIL] To: {recipient} | Body: {message}"         
    pass


# TODO 2: Implement SMSNotifier with send(self, recipient: str, message: str) -> str
class SMSNotifier:
    def send(self, recipient: str, message: str) -> str:
        return f"[SMS] To: {recipient} | Body: {message}"               


# TODO 3: Implement PushNotifier with send(self, recipient: str, message: str) -> str
class PushNotifier:
    def send(self, recipient: str, message: str) -> str:
        return f"[PUSH] To: {recipient} | Body: {message}"                  


def dispatch_broadcast(notifiers: list, recipient: str, message: str) -> list[str]:
    # TODO 4: Iterate through notifiers, invoke .send(recipient, message), and return list of results
    results = []
    for notifier in notifiers:      
        results.append(notifier.send(recipient, message))                                        
    return results  


# --- Verification Tests (DO NOT MODIFY BELOW THIS LINE) ---
if __name__ == "__main__":
    email_channel = EmailNotifier()
    sms_channel = SMSNotifier()
    push_channel = PushNotifier()

    channels = [email_channel, sms_channel, push_channel]
    results = dispatch_broadcast(channels, "Aisha", "Registration Deadline is Tomorrow")

    assert len(results) == 3
    assert results[0] == "[EMAIL] To: Aisha | Body: Registration Deadline is Tomorrow"
    assert results[1] == "[SMS] To: Aisha | Body: Registration Deadline is Tomorrow"
    assert results[2] == "[PUSH] To: Aisha | Body: Registration Deadline is Tomorrow"

    print("All tests passed successfully! Polymorphic dispatch verified.")
