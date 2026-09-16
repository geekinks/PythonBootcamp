# Assignment 02 — Food Delivery System

> **Multi-Entity Collaboration, State Machines, and Order Lifecycles**

## 1. Project Overview
Design an online food delivery backend system (similar to Chowdeck or UberEats) connecting Customers, Restaurants, Menus, Orders, and Delivery Drivers.

---

## 2. Domain Entities & UML Diagram

```mermaid
classDiagram
    class MenuItem {
        +str item_id
        +str name
        +float price
        +bool is_available
    }

    class Restaurant {
        +str name
        +str address
        +List~MenuItem~ menu
        +add_item(item: MenuItem)
        +get_menu() List~MenuItem~
    }

    class Customer {
        +str customer_id
        +str name
        +str delivery_address
        +create_order(restaurant: Restaurant) Order
    }

    class Driver {
        +str driver_id
        +str name
        +bool is_available
        +accept_delivery(order: Order)
        +mark_delivered(order: Order)
    }

    class OrderStatus {
        <<enumeration>>
        PLACED
        PREPARING
        OUT_FOR_DELIVERY
        DELIVERED
        CANCELLED
    }

    class Order {
        +str order_id
        +Customer customer
        +Restaurant restaurant
        +List~MenuItem~ items
        +Driver driver
        +OrderStatus status
        +add_item(item: MenuItem)
        +calculate_total() float
        +transition_to(new_status: OrderStatus)
    }

    Restaurant *-- MenuItem : Composes Menu
    Customer --> Order : Places
    Order o-- MenuItem : Contains
    Order --> Restaurant : Belongs to
    Driver --> Order : Delivers
```

---

## 3. Core Functional Requirements

### 3.1 MenuItem & Restaurant
- `MenuItem`: Represents individual dishes with price validation (`price > 0`).
- `Restaurant`: Contains a menu of `MenuItem` objects (Composition). Supports adding items and querying availability.

### 3.2 Order Lifecycle Management
- An `Order` starts in `OrderStatus.PLACED`.
- State transitions must follow valid sequential flow:
  - `PLACED` -> `PREPARING` -> `OUT_FOR_DELIVERY` -> `DELIVERED`.
  - Illegal state transitions (e.g. `DELIVERED` -> `PREPARING`) must raise an `InvalidStateTransitionError`.

### 3.3 Driver Assignment
- A `Driver` can only be assigned to one active delivery at a time.
- When an order transitions to `OUT_FOR_DELIVERY`, an available driver is assigned and marked unavailable.
- When `mark_delivered` is invoked, the order is marked `DELIVERED` and the driver becomes available again.

---

## 4. Evaluation Checklist
- [ ] Proper use of Enums / Constants for order states.
- [ ] Strict state transition validations.
- [ ] Accurate computation of subtotal, delivery fees, and order totals.
- [ ] Clear separation between Customer, Restaurant, Order, and Driver responsibilities.
