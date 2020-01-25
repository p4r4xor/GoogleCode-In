======
Model
======

Data Fields
===========

- ``status``: Indicates the status of the message:
    * 'pending_sender_confirmation': The sender has yet to click on the confirmation email.
    * 'sent': The sender has confirmed the email, and it has been sent to the recipient.
    * 'read': The recipient has read the email.
- ``sender_name``: Name of the sender of the packet.
- ``sender_email``: Email address of sender.
- ``sender_email_stripped``: Email address of sender without aliases, to prevent circumvention of the blacklist.
- ``sender_email_token``: Prevents CSRF by ensuring the link has been accessed from the email.
- ``sender_ip``: IP address of sender: rate-limiting takes place in order to prevent resource abuse.
- ``recipient_email``: Name of the recipient of the packet.
- ``recipient_email``: Email address of recipient.
- ``recipient_email_stripped``: Email address of recipient without aliases, to prevent circumvention of the blacklist.
- ``recipient_email_token``: Prevents CSRF by ensuring the link has been accessed from the email.
- ``message``: The text content of the message.
- ``sender_named``: Boolean indicating whether the sender wishes to reveal their identity to the packet recipient. If false, the recipient receives an anonymous packet.
- ``sender_approved_public``: Boolean indicating whether the sender wishes to make the contents of the packet public. (Both the sender and the recipient must approve making the packet public in order for it to be made available publically).
- ``sender_approved_public_named``: Boolean indicating whether the sender wishes to make their identity as the packet sender public.
- ``recipient_approved_public``: Boolean indicating whether the packet recipient wishes to make its contents public.
- ``recipient_approved_public_named``: Boolean indicating whether the recipient wishes to make their identity as the packet recipient public.
- ``admin_approved_public``: Boolean field indicating whether this message is allowed to be publically shared.


Model Functions
===============

- ``save()``: Strips sender and recipient emails, generates a message ID< and saves the message in the database.
- ``send_sender_confirmation()``: Sends a confirmation email to the sender of the packet.
- ``send_to_recipient()``: Sends the packet to the recipient.

Helper Functions
================

- ``strip_email()``: Removes email aliases and all non-alphanumeric characters, with the exception of the @ symbol.
