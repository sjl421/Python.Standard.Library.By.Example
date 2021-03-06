#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get address info for a service
"""

import socket

def get_constants(prefix):
    """Create a dictionary mapping socket module
    constants to their names.
    """
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.doughellmann.com', 'http',
                                   socket.AF_INET,      # family
                                   socket.SOCK_STREAM,  # socktype
                                   socket.IPPROTO_TCP,  # protocol
                                   socket.AI_CANONNAME, # flags
                                   ):
    
    # Unpack the response tuple
    family, socktype, proto, canonname, sockaddr = response

    print 'Family        :', families[family]
    print 'Type          :', types[socktype]
    print 'Protocol      :', protocols[proto]
    print 'Canonical name:', canonname
    print 'Socket address:', sockaddr
    print 
