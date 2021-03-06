:mod:`gs.group.list.command`
============================

Contents:

.. toctree::
   :maxdepth: 2

   api
   HISTORY

Introduction
============

This product provides support for email-commands. It does this by
providing a function for processing commands (to check for a
command in an email message), a way to `register command
processors`_, and the result enumeration for returning the result
of a command.

Register command processors
===========================

The commands are named *adaptors* that implement the
:class:`gs.group.list.command.interfaces.IEmailCommand`
interface. The *name* is the command-name in **lower case.** So
the command to unsubscribe someone from a group will have the
adaptor name ``unsubscribe``. The adaptor must

* Take the group in the :meth:`__init__` method (it adapts the
  group),
* Provide a :meth:`process` method that takes the email and
  browser-request as an argument.

Example
-------

I prefer to declare adaptors using ZCML. This will declare a
command named ``example``. This command will be executed by
:func:`process_command` whenever the subject line of an email
message contains starts with ``example`` (in upper or lower
case). The command itself is implemented by the
:class:`ExampleCommand` class in the :mod:`example` module in the
local directory:

.. code-block:: xml

  <adapter
    name="example"
    for="gs.group.base.interfaces.IGSGroupMarker"
    provides="gs.group.list.command.interfaces.IEmailCommand" 
    factory=".example.ExampleCommand" />

The :mod:`example` module would contain the
:class:`ExampleCommand` class, which inherits from the abstract
base-class for commands.

.. code-block:: python

  from gs.group.list.command import CommandABC, CommandResult
  class ExampleCommand(CommandABC):
      def process(email, request):
          # TODO: Stuff
          return CommandResult.commandStop

The ``request`` is passed in to the :meth:`process` method so the
class can issue email-notifications.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

