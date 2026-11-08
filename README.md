# Virtual Garage & Vehicle System 🚗🏍️

A dynamic and structured simulation system built in Python using advanced **Object-Oriented Programming (OOP)** principles. This application models a virtual garage capable of managing, servicing, and tracking different types of vehicles like Cars, Motorcycles, and Trucks.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML).
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Learning Data Structures & Algorithms (DSA) and data science libraries like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Vehicle Cataloging:** Add, modify, and track multiple vehicle types (Cars, Bikes, Trucks) with unique properties (Model, Year, Fuel Type).
*   **Garage Capacity Management:** Tracks available parking slots inside the virtual garage and automatically blocks entry if the garage is full.
*   **Service & Maintenance Simulator:** Tracks individual vehicle health, schedules oil changes or tune-ups, and updates service history status.
*   **Dynamic Operations:** Simulates real-time actions like parking a vehicle, fetching a vehicle by its license plate, and releasing it.

---

## 🛠️ OOP Concepts Implemented

This project is the perfect demonstration of architectural design using core **OOP principles**:
*   **Inheritance:** Designed a parent base class `Vehicle` which is cleanly inherited by child classes like `Car`, `Motorcycle`, and `Truck` to reuse common attributes.
*   **Polymorphism:** Implemented overridden methods like `start_engine()` or `service_cost()` that behave differently based on the vehicle type.
*   **Encapsulation:** Kept sensitive attributes (like mechanical status or registration details) secure using private and protected modifiers, exposed via getter/setter methods.
*   **Composition:** The `Garage` class uses a collection of `Vehicle` objects, showcasing how different components work together seamlessly.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd virtual-garage-vehicle-system
    ```
3.  **Run the application:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   Python 3.x installed on your machine.
