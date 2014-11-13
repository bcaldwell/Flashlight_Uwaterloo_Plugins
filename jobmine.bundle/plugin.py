
def results(parsed, original_query):
	return {
		"title": "Open Jobmine",
		"run_args": ['']
	}


def run(message):
  import webbrowser
  url = "https://jobmine.ccol.uwaterloo.ca/psp/SS/EMPLOYEE/WORK/h/?tab=DEFAULT&cmd=login&errorCode=106&languageCd=ENG#__Jobmine_Plus_has_taken_over_Jobmine"
  webbrowser.open (url, new=2)

