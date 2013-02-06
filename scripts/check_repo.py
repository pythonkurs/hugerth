from hugerth.Session3.py import CourseRepo, repo_dir
import os.path, sys



if __name__ == '__main__':
#Take an argument which is an absolute path
	if len(sys.argv) == 2:
		directory = sys.argv[1]
	else:
		print "Warning: awkward number of fields in the input line"
		print "Using current directory"
#Change current directory to given directory
		directory = os.getcwd()
#Take the last part of the new directory and make a CourseRepo out of it
	with repo_dir(directory):
		working_dir = os.path.basename(directory)
		repo = CourseRepo(working_dir)
#Check that this directory has the required files:
		if repo.check():
			print ("PASS (but you lost The Game)")
		else:
			print ("EPIC FAIL: you just lost The Game")
	
	




