# Object Oriented Programming Design Patterns

- Design patterns are categorized as creational, structural, or behavioral
Reference/credit: https://refactoring.guru/
## Creational Patterns
> Object creation mechanisms

### Singleton
> A class that has only a single instance while providing a global access point to this instance
- Used to control access to some shared resource (database/file)
#### Implementation
- Make default constructor private (prevent use of `new` operator with singleton class)
- Requires locks in multithreaded environment
- 

### Factory Method
### Abstract Factory

### Prototype

### Builder


## Structural Patterns
> Blueprint for combining objects and classes into larger structures

### Adapter

### Bridge

### Composite

### Decorator

### Facade

### Flyweight

### Proxy

## Behavioural Patterns
> Communication/state management methods between objects


### Chain of Responsibility

### Command

### Iterator

### Mediator

### Memento

### Observer

### State

### Strategy

### Template Method

### Visitor