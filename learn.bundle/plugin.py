
def results(parsed, original_query):
	return {
		"title": "Open Uwaterloo Learn",
		"run_args": ['']
	}


def run(message):
  import webbrowser
  url = "https://learn.uwaterloo.ca/"
  webbrowser.open (url, new=2)

