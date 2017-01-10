# xxsmap
This is a tool for finding xxs vulnerability's in websites.

                   
                                                    ___
                                                   __H__
                                    __  ____  _____ [(] _ __ ___   __ _ _ __
                                    \ \/ /\ \/ / __|[)]| '_ ` _ \ / _` | '_ \
                                     >  <  >  <\__ \[(]| | | | | (_| | | |_) |
                                    /_/\_\/_/\_\___/[)]|_| |_| |_|\__,_| .__/
                                                     V               |_|_|




All it has are few important neededs:

- Cookies must be separated with a single space
- All site names must end with a '/'

It only currently works on .php sites but that will change in the future to .aspx etc.
Currently it will only crawl the main page for urls but eventualy it will do the whole site.
To run it all you have to do is:
 
    python3 xxsmap.py --site [http://example.com/]
And that will do a basic scan of that site.
You can target spesific addresses aswell with:

    python3 xxsmap.py --address [https://example.com/site/shop/login.php?name=Dylan]
And xxsmap will pick out the spesific parameter and attack it.
If you where going to attack the Damn Vulnerably Web App for example you could use:

    python3 xxsmap.py --address [http://192.168.1.164/dvwa/vulnerabilities/xss_r/?name=#] --cookie [security=medium PHPSESSID=6b2519e1646eb27e23bf1462c5dda253] --threads 10
This will give you the ability to login to websites and exploit the otherwise hidden features and parameters.

It can find and get round most forms of common xxs security filters but it can't seem to get past htmlspecialchars,
the annoying thing about this is that if a xxs payload is sanitised by that filter it still shows up like it go through
this means that when you get the succsess sign there is only about a 90% chance of it actually being vulnerable.
