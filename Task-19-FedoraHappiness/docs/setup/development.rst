#######################################
How to set up a development environment
#######################################

This guide includes instructions for Linux / macOS and Windows.


**************
Pre-requisites
**************

You need the following programs installed before proceeding (on all operating systems).

- `Git <https://git-scm.com/>`__
- `Python 3.6.x <https://www.python.org/downloads/>`__


*****************
How to use Docker
*****************

No matter what operating system you use, you need Docker.
Docker is a tool to run applications inside what are known as "containers".
Containers are similar to lightweight virtual machines (VMs).
They make it easier to develop, test, and deploy a web application.
Fedora Happiness Packets uses Docker for local development and to deploy to the production website.

The project comes with a **Dockerfile**.
A Dockerfile is the instructions for a container build tool (like Docker) to build a container.
Look at the `Fedora Happiness Packets Dockerfile <https://pagure.io/fedora-commops/fedora-happiness-packets/blob/master/f/Dockerfile>`__ for an example.

How to install Docker
=====================

Install Docker as described in the `installation docs <https://docs.docker.com/install/>`__.
You also need to install `Docker Compose <https://docs.docker.com/compose/install/>`__.
Docker Compose is used to run multiple containers side-by-side.
While developing Fedora Happiness Packets, there are a few different services that run in multiple containers, like the Django web app, the Postgres database, and more.

See below for platform specific installation guidelines:

- `Docker Desktop for Mac <https://docs.docker.com/docker-for-mac/install/>`__ (Docker Compose included)
- `Docker Desktop for Windows <https://docs.docker.com/docker-for-windows/install/>`__ (Docker Compose included)
- `CentOS <https://docs.docker.com/install/linux/docker-ce/centos/>`__
- `Debian <https://docs.docker.com/install/linux/docker-ce/debian/>`__
- `Fedora <https://developer.fedoraproject.org/tools/docker/docker-installation.html>`__
- `Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`__


******************
Run initial set-up
******************

This section explains how to get started developing for the first time.

Fork and clone
==============

First, you need to **fork** the Fedora Happiness Packets repo on Pagure.io to your Pagure account.
Then, clone your fork to your workstation using **git**.
For extra help, see the `Pagure first steps <https://docs.pagure.org/pagure/usage/first_steps.html>`__ help page.
Once you clone your fork, you need to run a script to generate authentication tokens (more on this later).

::

    git clone "ssh://git@pagure.io/forks/<username>/fedora-commops/fedora-happiness-packets.git"
    cd fedora-happiness-packets
    ./generate_client_secrets.sh

Although Docker runs this script during container build-time, please generate a local copy first.
This way, new client keys are not being generated each time the container is rebuilt.
This avoids rate-limiting by the authentication service.

Add FAS account login info
==========================

Next, you need to configure Fedora Happiness Packets with your Fedora Account System (FAS) username and password.
This is used to authenticate with Fedora APIs for username search.
Copy the example file ``fas-admin-details.json.example`` as a new file named ``fas-admin-details.json``.
Add your username and password into the quotes.

Create a project config file
============================

Next, create a configuration file to add admin users to Fedora Happiness Packets.
Like before, copy ``config.yml.example`` to a new file named ``config.yml``.
Add your name and ``@fedoraproject.org`` email address for `ADMINS <https://docs.djangoproject.com/en/2.1/ref/settings/#admins>`_.
For superuser privileges, add your FAS username to the list.

How to test sending emails
==========================

In the development environment, sending emails is tested in one of two ways:

* Using console
* Using third-party mail provider (e.g. Gmail

Using console
-------------

The default setup is to send emails on the console.
The full content of emails will appear in the ``docker-compose`` console output (explained below).
To see this in action, no changes are needed.

Using Gmail
-----------

Sending real, actual emails can be tested with a third-party mail provider, like Gmail.
There are other mail services you can use, but this guide explains using Gmail.
To test this functionality:

#. In ``settings/dev.py``, un-comment the setting for ``Configurations to test sending emails using Gmail SMTP``.
   Comment out the setting under ``Configurations for sending email on console``.
   In ``docker-compose.yml``, un-comment the ports setting in ``celery`` service.
#. Enable `less secure apps <https://myaccount.google.com/lesssecureapps>`_ in the Gmail account which you want to use as the host email.
   (It is strongly recommended to not allow less secure apps in your primary Gmail account.
   A separate account for testing is recommended with this setting enabled.)
#. Replace ``<HOST@EMAIL.COM>`` and ``<HOST_EMAIL_PASSWORD>`` with the email address of the above account and its password.


**************************************************
Start Fedora Happiness Packets with Docker Compose
**************************************************

Now you are ready to start Fedora Happiness Packets!
You will use Docker Compose to start all the containers used at the same time (like Redis, Celery, and others).
Run this command to start up the project::

    docker-compose up

Once it finishes starting up, open `localhost:8000 <http://localhost:8000/>`__ in your browser
You should see the Fedora Happiness Packets home page.

Thanks to `PR #235 <https://pagure.io/fedora-commops/fedora-happiness-packets/pull-request/235>`__ from `@ShraddhaAg <https://twitter.com/ShraddhaAg>`__, changes to Django code, HTML templates, and CSS/JavaScript are automatically reloaded while ``docker-compose`` is running.
You should not need to rebuild the containers every time you make a change.
However, sometimes you will need to rebuild the containers (e.g. adding a new dependency).
This can be done with the following command::

    docker-compose up --build

Run integration tests
=====================

Integration tests are tests that ensure an application works fully from beginning to end.
Fedora Happiness Packets is not fully tested, but there are some integration tests.
To run integration tests, you need to enter the container while it is running and run the test suite.
Open a new window and run this command to open a shell prompt inside the Django web app container::

    docker-compose exec web bash

Once inside the container, run this command::

    docker-compose exec web ./manage.py test -v 2 -p integration_test*.py --settings=happinesspackets.settings.tsting

Test ``fedora-messaging`` integration
=====================================

To test if messages are being sent to the RabbitMQ broker, open a new terminal while ``docker-compose`` is running.
Run the following commands::

    docker-compose exec web bash
    fedora-messaging consume --callback=fedora_messaging.example:printer

The messages sent to the RabbitMQ broker, when a sender confirms sending a happiness packet, will be printed in this terminal.


**********************
Alternatives to Docker
**********************

There are other ways to run Fedora Happiness Packets without containers or Docker.
However, this is discouraged as current maintainers use containers to test changes and deploy Fedora Happiness Packets to production.
If you choose to not use Docker and set up everything manually, you may run into unexpected issues.
Project maintainers cannot easily help you if you choose this route (and may not be able to help you)!
Therefore, please consider very carefully if you wish to run everything locally without containers.


***************
Troubleshooting
***************

Windows: ``alpinelinux.org error ERROR: unsatisfiable constraints``
===================================================================

On Windows, you might get the above error when running ``docker-compose``.
This can be resolved by following these steps:

#. Open Docker settings.
#. Click on Network.
#. Look for "DNS Server" section.
#. It is set to *Automatic* by default.
   Change it to *Fixed*.
#. The IP address should now be editable.
   Try changing it to ``1.1.1.1``.
#. Save settings.
#. Restart Docker.
