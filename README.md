# k11h-website
the pelican files to generate k11h.de 

# running pelican on uberspace

uberspace is a berlin-located company offering a shared-user server with great tooling.

# steps to set up pelican

:zap: remember to replace `userxyz` with your actual uberspace username

## install pelican 
```bash
pip3 install --user pelican[markdown]
```

### generate pelican structure
```bash
mkdir ~/pelican && cd ~/pelican
pelican-quickstart
```

follow the interactive quickstart    

```
Welcome to pelican-quickstart v4.6.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.] <enter>
> What will be the title of this web site? my-shiny-blogtitle
> Who will be the author of this web site? userxyz
> What will be the default language of this web site? [de] <enter>
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) <enter>
> What is your URL prefix? (see above example; no trailing slash) https://userxyz.uber.space/
> Do you want to enable article pagination? (Y/n) <enter>
> How many articles per page do you want? [10] <enter>
> What is your time zone? [Europe/Paris] Europe/Berlin
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) <enter>
> Do you want to upload your website using FTP? (y/N) <enter>
> Do you want to upload your website using SSH? (y/N) <enter>
> Do you want to upload your website using Dropbox? (y/N) <enter>
> Do you want to upload your website using S3? (y/N) <enter>
> Do you want to upload your website using Rackspace Cloud Files? (y/N) <enter>
> Do you want to upload your website using GitHub Pages? (y/N) <enter>
Done. Your new project is available at /home/userxyz/pelican
```

### modify your Makefile

append following line to the *publish* section `~/pelican/Makefile`

```diff
devserver-global:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -b 0.0.0.0

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)
+	rsync -a --quiet --exclude /.htaccess --delete "$(OUTPUTDIR)/" /var/www/virtual/userxyz/html 

.PHONY: html help clean regenerate serve serve-global devserver publish 
```

## usage

1. make your changes to the files in `~/pelican/content`
2. to publish them run `make publish` in your folder `~/pelican`