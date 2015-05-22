import os

def main():
	proj_name = os.path.abspath('.').split('/')[-1]
	print "started create project '%s'" % proj_name
	create_files(proj_name)
	map(os.mkdir, ["templates", "static"])
	print "project '%s' created" % proj_name

def create_files(proj_name):
	for f in (proj_name, "runserver", "config", "controllers", "tests", "views", "forms"):
		py_fname = get_py_file_name(f)
		open(py_fname, "w").close()

def get_py_file_name(fname):
	return "{0}.py".format(fname)

def create_dirs():
	pass

if __name__ == '__main__':
	main()