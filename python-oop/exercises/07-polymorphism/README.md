# Exercise 07 — Polymorphism

**Difficulty**: 🟡 Intermediate

## Objective
Implement polymorphic interfaces and Duck Typing to process heterogeneous collections of academic items without type branching (`isinstance`).

## Scenario
Build a notification and billing dispatcher that can broadcast alerts across multiple delivery channels (Email, SMS, Portal Alert) and compute diverse assessment marks (Exams, Quizzes, Lab Practicals).

## Requirements
1. Implement three polymorphic Notifier classes:
   - `EmailNotifier`: `send(self, recipient: str, message: str) -> str` -> returns `f"[EMAIL] To: {recipient} | Body: {message}"`
   - `SMSNotifier`: `send(self, recipient: str, message: str) -> str` -> returns `f"[SMS] To: {recipient} | Body: {message}"`
   - `PushNotifier`: `send(self, recipient: str, message: str) -> str` -> returns `f"[PUSH] To: {recipient} | Body: {message}"`
2. Implement a dispatcher function:
   - `dispatch_broadcast(notifiers: list, recipient: str, message: str) -> list[str]`
   - Iterates through the collection of notifiers, calling `.send(recipient, message)` on each, and collects the results into a list.

## Starter Code
See [starter.py](starter.py).

## Expected Behavior
```text
All tests passed successfully! Polymorphic dispatch verified.
```
