#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

#
# (c) 2013 Heinlein Support GmbH
#          Robert Sander <r.sander@heinlein-support.de>
#

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  This file is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from collections.abc import Iterator, Mapping, Sequence

from pydantic import BaseModel

from cmk.server_side_calls.v1 import (
    ActiveCheckCommand,
    ActiveCheckConfig,
    HostConfig,
    Secret,
    noop_parser,
)

from cmk.utils import debug
from pprint import pprint

def generate_imap_commands(
    params: Mapping[str, object],
    host_config: HostConfig,
) -> Iterator[ActiveCheckCommand]:
    if debug.enabled():
        pprint(params)
        pprint(host_config)
    yield ActiveCheckCommand(
        service_description="IMAP XXX",
        command_arguments=[],
    )

active_check_imap = ActiveCheckConfig(
    name="imap",
    parameter_parser=noop_parser,
    commands_function=generate_imap_commands,
)

# def check_imap_arguments(params):
#     args = ""

#     service_desc, options = params

#     if 'hostname' in options:
#         args += " -H %s" % quote_shell_string(options['hostname'])
#     else:
#         args += " -H $HOSTADDRESS$"

#     if 'ssl' in options:
#         args += " -S"
#         if 'port' in options:
#             args += " -p %d" % options['port']
#         else:
#             args += " -p 993"
#     else:
#         if 'port' in options and options['port'] != 143:
#             args += " -p %d" % options['port']

#     if "ip_version" in options:
#         if options['ip_version'] == 'ipv4':
#             args += ' -4'
#         else:
#             args += ' -6'

#     if 'send' in options:
#         args += ' -s "%s"' % options['send']

#     if 'expect' in options:
#         args += ' -e "%s"' % options['expect']

#     if 'quit' in options:
#         args += ' -q "%s"' % options['quit']

#     if 'refuse' in options:
#         args += ' -r %s' % options['refuse']

#     if 'mismatch' in options:
#         args += ' -M %s' % options['mismatch']

#     if 'jail' in options:
#         args += ' -j'

#     if 'maxbytes' in options:
#         args += ' -m %d' % options['maxbytes']

#     if 'delay' in options:
#         args += ' -d %s' % options['delay']

#     if 'certificate_age' in options:
#         args += ' -D %d,%d' % ( options['certificate_age'][0], options['certificate_age'][1] )

#     if 'warning' in options:
#         args += ' -w %d' % options['warning']

#     if 'critical' in options:
#         args += ' -c %d' % options['critical']

#     if 'timeout' in options:
#         args += ' -t %d' % options['timeout']

#     return args

# def check_imap_description(params):
#     return params[0]

# active_check_info['imap'] = {
#     "command_line": "$USER1$/check_imap $ARG1$",
#     "argument_function": check_imap_arguments,
#     "service_description": check_imap_description,
#     "has_perfdata": True,
#     }
