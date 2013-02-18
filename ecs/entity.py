"""

Contains definitions for the basic Entity and EntityManager types.

"""

import component

class Entity(object):
	"""
	Encapsulates a guid to use in the entity database.
	"""
	def __init__(self, guid):
		self.__guid_ = guid
		
	def __str__(self):
		return str(self.__guid_)
	
	def __hash__(self):
		return self.__guid_
	
	def __eq__(self, other):
		return self.__guid_ == other.__guid_
	
	
	
class EntityManager(object):
	"""
	Provides database-like access to components based on an entity_id key.
	"""
	def __init__(self):
		self.database = {}
		self.lowest_guid = 0
		
	def newEntity(self):
		"""
		Returns a new entity instance with the current lowest guid value.
		
		Does not store a reference to it, and does not make any entries in the database
		referencing it.
		"""
		
		new_e = Entity(self.lowest_guid)
		self.lowest_guid += 1
		return new_e
		
	def addComponent(self, entity_id, component_instance):
		"""
		Adds a component to the database and associates it with the given entity_id.
		
		entity_id can be an Entity object or a plain integer.
		"""
		main_key = type(component_instance)
		if main_key not in self.database:
			self.database[main_key] = {}
			
		self.database[main_key][entity_id] = component_instance
		
	def removeComponent(self, entity_id, component_type):
		"""
		Removes the component of component_type associated with entity_id from the database.
		
		Doesn't do any kind of data-teardown.  It is up to the system calling this code to do that.
		
		In the future a callback system may be used to implement type-specific destructors.
		"""
		try:
			del self.database[component_type][entity_id]
		except KeyError:
			pass
		
		if self.database[component_type] == {}:
			del self.database[component_type]
		
	def getPairsForType(self, component_type):
		"""
		Returns a list of (entity_id, component_instance) tuples for all entities in the database
		possessing a component of component_type.
		
		Returns None if there are no components of this type in the database.
		"""
		try:
			return self.database[component_type].items()
		except KeyError:
			return None
		
	def getComponentForEntity(self, entity_id, component_type):
		"""
		Returns the instance of component_type for the entity_id from the database.
		
		Returns None if the entity does not have that component.
		"""
		try:
			return self.database[component_type][entity_id]
		except KeyError:
			return None
	
	def deleteEntity(self, entity_id):
		"""
		Removes all components from the database that are associated with entity_id,
		with the side-effect that the entity is also no longer in the database.
		"""
		for comp_type in self.database.iterkeys():
			try:
				del self.database[comp_type][entity_id]
				if self.database[comp_type] == {}:
					del self.database[comp_type]
			except:
				pass
		