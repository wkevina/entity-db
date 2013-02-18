class DuplicateSystemTypeException(Exception):
	pass

class System(object):
	"""
	An object that represents an operation on a set of objects from the game database.
	"""
	def __init__(self):
		self.sys_man = None
		self.priority = 0 # just a placeholder for the system-manager to do what it will
		
	def update(dt, entity_manager):
		"""
		Called by the system manager.  Here is where the functionality of the system is
		implemented.
		"""
		print 'System.update called. dt={}, entity_manager={}'.format(dt, entity_manager)
	
	
class SystemManager(object):
	"""
	A container and manager for System objects.  Maintains a list of System objects.
	
	Has a facility for updating those System objects, in the order of priority.
	"""
	def __init__(self, entity_manager):
		self.entity_manager = entity_manager
		self._systems = []
		
	def add_system(self, system_instance, priority=0):
		"""
		Adds a System instance to the manager.  It will be updated according to 
		the priority given, lower numbers first.
		"""
		if [True for s in self._systems if type(s) is type(system_instance)]:
			raise DuplicateSystemTypeException()
		
		system_instance.priority = priority
		system_instance.sys_man = self
		
		self._systems.append(system_instance)
		self._systems.sort(key=lambda s: s.priority)
		
	def remove_system(self, system_type):
		"""
		Removes a System instance of type system_type from the manager.
		"""
		for s in self._systems:
			if type(s) is system_type:
				self._systems.remove(s)
				return
		
	def update_systems(self, dt):
		"""
		Updates each system, in the order of their priority.
		"""
		for system in self._systems:
			system.update(dt, self.entity_manager)