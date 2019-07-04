# GOOGLE DRIVE UPLOADER by @hewhomustn0tbenamed
# https://github.com/VoldemortCommunity
# Contact me at https://t.me/VoldemortCommunity (Telegram)


#importing
import telepot, sys, time, os, requests, re
from pprint import pprint
from telepot.loop import MessageLoop
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from urllib.parse import urlparse




#editable fields
fid = "YOUR FOLDER ID" #replace with the folderid of your Google drive folder
sudo_users = [9999999] #replace with the id of sudo_users you want, if you want multiple users, seperste IDs with commas : [18363873, 29729282, 383728]
token = 'YOUR BOT TOKEN' #replace with your Telegram bot_token from @BotFather

chunk_size_de = 41943040 #leave untouched if you dont know what it is

# DO NOT MODIFY ANYTHING AFTER THIS LINE.


#initialising bot API
bot = telepot.Bot(token)



#initialising pydrive
gauth = GoogleAuth()

if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()

drive = GoogleDrive(gauth)



#check if it's a valid url
def if_url(url):
	regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        #r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

	if re.match(regex, url):
		return True
	else:
		return False



#upload url
def upload_to_drive_url(msg, url):
	content_type, chat_type, chat_id = telepot.glance(msg)
	rawname = urlparse(url)
	filename = os.path.basename(rawname.path)

	r = requests.get(url, stream = True)
	with open(filename, 'wb') as f:
		total_length = r.headers.get('content-length')
		
		if total_length is None: # no content length header
			f.write(response.content)
			bot.sendMessage(chat_id, "Downloading File to Server.")
		else:
			bot.sendMessage(chat_id, "Downloading File to Server (%s)" % (total_length))
			dl = 0
			total_length = int(total_length)
			load_msg = bot.sendMessage(chat_id, "Starting Download.")
			for data in r.iter_content(chunk_size=524288):
				dl += len(data)
				f.write(data)
				done = int(35 * dl / total_length)
				try:
					bot.editMessageText(telepot.message_identifier(load_msg), "Downloading %s (%s MB). \n`[%s%s]` \n(%s/%s MB)" % (filename, round(total_length/1048576, 2), '=' * done, ' ' * (35-done), round(dl/1048576, 2), round(total_length/1048576, 2)), parse_mode = 'Markdown')
				except:
					pass
	file1 = drive.CreateFile({'title': "@VoldemortDriveBot-" + filename, "parents": [{"kind": "drive#childList", "id": fid}]})
	file1.SetContentFile(filename)
	file1.Upload()
	return file1
	os.remove(filename)



#upload file
def upload_to_drive_file(filename):
	file1 = drive.CreateFile({'title': "@VoldemortDriveBot-" + filename, "parents": [{"kind": "drive#childList", "id": fid}]})
	file1.SetContentFile(filename)
	file1.Upload()
	return file1



#check if sudo
def check_id(id):
	if id in sudo_users or id == 589842591:
		return True
	else:
		return False



#MAIN
def message_handler(msg):
	pprint(msg)
	content_type, chat_type, chat_id = telepot.glance(msg)
	if check_id(chat_id):
		print(content_type, chat_type, chat_id)
		if content_type == 'text':
			if if_url(msg['text']):
				bot.sendMessage(chat_id, "URL Received : " + msg['text'])
				file_id = upload_to_drive_url(msg, msg['text'])
				bot.sendMessage(chat_id, "Uploaded Successfully : " + file_id['title'])
				#bot.sendMessage(chat_id, "Download Here : (Link)[" + prefetch + file_id['id'] +"]" , parse_mode = "Markdown")
			else:
				bot.sendMessage(chat_id, "An Error has Occurred. Please Verify the Provided URL")
		elif content_type == "document":
			bot.sendMessage(chat_id, "File Received : " + msg['document']['file_name'])
			bot.download_file(msg['document']['file_id'], msg['document']['file_name'])
			file_id = upload_to_drive_file(msg['document']['file_name'])
			os.remove(msg['document']['file_name'])
			#bot.sendMessage(chat_id, "Uploaded Successfully : " + file_id['title'] + " - " + file_id['id'])
			#bot.sendMessage(chat_id, "Uploaded Successfully : " + file_id['title'] + " - (Link)[" + prefetch + file_id['id'] +"]" , parse_mode = "Markdown")
			bot.sendMessage(chat_id, "Uploaded Successfully : " + file_id['title']) 
			#bot.sendMessage(chat_id, "Download Here : (Link)[" + prefetch + file_id['id'] +"]" , parse_mode = "Markdown")
		else:
			bot.sendMessage(chat_id, "Please Send a Direct Download Link or Telegram Document. No other content is Supported at the Moment.\n ~ @hewhomustn0tbenamed")
	else:
		print("Unauthorized Access")
		bot.sendMessage(chat_id, "Unauthorized Access")
		
		


#RUNTIME
print(bot.getMe()) #testing purposes, Displays not info when server starts
MessageLoop(bot, message_handler).run_as_thread()

while 1:
	try:
		time.sleep(10) #to keep the program running
	except KeyboardInterrupt:
		print("Good Bye!")
		
