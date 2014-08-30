# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from email.message import Message
from email.parser import Parser
import shlex
from zope.cachedescriptors.property import Lazy
from zope.component import queryAdapter
from .interfaces import IEmailCommand
from .result import CommandResult


class ProcessEmailCommand(object):
    '''Process an email command

:param group: A group object.
:param email: An email, with the IEmail interface'''

    def __init__(self, group, email):
        self.group = group
        self.email = email

    @Lazy
    def command(self):
        retval = None
        subject = self.email.get('Subject', None)
        if subject:
            components = [c.lower() for c in shlex.split(subject)]
            retval = components[0] if components else None
        return retval

    def process(self):
        '''Process the command in the email

:returns: The result of processign the command
:rtype: ``.result.CommandResult``'''
        retval = CommandResult.notACommand
        if self.command:
            a = queryAdapter(self.group, IEmailCommand, self.command)
            if a:
                retval = a.process(self.email)
        return retval


def process_command(group, email):
    '''Process a command in an email message

:param group: The group that recieved the email message.
:param email: The email message that was recieved (which may or may not
              contain a command).
:type email: str or :class:`email.message.Message`
:returns: If a command was processed, and if email processing should
          continue.
:rtype: :class:`CommandResult`

When an email is recieved it needs to checked to see if its ``Subject``
header is command, and the command executed if necessary. The
:func:`process_command` function performs both of these tasks. The result
will be either

* :attr:`CommandResut.notACommand` if the email is a normal message,
* :attr:`CommandResut.commandStop` if the email contained a command and
  processing should stop, or
* :attr:`CommandResut.commandContinue` if the email contained a command and
  processing should continue.
'''
    if isinstance(email, Message):
        e = email
    elif isinstance(email, basestring):
        p = Parser()
        e = p.parsestr(email)
    else:
        m = 'email must be a string or a email.message.Message'
        raise TypeError(m)
    emailProcessor = ProcessEmailCommand(group, e)
    retval = emailProcessor.process()
    return retval
