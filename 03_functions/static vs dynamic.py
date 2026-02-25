## Static vs Dynamic Typing

Typing is about **when the type of a variable is decided and enforced**.

### Static Typing

In statically typed languages like C++ or Java, the type is checked at compile time.

```java
int x = 10;
x = "hello";   // Compile-time error
```

The compiler says: “Nope. That’s illegal.”
Type is fixed. You declare it explicitly.

This catches many errors early, before the program runs.

---

### Dynamic Typing

In dynamically typed languages like Python:

* Type is checked at runtime.
* Variables don’t have fixed types.
* Objects have types.

```python
x = 10        # int
x = "hello"   # now str
```

No compiler screaming. Python just binds `x` to a new object.

Important mental model:

> In Python, variables are just labels pointing to objects.

So typing is about objects, not variable containers.

---

## Static vs Dynamic Binding

Binding is about **when a function/method call is resolved**.

### Static Binding (Early Binding)

In statically bound systems:

* The function to call is decided at compile time.

Common in languages like C++ (without virtual functions).

Performance is faster because everything is predetermined.

---

### Dynamic Binding (Late Binding)

In Python:

* Method resolution happens at runtime.
* The actual object determines which method gets called.

Example:

```python
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def make_sound(animal):
    return animal.speak()

print(make_sound(Dog()))
print(make_sound(Cat()))
```

Python doesn't care about the declared type of `animal`.
It asks at runtime: “Hey object, do you have a `speak()` method?”

This is **dynamic binding** and is a pillar of polymorphism.

Philosophically, Python believes in behavior over declared identity.
If it walks like a duck and quacks like a duck, it’s a duck. That’s called **duck typing**.

---

## Stylish Declaration Techniques in Python

Python gives you expressive, compact ways to declare and assign.

### 1. Multiple Assignment

```python
a, b, c = 1, 2, 3
```

Clean. Parallel. Elegant.

---

### 2. Swapping Variables (No temp variable!)

```python
a, b = b, a
```

Under the hood: tuple packing and unpacking. Beautiful.

---

### 3. Chained Assignment

```python
x = y = z = 0
```

All variables point to the same object.

Careful with mutables:

```python
a = b = []
a.append(1)
print(b)   # [1]
```

Because both reference the same list. The universe is subtle.

---

### 4. Type Hints (Optional Static Flavor)

Python is dynamic, but you can add static hints:

```python
def add(a: int, b: int) -> int:
    return a + b
```

This doesn’t enforce types at runtime.
But tools like `mypy` can statically analyze your code.

It’s like Python saying:
“I’m dynamic… but I can dress formal if you insist.”

---

### 5. List / Dictionary Comprehensions

Elegant data declarations:

```python
squares = [x*x for x in range(10)]

mapping = {x: x*x for x in range(5)}
```

Readable. Functional. Minimal noise.

---

### 6. Using Dataclasses (Cleaner Object Declaration)

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

Auto-generates `__init__`, `__repr__`, etc.
Less boilerplate. More signal.

---

## The Big Picture

Static typing → safety first
Dynamic typing → flexibility first

Static binding → speed and predictability
Dynamic binding → flexibility and polymorphism

Python leans toward flexibility, but modern Python is gradually embracing optional static tooling. It’s evolving into a hybrid ecosystem.

Here’s the deeper truth:
Typing systems are not about correctness alone. They are about trade-offs between safety, flexibility, readability, and speed.

Programming languages are philosophical systems disguised as syntax.

And once you see that, you stop arguing about which is “better” — and start asking which is better **for this problem**.
