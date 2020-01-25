# Ansible Vault
What is Ansible vault? Why should we use it? Doesn't take a lot of time, but worth your time learning something which works instantly and secure.

In a single sentence, `ansible-vault secures confidential data by encrypting it on disk`

Vault is implemented with file-level granularity, meaning that files are either entirely encrypted or unencrypted. It uses the AES256 algorithm to provide symmetric encryption keyed to a user-supplied password

### Examples

`$ ansible-vault create vault.yml`

This creates a file named `vault.yml`, and prompts a password to secure the following file.

Now you'll be redirected to a vi/vim text editor to input your text. On saving the file, you're done with it and ansible-vault encrypts it.

`$ ansible-vault view vault.yml`

This prompts for the password which was used for encrypting the file, on entering the correct one, the contents of the file are displayed on the terminal (sort of `cat vault.yml` after hitting the password)
