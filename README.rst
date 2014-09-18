=========================
``gs.group.list.command``
=========================
~~~~~~~~~~~~~~~~~~~~~~~~~~
Email commands for a group
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-09-18
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

It is traditional for mailing lists to support a set of
*commands.* This product provides support for these commands in
GroupServer groups. Commands are extracted from the ``Subject``
line of an email message: the first word is extracted, converted
to lower case, and the command is then looked up. This allows
``Unsubscribe``, ``unsubscribe`` and ``Re: Unsubscribe`` to work,
but ``FYI: unsubscribe`` will be treated as a normal post.

The commands themselves are supplied by other products. This
product just provides the framework for registering commands. The
full Sphinx documentation is provided in the ``docs`` directory
of this product.

Resources
=========

- Documentation: http://gsgrouplistcommand.readthedocs.org/
- Code repository: https://github.com/groupserver/gs.group.list.command
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
