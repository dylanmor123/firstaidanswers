from VideoSearch import SearchYouTube
from ImageSearch import SearchImage
import webbrowser

VIDEO_CATEGORIES = ["What if", "Should I", "What should I do if", "How do I", "How can I tell if", "Do I", "What do I do if", "Can I give them",
"How do I treat", "When should I call 911?", "Should I try", "How long should I", "How will I know if", "What does"]

IMAGE_CATEGORIES = ["What is", "What are the signs and symptoms of"]

def Answer(question):

	while question != "OK":
		answer_found = False
		for category in IMAGE_CATEGORIES:
			if category in question:
				webbrowser.open(SearchImage(question))
				question = raw_input("What's Your Emergency: ")


		for category in VIDEO_CATEGORIES:
			if category in question:
				webbrowser.open(SearchYouTube(question))
				question = raw_input("What's Your Emergency: ")


				
		if not answer_found:
			print "Sorry, we couldn't find the answer you were looking for"
			break
				

	return


#def getStory(category, keywords):




