---
title: English quantifiers -- Bus example
...

What does the statement "everyone can fit on a bus" mean?

# Partition

Everyone can fit on a bus by dividing people between buses

![Everyone can fit on a bus by dividing people between buses](files/bus-1.svg)

This is formalized in mathematics as a partition problem:
given a set of buses and a set of people,
find a mapping between people and buses that satisfied capacity constraints.

# As a set, universal

Everyone can fit on a bus, so we only need one bus.

![Everyone can fit on a bus so we only need one bus](files/bus-2.svg)

This is formalized in mathematics by saying the "fit on a bus" predicate applies to an entire set of people rather than to individual people.

# One at a time, universal

Everyone can fit on a bus, even the largest person in the world.

![Everyone can fit on a bus, even the largest person in the world](files/bus-3.svg)

This is formalized in mathematics by saying the "fit on a bus" predicate applies to any person we happen to pick, but individually instead of as a group.

# As a set, existential

Everyone can fit on a bus, so we only need one bus if we get the biggest bus.

![Everyone can fit on a bus if we get the biggest bus](files/bus-4.svg)

This is the same as the item before (a property of an entire set of people) but is differently quantified: where the previous item implied the fitting was independent of the bus selected, this one implies that only some of the buses need ot be big enough.

# One at a time, existential

Everyone can fit on a bus, even the largest person in the world can fit on at least one of our buses

![Everyone can fit on a bus, even the largest person in the world can fit on at least one of our buses](files/bus-5.svg)

