# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def dummy(request):
    """
    Dummy view
    """
    result = {}
    result['title'] = "OK !"
    return render_to_response('dummy.html',result,
                                          context_instance=RequestContext(request))
