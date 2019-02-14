### imgurpoi

Simple python imgur uploader with API and CLI.  
Based on Imgur API v3.

## Requirements
- click - For CLI 
- requests - For functioning
- pyperclip - For copy to clipboard support


## Quickstart
Getting Imgur API credentials
Go to https://api.imgur.com/oauth2/addclient and register a new Imgur API client.    
You will need an Imgur account to do this.   

You can put it any valid URL for the callback URL - we won’t be using it.

First, create a file called ~/.config/imgur_uploader.cfg, with the following contents (substitute your credentials):
```
[imgur]
id = 9354da9ecdcfae3
secret = 8387eca75687ecad9876ead47786edac0875dc0d
```

    $ pip install imgurpoi

### License
-------

imgurpoi is distributed under the terms of both

- `MIT License <https://choosealicense.com/licenses/mit>`_