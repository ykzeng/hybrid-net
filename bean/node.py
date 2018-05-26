import sys, logging
from abc import ABCMeta, abstractmethod

class node_type:
	SWITCH=0
	# currently only supports VM
	DEV=1
	# xrouter implemented based on ovs switch
	ROUTER=2
	# pure router based on linux netns
	PROUTER=3


class node:
	__metaclass__ = ABCMeta
	# device id
	did=''
	# device type
	dtype=1
	# device name
	name=''

	def __init__(self, did, name, dtype):
		self.did=did
		self.dtype=dtype
		self.name=name
		pass

	@abstractmethod
	def uninstall(self):
		pass

	@abstractmethod
	def start(self, session=None):
		pass