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

```bash
$ /root/portalapp
```
> This is the directory where the django project is located for the portal itself. 

```bash
$ /root/portalapp/apps
```
> This is the directory contains all the apps that are part of the project. If you add additional apps to your project, use django-admin here to add additional apps. 

```bash
$ /root/portalapp/core
```
> This is the directory contains all core functionality of the portal. It is not recommended to update code in here. This is beacuse you can update the core as new version come to augment functionality for your portal.


```bash
$ /root/portalapp/html5_ui
```
> This is the directory contains the HTML5-based theme, and user-interfaces for the app. To create code-specialization segregation, this is where the front-end engineers can focus.

```bash
$ /root/portalapp/nginx
$ /root/portalapp/staticfiles
```
> These are system directories. If your hosting environment requires nginx, you can augment your context specific configuration in here.
> The staticfiles folder holds all the static files here if they are hosted on the app server.
