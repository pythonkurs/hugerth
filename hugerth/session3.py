#!/usr/bin/env python

import os.path

class CourseRepo(object):
	def __init__(self,lastname):
		self.required = [".git", "setup.py", "README.md", 
				"scripts/getting_data.py", "scripts/check_repo.py"]
		self._also_required(lastname)
		self._surname = lastname 

	@property
	def surname(self):
		return self._surname

	@surname.setter
	def surname(self, lastname):
		self._surname = lastname
		self._also_required(lastname)

	def _also_required(self, lastname):
		self.required.append("{lastname}/__init__.py".format(lastname=lastname))
		self.required.append("{lastname}/session2.py".format(lastname=lastname))
		self.required.append("{lastname}/session3.py".format(lastname=lastname))

	def check(self):
		for file in self.required:
			if not os.path.exists(file):
				print "Not found: " + file
				return False
		return True

class repo_dir(object):
	def __init__(self, target):
		self.original = os.getcwd()
		self.target = target
	def __enter__ (self):
		os.chdir(self.target)
	def __exit__ (self, type, value, tb):
		os.chdir(self.original)
