Flail - The Ball and Chain Decorator
====================================

Flail allows any decorator to be transformed into something that looks
a little bit like a ball-and-chain attached to the thing that's being
decorated.  For example::

    from flail import _
    from dataclasses import dataclass
    from abc import abstractmethod, ABC
    import attr

    # Add different chain fixtures
    _.d = dataclass
    _.a = abstractmethod
    _.s = attr.s

    # Examples
    @_._._._._.d
    class Coordinates:
        x : float
        y : float

    @_._._._.s
    class Vector:
        x = attr.ib()
        y = attr.ib()
        z = attr.ib()

    class Connection(ABC):
        @_._.a
        def open(self):
            ...
        @_.__.a
        def close(self):
            ...
        @_._.a
        def read(self, maxbytes):
            ...
        @_.__.a
        def write(self, data):
            ...

Note: The use of ``...`` in the above ``Connection`` class is not really
neccessary, but makes it look a bit more bad-ass (use ``pass`` if this
bothers you).

As shown, you can attach different decorators to the chain as what
flail refers to as "fixtures."  The recommended style of flail is to
extend the chain so that the fixture appears to be attached to the
center of the class/function name that follows.  For example::

    # YES!
    @_._._._._.d
    class Coordinates:
        x : float
        y : float

    # NO!
    @_.d
    class Coordinates:
        x : float
        y : float

If you're having trouble centering it, you can use more than one
underscore.  For example::

    @_._.__.d
    class Vect3:
        x : float
        y : float
        z : float

FAQ
---

*Why?*

Does this really need to be constantly explained?

*What's with the name?*

The name refers to the medieval weapon consisting of a ball and chain.
See `https://en.wikipedia.org/wiki/Flail_(weapon) <https://en.wikipedia.org/wiki/Flail_(weapon)>`_.

*Who?*

Flail is the brainchild of David Beazley (@dabeaz) who disavows all
knowledge of it and who should probably be working on his book
instead.  

