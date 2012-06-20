# Copyright (c) 2010 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from gs.skin.ogn.ogs.interfaces import IOGSLayer

from five import grok
from zope.component import createObject
from zope.interface import providedBy
from zope.publisher.interfaces import INotFound
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.security.interfaces import IForbidden

from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass
import Acquisition
import traceback

grok.layer(IOGSLayer)

class NotFound(grok.View):
    grok.name('error.html')
    grok.context(INotFound)
    index = ZopeTwoPageTemplateFile('browser/templates/not_found.pt')

    def contextdir(self):
        return str((str(self.context.error),
                    str(self.context.error.args),
                    str(self.context.error.message),
                    traceback.format_exc()))

    @property
    def siteInfo(self):
        return createObject('groupserver.SiteInfo', 
                self.context)
        
    def update(self):
        self.response.setStatus(404)

    def render(self):
        return self.index(self.context)

class Forbidden(grok.View):
    grok.name('error.html')
    grok.context(IForbidden)

    def update(self):
        self.response.setStatus(403)

    def render(self):
        return HTML_TEMPLATE % (
            self.__class__.__name__, str(self.context.error))


class Error(grok.View):
    grok.name('error.html')
    grok.context(Exception)
    index = ZopeTwoPageTemplateFile('browser/templates/not_found.pt')

    def contextdir(self):
        return str((str(self.context.error),
                    str(self.context.error.args),
                    str(self.context.error.message),
                    str(dir(self.context.error)),
                    traceback.format_exc()))

    @property
    def siteInfo(self):
        return createObject('groupserver.SiteInfo',
                self.context)

    def update(self):
        self.response.setStatus(500)

    def render(self):
        return self.index(self.context)
