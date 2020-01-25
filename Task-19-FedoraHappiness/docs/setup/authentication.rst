==============
Authentication
==============

The Fedora Happiness Packets project uses Open ID Connect in order to access the Fedora Account System in order to retrieve the user's email and name.
This means that in order for packet sending functionality to work, the server that this project is running on must have a client ID and secret from the Fedora Infrastructure OIDC provider.

Development
===========

In order to obtain a Client ID and Secret for a development server, simply run the ``generate_client_secrets.sh`` located at the project root. The script will not run if it finds a client_secrets.json file, preventing API abuse.

Alternatively, you may use the `oidc-register <https://github.com/puiterwijk/oidc-register>`_ tool to generate a client ID. However,the project expects to have a file as returned by the ``generate_client_secrets.sh`` script, so if you have any issues with ``oidc-register``, use the script.


Staging/Production
==================

File a ticket with the Fedora Infrastructure team: https://pagure.io/fedora-infrastructure/issues


More information on the authentication structure can be found in the Fedora wiki: https://fedoraproject.org/wiki/Infrastructure/Authentication
