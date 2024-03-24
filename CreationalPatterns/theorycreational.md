
# Creational Design Patterns 
This repository contains an overview of the creational design patterns along with important points to remember, particularly for fresher interviews.

## Singleton Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. It is commonly used in scenarios like database connections, logging, configuration management, etc.

### Important Points:

- Use cases include managing global resources, ensuring single configuration settings, and more.
- Be cautious with multithreading; ensure thread safety if the application is multithreaded.
- Consider alternatives like dependency injection if the Singleton introduces tight coupling.

## Factory Method Pattern

The Factory Method pattern defines an interface for creating an object but allows subclasses to alter the type of objects that will be created. It is commonly used in frameworks where classes cannot anticipate the type of objects they must create.

### Important Points:

- Decouples the client code from the object creation logic.
- Provides flexibility to subclasses to create specific implementations of objects.

## Abstract Factory Pattern

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. It allows a client to use an abstract factory to create a family of related products without knowing about the concrete implementations.

### Important Points:

- Promotes loose coupling between client code and concrete implementations.
- Encourages the use of composition over inheritance, as it deals with object composition.

## Builder Pattern

The Builder pattern separates the construction of a complex object from its representation so that the same construction process can create different representations. It is useful when the construction process must allow for different representations of the constructed object.

### Important Points:

- Simplifies the creation of complex objects by providing a step-by-step approach.
- Promotes the immutability of objects, as builders typically produce immutable objects.

## Prototype Pattern

The Prototype pattern creates new objects by cloning an existing object, known as the prototype, instead of creating new instances using a constructor. It is useful when the construction of a new object is more efficient by copying an existing object.

### Important Points:

- Improves performance by avoiding costly object creation operations.
- Ensure that the cloning process produces deep copies if the object contains nested structures.
