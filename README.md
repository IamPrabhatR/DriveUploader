# Drive Uploader
- Telegram to Google Drive Uploader BETA by @Voldemort1912 (Uploaded on 04/07/2019)

## For Educational Purposes Only!!
#### I Will Not be Responsible for Any Kind of Problems That Arise due to Unfair Usage!!
###### P.S. You Know What I Mean! xD

### IMPORTANT
* THIS IS A BETA VERSION.
* PLEASE REPORT ANY BUGS OR SUGGESTIONS ON TELEGRAM OR GITHUB.
* Report any Bugs at [@VoldemortCommunity](https://t.me/VoldemortCommunity) (Telegram)


## Setting Up. ( Heroku )
* Open a Terminal & Run `pkg update && pkg upgrade && pkg install git python nano nodejs && npm install -g heroku`
* Next, Run `git clone https://github.com/VoldemortCommunity/DriveUploader && cd DriveUploader`
* Install Requirements using `pip install -r requirements.txt`
* Go to [@BotFather](https://t.me/BotFather) & Create a New Bot. Copy the Bot Token.
* Get Drive folder ID:
	- Visit [Google Drive](https://drive.google.com).
	- Create a new folder. The bot will upload files inside this folder.
	- Open the folder.
	- The URL will be something like `https://drive.google.com/drive/u/0/folders/012a_345bcdefghijk`. Copy the part after folders/ (012a_345bcdefghijk). This is the folder ID that you'll need.
* Go to [@MissRose_bot](https://t.me/MissRose_bot) and Type `/info`, Copy your ID that shows up.
* Configure the Required Information using any Text Editor, the Simplest is nano
	- Type `nano bot.py` & paste the Required Information in the `#editable fields` Section
* Next, Setup Google Drive API (Doing this in Desktop View is Highly Recommended):
	- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
	- Log-in and Create a Project if Asked to do so
	- Go To the [Google API Library](https://console.developers.google.com/apis/library), Search for Drive and Enable it.
	- Wait for a 10 Minutes as it Takes Time for the API to be Enabled.
	- Tap on `Create Credentials` & Select `OAuth Client ID`
	- You Will be Asked to setup the OAuth Consent Screen, Type in the Application Name, and Enter `https://localhost:8080` in All Link Fields Except Terms of Service. Save this and Head Back to Creating Credentials.
	- Select `Other` as the Application Type and Use any Name you Like.
	- Once the Credentials are Created, Close the Pop-up and Find your Credentials in the List of OAuth 2.0 Client IDs
	- Press the Download Button on the Far Right of the Screen
	- a File Named `client_secret_SOME_LONG_STRING.apps.googleusercontent.com.json` will be Downloaded.
	- Rename this to `client_secrets.json` and Copy/Move it to the Root Directory of the Bot. Termux Users can Execute : `termux-setup-storage && cp ~/storage/downloads/client_secrets.json ~/DriveUploader`
* Before Pushing to Heroku, run the App on your own Device to Generate Credentials. Type `python bot.py` and Send a file to the Telegram Bot, Come Back to the Terminal and you'll see a Sign-In Link, Copy Paste the Link in a Browser and Allow Permissions To Access Drive.
* After Doing this, [Create an Account on Heroku](https://signup.heroku.com/)
* Type `heroku login` in your Terminal and Enter the Details.
* Type `heroku create` to Create a New App
* Run `git add -A && git commit -m "Uploaded Files" && git push --set-upstream heroku master` to Automatically Push and Compile the App on Heroku.
* Go to Your [Heroku Dashboard](https://dashboard.heroku.com) and Find the App, Tap on `Configure Dynos` and Turn on the Switch by Editing It
* THAT'S IT. YOU CAN NOW SEND ANY FILE OR DIRECT DOWNLOAD LINK TO THE TELEGRAM BOT TO UPLOAD IT TO YOUR GOOGLE DRIVE.


## To-Do

* You Tell Me. Suggestions → [@VoldemortCommunity](https://t.me/VoldemortCommunity) (Telegram)

### Issues?

* Report Them on GitHub!!
* Contact Support : [@VoldemortCommunity](https://t.me/VoldemortCommunity) (Telegram)

### Feature Requests & Feedback

* Contact Me : [@hewhomustn0tbenamed](https://t.me/VoldemortCommunity) (Telegram)
* Mail Me : [Voldemort1912@hackermail.com](mailto:voldemort1912@hackermail.com)

#### Have Questions?
* Join the Conversation at [@VoldemortCommunity](https://t.me/VoldemortCommunity) !!
* DM me [@Voldemort1912](https://github.com/Voldemort1912) !!
* DM me on Telegram [@hewhomustn0tbenamed](https://t.me/hewhomustn0tbenamed) !!
