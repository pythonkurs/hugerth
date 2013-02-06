import os.path

class CourseRepo(object):
	def __init__(self,lastname):
		self.lastname = lastname
		self.required=[".git", "setup.py", "README.md", "scripts/getting_data.py", "scripts/check_repo.py", "{lastname}/__init__.py".format(lastname=self.lastname), "{lastname}/session3.py".format(lastname=self.lastname)]
	def check(self):
		for file in self.required:
			if not os.path.exists(file):
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
