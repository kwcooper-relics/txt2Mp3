from gtts import gTTS
import random

#TODO

#add logic for whether to convert or nah
#add logic for converting to a new folder, and doing buisness from there like...
#...support to add the text to convert directly into the function as input.

#future...
#support for multiple filetypes to save, as a choice
#an option to split the file, by a specified portion, chapter?
#a local option, so you don't need internet support
#add support to adjust read speed


#Process Text File-----------------
#> Add support for file cleanup so the text doesn't read out non letter characters

#duplicate letter support? 

def text_cleanup(file):
	print 'converting file'
	symb = "!@#$^%*"
	with open(file, 'r') as f, open('cleanedFile' + '.txt', 'w+') as cf:
		for line in f:
			l2 = line.translate(None, symb)
			cf.write(l2)
			cf.write('\n')

#Convert/save Text File-----------------

def convert_n_save(file):
	with open(file) as f:
		txt = f.read()
		tts = gTTS(text = txt, lang='en')
		rand = random.randrange(0,25,1)
		try:
			name = raw_input('filename? > ')
			print 'saving file, do not exit the program...'
			tts.save(str(name) + '.mp3')
			print 'saved as: ' + name + str(rand) + '.mp3'
		except EOFError:
			print 'EOFError, saving as default name'
			print 'saving file... '
			tts.save('audiobook' + str(rand) + '.mp3')
			print 'saved as: ' + 'audiobook' + str(rand) + '.mp3'
	


print 'Welcome to txt2mp3 2.1'
print 'Please paste the location of the txt file to convert'
loco = raw_input('> ')
text_cleanup(loco)

#print 'do you want to convert the cleaned text to an audiobook?'
print 'Please paste the location of the txt file to convert to mp3'
loco = raw_input('> ')
convert_n_save(loco)




