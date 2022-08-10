# django-portal-template

This open-source repository is to get started quickly with a portal-type application. 

Courtesy of www.buzzerboy.com

# Requirements

The following tools must be installed on your Windows machine:
1. Vagrant (vagrantup.com) - We use this as a virtualization tool to run linux as a development server
2. VisualStudio Code (https://code.visualstudio.com/) - We use this as an IDE
3. Docker (https://www.docker.com/) - We use this as a virtualization tool for deploying the QA and Production environments

# Special Acknowledgements

In development of this portal template, I leveraged MIT Licensed AppSeed.us UI Aargon Dashboard Freeware.

# Directory Structure


```bash
$ /root/
```
> This is the root directory where you cloned the repository. You can name is what ever you like.

```bash
$ /root/environments
```
> This is the directory where the Vagrantfile and Vagrant setup is located. Vagrant is specifically helpful in setting up a linux based virtual environment. But,
> if you're using python on your Windows or Mac, then you can ignore this directory.

```bash
$ /root/Graphics
```
> This is the directory where the saw images are located for use within the portal. You can use it to store your raw images as well. Exported PNG or SVG files are located inside the static directory as described later on.



