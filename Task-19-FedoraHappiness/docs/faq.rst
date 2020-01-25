##########################
Frequently asked questions
##########################

This page contains frequently asked questions about fedora-happiness-packets.
It includes troubleshooting steps and other project details.


ERROR: Couldn't connect to Docker deamon at http+docker://localhost-is it running?
    Verify the logged in user is member of the docker group.
    To verify logged in user run::

 	sudo usermod -aG docker ${USER}

    If logged in user is not member of the docker group add it using::

	sudo gpasswd -a${USER}

No sample messages on the main page and no messages in Archives, even though both sender and receiver approved to display message publicily.

    This is due to ``admin_approved_public`` not being set. This has to be done manually using shell.
    Steps to resolve:

    1. Access the shell of the container web using::

        docker-compose exec web sh

    2. Acess the Django shell using::

        python manage.py shell

    3. Import the ``Message`` model and query the necessary message.
       [Assuming the variable ``message`` points to the queried object]

    4. Set the ``admin_approved_public`` attribute to True and save the modified object::

        message.admin_approved_public = True
        message.save()

    Now when you access Archives, the message can be seen.

ERROR: for fedora-happiness-packets_redis_1  Cannot start service redis: driver failed programming external connectivity on endpoint fedora-happiness-packets_redis_1 starting userland proxy: listen tcp 0.0.0.0:6379: bind: address already in use
    A redis service is already running on your machine. To see what process is running use::

        sudo netstat -lnp

    End the running process run the web server again using ``docker-compose up``.
    To see processes running on a particular port (eg: 0.0.0.0:6379) Use ``grep`` to filter for that specific port::

        sudo netstat -tulnp | grep 6379
