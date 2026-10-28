# MWRCD Capstone Project

Current Zensical Version: 0.0.51

Last PIP Freeze: 7/24/2026      ([Update Zensical](#update-zensical) if changed)


## Initial Set Up

### SSH Key Setup

Before you can download the documentation site and submit changes, you'll need an SSH Key setup on your GitLab account. When copying your key, *make sure* it starts with `ssh-ed25519` and ends with your computer hostname.

Obtaining public SSH Key:

*Linux/Mac:*

```
cat ~/.ssh/id_ed25519.pub
```

*Windows:*

Open `C:\Users\<username>\.ssh\id_ed25519.pub` in Notepad

If the above shows that a file doesn't exist, then you can generate a new one using this command:

```
ssh-keygen -t ed25519 
# Leave the filename blank / default unless you know you want to generate a custom one.
# Enter a passphrase that you'll remember each time you interact with your key
```

In GitHub, go to your profile settings and find the [SSH Keys and GPG Keys](https://github.com/settings/keys) section in the left navigation bar to add your public key.

### Clone Git Repository
The documentation site is handled through git and currently hosted on GitHub.

```
git clone git@github.com:bauerta-uwec/MWRCD-Capstone-HS.git
```

### Python Set Up

[Python 3](https://www.python.org/downloads/) and pip is required on your machine before running the Zensical engine.

It's *highly* required to use a virtual environment (or conda if installed) to be consistent with other admins and the production server.

#### Virtual Environment (venv)

See [this page](https://docs.python.org/3/library/venv.html) for more details.

NOTE: venv will create the environment folder in the same directory you are in. Keep this in mind and rename used venv name as needed. It's recommended to do this inside the git `mwrcd-capstone` folder that contains all the site files.

Linux/MacOS: 
```
python -m venv venv-mwrcd-capstone
source venv-mwrcd-capstone/bin/activate 
```

If `python` isn't found, then try `python3` instead.

Windows:

```
py -m venv venv-mwrcd-capstone 
venv-mwrcd-capstone\Scripts\activate
```

#### Conda

```
conda env create -n mwrcd-capstone
conda activate mwrcd-capstone

# Make sure your environment has the pip command
conda install pip
```

### Install Zensical

To keep things consistent, make sure to run this command fairly often *in your environment*. Run this command inside your mwrcd-capstone website directory.

```
pip install -r pip-requirements.txt
```

## Editing Pages

### Download New Changes

Everytime you start working on the documentation site, it's recommended to pull the latest changes down to your computer to ensure you have the most up-to-date guides.

```
git pull
```

### Activate Python Environment

Before you can run the Zensical software, you'll need to make sure you have activated the Python environment containing all of the code.

Navigate to the parent location of where you installed the `venv-mwrcd-capstone` directory.

Linux/MacOS (venv): 
```
source venv-mwrcd-capstone/bin/activate 
```

Windows (venv):

```
venv-mwrcd-capstone\Scripts\activate
```

Conda:

```
conda activate mwrcd-capstone
```

### Update Zensical

It's also recommended to occasionally run the following command to update Zensical, especially if the date below is newer than when you last ran the command.

```
pip install -r pip-requirements.txt
```

### Start Local Server

Depending on your OS and terminal set up, there are a few different commands available to build and spin up a local server for running your own Zensical instance.

```
zensical serve
    OR
python -m zensical serve
    OR
python3 -m zensical serve
```

This should start up a local website hosting your documents accessible by going to [`http://127.0.0.1:8000`](http://127.0.0.1:8000) in your web browser.

### Make Your Changes

Everything in Zensical is written using a mix of Markdown and HTML. For the most part try to stick with Markdown for consistency, but use HTML for anything more complex.


### Submit Your Changes

Once you are done working on the pages, then commit and push the code back up to the remote / gitlab server for other admins to access.

```
git add -p <files-to-add>
git commit -m "What You Did"
git push
```

## Guidelines

- Passwords, access tokens, and any other private info should *not* be included in these docs.

## References
* [Git Repo](https://github.com/bauerta-uwec/MWRCD-Capstone-HS)
* [Git Tutorial](https://git-scm.com/docs/gittutorial)
* [Zensical User Guide](https://zensical.org/docs/get-started/)
* [Markdown Guide](https://www.markdownguide.org/)