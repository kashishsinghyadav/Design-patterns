# Practice Problems for Creational Design Patterns

## Singleton Pattern

### Problem:
Implement a configuration manager for a game application using the Singleton pattern. The configuration manager should load game settings from a file and provide a global point of access to these settings throughout the application.

### Constraints:
- The configuration manager should have methods to load settings from a file and retrieve settings by key.
- Ensure that only one instance of the configuration manager exists throughout the application.

## Factory Method Pattern

### Problem:
Create a simple pizza ordering system using the Factory Method pattern. The system should allow customers to order different types of pizzas (e.g., Margherita, Pepperoni, Veggie) through a factory method.

### Constraints:
- Define an abstract class `Pizza` with subclasses for each type of pizza.
- Implement a `PizzaFactory` class with a method to create pizzas based on customer orders.

## Abstract Factory Pattern

### Problem:
Develop a GUI library using the Abstract Factory pattern to support multiple platforms (e.g., Windows, macOS). The library should provide factory classes for creating buttons and text boxes specific to each platform.

### Constraints:
- Define an abstract class `GUIFactory` with methods to create buttons and text boxes.
- Implement concrete factory classes (`WindowsGUIFactory`, `MacGUIFactory`) for each platform.

## Builder Pattern

### Problem:
Build a simple house construction system using the Builder pattern. The system should allow users to construct different types of houses (e.g., standard house, villa) by specifying the number of rooms, bathrooms, and other features.

### Constraints:
- Define a builder interface with methods for constructing different parts of the house.
- Implement concrete builder classes for each type of house, such as `StandardHouseBuilder` and `VillaBuilder`.

## Prototype Pattern

### Problem:
Create a prototype-based user profile system for a social media application using the Prototype pattern. The system should allow users to create new profiles by cloning an existing profile template.

### Constraints:
- Define a prototype interface with a method to clone user profiles.
- Implement concrete prototype classes for different types of user profiles, such as `BasicUserProfile` and `PremiumUserProfile`.
