fedora-happiness-packets
========================


### Create development environment

These instructions run an instance of fedora-happiness-packets on your local machine for development and testing purposes.
See [setup instructions](https://fedora-happiness-packets.readthedocs.io/setup/development/) in our documentation.

### Setting up the environment

Please install docker and docker-compose before moving onto the next steps.

```
git clone https://github.com/p4r4xor/ultimate-ears.git
cd fedora-happiness
./generate_client_secrets.sh
```

Next step is to edit and enter your FAS account details in the file `fas-admin-details.json`. Both your credentials must be in the quotes.

Now open the file `config.yml` and add your name only in the super-user privileges if you don't have a `@fedoraproject.org` email. 

**Start Fedora Happiness Packets with Docker Compose**

`sudo docker-compose up`

and you're good to go. Open the link `localhost:8000` in any of your browsers to start developing.
