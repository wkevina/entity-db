entity-db
=========

A python entity-system-component library for games.

There are many articles on the internet advocating a switch to entity-based systems for game logic.  However, most authors seem to burn themselves out telling why the old inheritance-based approach is problematic, and how an entity system will solve your problems, without ever really explaining what it is or how to do it.

This project attempts to provide an actual implementation for use in your and my game projects.

I call the library an "entity-system-component" library, rather than an entity system, as the entity portion is just one building block concept.

The module is called `ecs`.  `ces` is too close to something else, and while there is another library called `ecs`, it's for an E-Commerce service from Amazon and is unlikely to name-clash in your projects.

As this module is in somewhat rarefied air, with not a lot of company, the concepts and API will change often during development.  Inspiration is taken from the Ash entity framework for AS3.

### Concepts

`ecs` stands for entity, component, AND system.  The system part is just as important as the component and entity part.  So what are these?

`entity`: Simply a unique identifier, used to label components as belonging to a logical grouping.

`component`: A collection of data.  Has no behavior associated with it.

`system`: In this case, a system operates on the data in components.

### Details


Right now, `ecs` defines a few core core classes:

```
Entity
EntityManager
Component
System
SystemManager
```

The EntityManager is a database that stores Components, referenced by their type and entity id.

SystemManager maintains a set of System instances and allows them to perform their operations.

The System is where the action really happens.  A System instance queries the EntityManager database for a set of Components and operates on the data contained in them.
