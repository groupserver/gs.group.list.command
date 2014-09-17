:mod:`gs.group.list.command` API Reference
==========================================

The API for email-commands is in two parts: `processing
commands`_, and `the result enumeration`_.

Processing commands
-------------------

The :func:`gs.group.list.command.process_command` function is
used to process the commands in an email message.

.. autofunction:: gs.group.list.command.process_command

Example
~~~~~~~

::

  r = process_command(self.group, email, request)
  if r == gs.group.list.command.CommandResult.commandStop:
    return

Command Abstract Base Class
---------------------------

The :class:`CommandABC` abstract base-class provides some useful
functionality

.. autoclass:: gs.group.list.command.CommandABC
   :members:

Sub-classes of :class:`CommandABC` will need to provide the
:meth:`process` method. The browser-request is passed in so the
command can issue email-notifications.

The Result Enumeration
----------------------

The result enumeration is returned by the
:func:`gs.group.list.command.process_command` function, and the
command that are registered.

.. autoclass:: gs.group.list.command.CommandResult
   :members:
