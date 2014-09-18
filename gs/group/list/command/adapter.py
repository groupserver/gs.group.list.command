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
from abc import ABCMeta, abstractmethod
import shlex


class CommandABC(object):
    '''Abstract base-class for command-adaptors

:param object group: The group that is adapted.
    '''
    __metaclass__ = ABCMeta

    def __init__(self, group):
        self.context = self.group = group

    @abstractmethod
    def process(self, email, request):
        '''Process the command in the email

:param email: The email message that contains the command.
:type email: :class:`email.message.Message`
:param request: The HTTP request made to process the email.
:returns: If a command was processed, and if email processing should
          continue.
:rtype: :class:`.CommandResult`

*Concrete* classes must implement this method.'''

    @staticmethod
    def get_command_components(email):
        '''Get the components of the command in the ``Subject``

:param email: The email message that contains the command.
:type email: :class:`email.message.Message`
:returns: The ``Subject`` of the email, split into components and
          lower-cased.
:rtype: list of strings

The :meth:`get_command_components` method splits the command in the
``Subject`` into parts using the :func:`shlex.split` function. The
components of the command are in lower-case, with all ``re:`` parts
discarded.'''
        subj = email['Subject']
        comp = shlex.split(subj)
        retval = [c.lower() for c in comp if c.lower() != 're:']
        return retval
