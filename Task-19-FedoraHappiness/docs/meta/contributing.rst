########################################
Contributing to fedora-happiness-packets
########################################

These guidelines explain how to submit changes to `fedora-happiness-packets <https://pagure.io/fedora-commops/fedora-happiness-packets>`__.
Following these guidelines help maintainers respond to new tickets and pull requests.
Not following these guidelines may make it harder or take longer to review your change.
If you have questions about any of these guidelines, please ask in the `Community Operations team channels <https://docs.fedoraproject.org/en-US/commops/#find-commops>`__.


*****
Goals
*****

Our goals are the purpose of our development.
All changes should align to project goals.
This helps focus our development efforts and be a considerate downstream (a.k.a. forked) project.
Changes that do not align to these goals may not be accepted by maintainers.

More goals may be added or changed in the future.

1. fedora-happiness-packets is a fork.
======================================

`fedora-happiness-packets <https://pagure.io/fedora-commops/fedora-happiness-packets>`__ is a fork of `mxsasha/happinesspackets <https://github.com/mxsasha/happinesspackets>`__.
The upstream project is also active and still in use.
As a considerate downstream, if a change could also help upstream, we should direct changes there.

If a change to our project is also useful to upstream, always `file a new issue <https://github.com/mxsasha/happinesspackets/issues/new>`__ to see if upstream wants to accept a change.
A positive relationship with our upstream project is important.

2. fedora-happiness-packets supports changes required for deployment in Fedora community.
=========================================================================================

Changes to fedora-happiness-packets should generally be Fedora-specific.
This includes `fedora-messaging <https://fedora-messaging.readthedocs.io/>`__ support, Fedora-related design changes, or integrating into other parts of the Fedora community.
Sometimes there are exceptions.
When deciding exceptions, always consider Goal 1.

3. Good code is tested code.
============================

Introducing new code means adding unit tests.
Fedora Happiness Packets uses the `Django test suite <https://docs.djangoproject.com/en/dev/topics/testing/>`__ and `pytest <https://pytest.org/>`__ for testing.
As a rule of thumb, consider this wisdom when writing tests:

* Use test functions and plain-old ``assert`` statements.
* Ideally, test functions should be *around* five lines and assert one thing.
* If you need multiple test classes, inheritance, or OOP, you might be doing it wrong.
* If you need to make imports from other test directories, you might be doing it wrong.
* If you need more than two levels of indentation, you might be doing it wrong.
* "There's a plugin for that!"
  Pytest has a rich `plugin community <https://docs.pytest.org/en/latest/plugins.html>`__ with almost anything you can think of.
  Take advantage of them!
* Don't use ``@mock.patch`` or ``with mock.patch``.
  Use `pytest fixtures <https://pythontesting.net/framework/pytest/pytest-fixtures-nuts-bolts/>`__. [#]_

********************************
Create a development environment
********************************

See :doc:`../setup/development`.


*************************
Start working on a ticket
*************************

Want to work on a new ticket?
Follow these three steps:

1. Check if ticket has |PASSED| label
2. Check if ticket is already assigned
3. Leave a comment in the ticket to work on it

Issues with the |PASSED| label passed maintainer review.
This means they are accepted as tasks to work on.
Working on a ticket without the |PASSED| label means your work may not be accepted.

If someone else is already assigned, it means the task is **already in progress**.
An assigned ticket is not available to start new work.
If a ticket has no updates for longer than seven days, you may follow up and ask if the assignee is still working on the ticket.

Finally, **leave a comment** in the ticket you want to work on.
A maintainer will reply asking for more information or they will assign the ticket to you.
When you are assigned a ticket, this means you are approved to work on it.

Inactive tickets
================

Sometimes, an assignee of a ticket may no longer have time to work on a ticket.
**After five days of no updates, a ticket can be reassigned by a project maintainer.**
This *DOES NOT* mean all tickets must be solved in five days.
It *DOES* mean if an assignee does not respond to new comments in a ticket after five days of their last comment, it can be re-assigned.
This helps to keep tickets open and available for those who have time to work on them.

If you are working on a ticket and more than five days have passed since your last comment, please give an update when possible.


*********************
Submit a pull request
*********************

These guidelines help maintainers review new pull requests.
Stick to the guidelines for faster pull request reviews.

1. Prefer gradual small changes than sudden big changes
2. Write a helpful title for your pull request (if someone reads only one sentence, will they understand your change?)
3. Address the following questions in your pull request:

   1. What is a summary of your change?
   2. Why is this change helpful?
   3. Any specific details to consider?
   4. What do you think is the outcome of this change?

4. Include screenshots of before/after if your change is a front-end change.

Maintainer response time
========================

Project maintainers / mentors are committed to **no more than three days for a reply** during Fedora Summer Coding project cycles.
Current maintainers are volunteers working on the project, so we try to keep up with the project as best we can.
If more than three days have passed and you have not received a reply, follow up with the `Community Operations team channels <https://docs.fedoraproject.org/en-US/commops/#find-commops>`__ team.
Someone may have missed your comment – no one is intentionally ignored.

*Remember*, using issue templates and answering the above questions in pull requests reduces response time from a maintainer to your ticket / PR.


.. [#] You can still use ``mock.patch``.
       It has more features than pytest's monkeypatch fixture.
       But don't use it with a decorator, which has a problem of applying at import time nor using it in ``with`` statements.
       Instead, you would use it with ``pytest-mock``, which exports the Mock API via a ``mocker`` fixture.
       The fixture ensures the enter/exit context happens at the usual time in pytest setup/teardown.

.. |PASSED| image:: https://pagure.io/fedora-commops/fedora-happiness-packets/issue/raw/files/d4820df9449fd61951d807b5fe86231092a31db15932759b2b7b810262c002d0-Screenshot_2019-02-24_Settings_-_fedora-commops_fedora-happiness-packets_-_Pagure_io.png
   :target: https://pagure.io/fedora-commops/fedora-happiness-packets/issues?status=Open&tags=PASSED
