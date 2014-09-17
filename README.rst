===============
``gs.database``
===============
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Get a database connection for the current GroupServer instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Authors: `Richard Waid`_; `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-05-21
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

Introduction
============

`GroupServer`_ stores *most* of its data using the `PostgreSQL`_
relational database [#otherData]_. The `SQLAlchemy`_ system is
used to provide the connection between GroupServer and PostgreSQL
[#transaction]_. The ``gs.database`` product provides some
utilities to establish the connection, and use the connection
more easily. Most code will perform a query in the same way, and
not have to consider which `database instance`_ is being used.

See the Sphinx documentation in ``docs`` for more information.


Database Instance
=================

:Note:
  For GroupServer installations with only one site there can only
  be one database instance, so this section can be ignored.

GroupServer is highly scalable:

* One `Zope`_ instance can manage multiple GroupServer instances,
* One GroupServer instance can manage multiple sites, and
* One site can handle multiple groups.

The PostgreSQL database is independent of this. A single
*database instance* can be shared by multiple sites. The main
advantage of this is that the **profile** information is shared
[#profile]_. However, the databases do not need to be shared.

The front-end HTTP proxy is used to set the correct database
instance, in much the same way that the proxy is used to select
the correct skin [#skin]_. The proxy should set the
``HTTP_INSTANCEID`` environment variable in the HTTP request to
the ID of the database to connect to. The
``gs.database.core.getInstanceId`` utility, which is called by
both ``getTable`` and ``getSession``, will then examine this
environment variable to determine the correct database instance
for the current **request**.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.database
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _ConfigParser: http://docs.python.org/library/configparser.html
..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/
.. _Richard Waid: http://groupserver.org/p/richard
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

.. _PostgreSQL: http://www.postgresql.org/

.. [#otherData] Neither files, nor image caches are stored in the
                relational database. These are the the two major
                exceptions to the "data is in the database" rule.

.. _SQLAlchemy: http://www.sqlalchemy.org/

.. [#transaction] `The zope.sqlalchemy product
                  <http://pypi.python.org/pypi/zope.sqlalchemy>`_
                  also provides some integration between Zope
                  transactions and the SQLAlchemy transactions.

.. _Zope: http://zope.org/

.. [#profile] By sharing profile information between sites people
              can use the same profile to log in to multiple
              sites, and do not have to verify their email
              address for each site.

.. [#skin] Skins are not just colour-schemes, but entire
           collections of code. As crazy as it sounds, `selecting
           a skin based on URL
           <http://plone.org/documentation/kb/select-skin-by-url>`_
           can change vast amounts of behaviour, and is normal
           with Zope.
