import git;
import sys;

def getLogs(repo):
	""" Get the logs (seperated into 4-item chunks, and without useless stuff.) """
	if isinstance(repo, basestring):
		repo = git.Repo(repo)
	list_log = repo.git.log().split("\n")
	while u'' in list_log:
		list_log.remove(u'')
	temp = list(chunks(list_log,4))
	return temp

def generateHTML(path):
	repo = git.Repo(path);
	log = getLogs(repo)
	page = "";
	for i in reversed(log):
		page += i[0]+"<br>"
		page += i[1]+"<br>"
		page += i[2]+"<br>"
		page += i[3]+"<br>"
		page += "<br>"
	return page

def generateMarkdown(path):
	repo = git.Repo(path);
	log = getLogs(repo)
	page = "# Commits for "+path+"\n";
	for i in reversed(log):
		page += i[0]+"  \n"
		page += i[1]+"  \n"
		page += i[2]+"  \n"
		page += i[3]+"  \n"
		page += "\n"
	return page
