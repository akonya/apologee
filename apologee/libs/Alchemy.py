import gevent
from gevent import monkey
import AlchemyAPI
from urllib import urlencode
from urllib2 import urlopen
from abc import ABCMeta,abstractmethod
import json

gevent.monkey.patch_all()

_alchemy_key = ''

class InvalidKey(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid key is provided, Alchemy needs a proper private key.")

class BadAPIRequest(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

class BadAPIResponse(Exception):
    def __init__(self, j):
        Exeception.__init__(self, json.dump(j))

def initAPIPrivateKey(key):
    """ Set the Alchemy API private key. It's shared for all following API calls.
    key is either a file object or a plain string """
    if not key:
        raise InvalidKey
    try:
        r = key.read
        if callable(r):
            global _alchemy_key
            _alchemy_key = key.read()
    except AttributeError:
        global _alchemy_key
        _alchemy_key = key

class AbstractAlchemyRequest(gevent.Greenlet, object):
    """ This abstract class indicates a basic Alchemy API.
    Usually an API has a corresponding endpoint."""
    __metaclass__ = ABCMeta
    _outputmode = 'json'
    def __init__(self, endpoint, params, data):
        gevent.Greenlet.__init__(self)
        self._endpoint = endpoint
        self._params = urlencode(params)
        self._data = data
        self._data["apikey"] = _alchemy_key
        self._data["outputMode"] = "json"

    def getdata(self):
        return self._data
    def setdata(self, data):
        self._data = data

    def _run(self):
        url = self._endpoint + ('?' + self._params if self._params else '')
        result = urlopen(url, urlencode(self._data))
        self._result = result.read()
        return result
    @abstractmethod
    def result(self):
        pass

class TextSentimentRequest(AbstractAlchemyRequest):
    _endpoint = 'http://access.alchemyapi.com/calls/text/TextGetTextSentiment'
    def __init__(self, **kwargs):
        AbstractAlchemyRequest.__init__(self, TextSentimentRequest._endpoint, {}, kwargs)
        try:
            self.__text = kwargs['text']
        except AttributeError:
            self.__text = ''

    def gettext(self):
        return self.__text

    def settext(self, t):
        self.__text = t

    def result(self):
        r = json.loads(self._result)
        try:
            st = r['status']
            if st != 'OK':
                raise BadAPIRequest(r['statusInfo'])
            else:
                return r['docSentiment']
        except AttributeError:
            raise BadAPIResponse("The remote returned invalid data.")

def getSentiment(text):
    req = TextSentimentRequest(text = text)
    req.start()
    req.join()
    return req.result()
