'''
Small dill Wrapper with Metadata

MIT License

Copyright (c) 2021 Anubhav Mattoo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
__version__ = '0.1.0'
__author__ = 'Anubhav Mattoo'
__email__ = "anubhavmattoo@outlook.com"
__license__ = "MIT"
__status__ = "Beta"

import dill
from os import PathLike
from io import BytesIO


class Dillo():
    """
    dill with Metadata and Signing
    """
    def __init__(self, name: str, type: str = 'pickle',
                 sign: str = 'SHA256', **kwargs):
        self.name = name
        self.type = type
        self.sign = sign
        self.protocol = kwargs.pop('protocol', None)
        self.byref = kwargs.pop('byref', None)
        self.fmode = kwargs.pop('fmode', None)
        self.recurse = kwargs.pop('recurse', None)
        self._stream = b''
        self.ignore = kwargs.pop('ignore', None)
        self.tags = set()

    def __bytes__(self):
        return self._stream

    def __repr__(self):
        fstr = f'-----METADATA-----\n'\
             + f'Name   : {self.name}\n'\
             + f'dillO  : {self.type}\n'\
             + f'Sign   : {self.sign}\n'\
             + f'Tags   : {", ".join([x for x in self.tags])}\n'\
             + f'Length : {len(self._stream)} Bytes\n'
        return fstr

    def store(self, obj, **kwargs) -> None:
        '''
        In Memory Strorage
        '''
        self._stream = dill.dumps(obj, self.protocol, self.byref,
                                  self.fmode, self.recurse, **kwargs)

    def read(self, **kwargs):
        '''
        In Memory Read
        '''
        return dill.loads(self._stream, self.ignore, **kwargs)

    def write_file(self, filepath: PathLike):
        '''
        dillO to File
        '''
        data = self.text()
        if self.type == 'pickle':
            with open(filepath, 'wb') as f:
                f.write(self.__repr__().encode())
                f.write(data)
                f.write(self.get_sign())
        elif self.type == 'json':
            with open(filepath, 'w') as f:
                f.write(self.json_string())

    def json_string(self):
        '''
        JSON String Helper
        '''
        import jsonpickle
        self.hash = self.get_sign()[15:]
        return jsonpickle.encode(self)

    def json(self):
        '''
        JSON Object
        '''
        import json
        return json.loads(self.json_string())

    def text(self):
        '''
        Base64 Helper
        '''
        from base64 import urlsafe_b64encode
        data = urlsafe_b64encode(self._stream)
        if len(data) >= 80:
            data = b"".join(data[i:i+79] + b"\n"
                            for i in range(0, len(data), 79))
            data = data[:-1]
        data = f'-----DILLO-----\n'.encode() + data + b'\n'
        return data

    def get_sign(self) -> bytes:
        '''
        Data Signing Helper
        '''
        from .signing import Sign
        if self.sign == 'MD5':
            return b'-----SIGN-----\n' + Sign.md5(self._stream).encode()
        elif self.sign == 'SHA256':
            return b'-----SIGN-----\n' + Sign.sha256(self._stream).encode()
        elif self.sign == 'SHA3-256':
            return b'-----SIGN-----\n' + Sign.sha3_256(self._stream).encode()
        else:
            raise TypeError(f'Unknown Signing Type \'{self.sign}\'')

    def add_tag(self, tag: str) -> None:
        self.tags.add(tag)

    @classmethod
    def read_file(cls, filepath: PathLike):
        '''
        dillO File Reader
        '''
        from base64 import urlsafe_b64decode
        with open(filepath, 'r') as f:
            buffer_data = f.read()
        import re
        regex = r'^-{5}METADATA-{5}\n'\
            + r'(Name   : (?P<name>.*))\n'\
            + r'(dillO  : (?P<type>.*))\n'\
            + r'(Sign   : (?P<sign>.*))\n'\
            + r'(Tags   : (?P<tags>.*))\n'\
            + r'(Length : (?P<length>[0-9]* Bytes))\n'\
            + r'-{5}DILLO-{5}\n'\
            + r'(?P<dillo>[A-Za-z0-9-_=\n]*)'\
            + r'-{5}SIGN-{5}\n(?P<hash>[0-9a-fA-F]*)$'
        parsed_buffer = re.match(regex, buffer_data)
        if parsed_buffer:
            this = cls(parsed_buffer['name'], parsed_buffer['type'],
                       parsed_buffer['sign'])
            this.tags = set(parsed_buffer['tags'].split(', '))
            data = ''.join(parsed_buffer['dillo'].splitlines())
            data = urlsafe_b64decode(data)
            setattr(this, '_stream', data)
            if this.get_sign().decode()[15:] == parsed_buffer['hash']:
                return this
            else:
                raise ValueError('Unverified dillO')
        else:
            try:
                import jsonpickle
                import json
                this = jsonpickle.decode(buffer_data)
                urlsafe_b64decode(
                    json.loads(buffer_data)['hash']['py/b64']).decode()
                if this.get_sign().decode()[15:] ==\
                   urlsafe_b64decode(
                        json.loads(buffer_data)['hash']['py/b64']
                   ).decode():
                    return this
                else:
                    raise ValueError('Unverified dillO')
            except ValueError:
                raise
            except Exception:
                raise TypeError('Incorrect File Format')


class Dillo_Session(object):
    """
    Dillo for Interpreter Sessions
    """
    def __init__(self, name: str, type: str = 'pickle',
                 sign: str = 'SHA256', **kwargs):
        self.name = name
        self.type = type
        self.sign = sign
        self.protocol = kwargs.pop('protocol', None)
        self.byref = kwargs.pop('byref', None)
        self.fmode = kwargs.pop('fmode', None)
        self.recurse = kwargs.pop('recurse', None)
        self._stream = BytesIO()
        self.tags = set()

    def __bytes__(self):
        return self._stream

    def __repr__(self):
        fstr = f'-----METADATA-----\n'\
             + f'Name   : {self.name}\n'\
             + f'dillO  : {self.type}\n'\
             + f'Sign   : {self.sign}\n'\
             + f'Tags   : {", ".join([x for x in self.tags])}\n'\
             + f'Length : {len(self._stream.getvalue())} Bytes\n'
        return fstr

    @classmethod
    def store_session(cls, name: str, type: str = 'pickle',
                      sign: str = 'SHA256',
                      main=None, byref=False, **kwargs):
        '''
        In Memory Storage
        '''
        this = cls(name, type, sign, **kwargs)
        dill.dump_session(this._stream, main, byref, **kwargs)
        this._stream.seek(0)
        return this

    def load_session(self, main=None, **kwargs):
        '''
        In Memory Read
        '''
        dill.load_session(self._stream, main, **kwargs)

    def write_file(self, filepath: PathLike):
        '''
        dillO to File
        '''
        data = self.text()
        if self.type == 'pickle':
            with open(filepath, 'wb') as f:
                f.write(self.__repr__().encode())
                f.write(data)
                f.write(self.get_sign())
        elif self.type == 'json':
            with open(filepath, 'w') as f:
                f.write(self.json_string())

    def json_string(self):
        '''
        JSON String Helper
        '''
        import jsonpickle
        self.hash = self.get_sign()[15:]
        return jsonpickle.encode(self)

    def json(self):
        '''
        JSON Object
        '''
        import json
        return json.loads(self.json_string())

    def text(self):
        '''
        Base64 Helper
        '''
        from base64 import urlsafe_b64encode
        data = urlsafe_b64encode(self._stream.getvalue())
        if len(data) >= 80:
            data = b"".join(data[i:i+79] + b"\n"
                            for i in range(0, len(data), 79))
            data = data[:-1]
        data = f'-----DILLO SESSION-----\n'.encode() + data + b'\n'
        return data

    def get_sign(self) -> bytes:
        '''
        Data Signing Helper
        '''
        from .signing import Sign
        if self.sign == 'MD5':
            return b'-----SIGN-----\n' + Sign.md5(
                self._stream.getvalue()).encode()
        elif self.sign == 'SHA256':
            return b'-----SIGN-----\n' + Sign.sha256(
                self._stream.getvalue()).encode()
        elif self.sign == 'SHA3-256':
            return b'-----SIGN-----\n' + Sign.sha3_256(
                self._stream.getvalue()).encode()
        else:
            raise TypeError(f'Unknown Signing Type \'{self.sign}\'')

    def add_tag(self, tag: str) -> None:
        self.tags.add(tag)

    @classmethod
    def read_file(cls, filepath: PathLike):
        '''
        dillO File Reader
        '''
        from base64 import urlsafe_b64decode
        with open(filepath, 'r') as f:
            buffer_data = f.read()
        import re
        regex = r'^-{5}METADATA-{5}\n'\
            + r'(Name   : (?P<name>.*))\n'\
            + r'(dillO  : (?P<type>.*))\n'\
            + r'(Sign   : (?P<sign>.*))\n'\
            + r'(Tags   : (?P<tags>.*))\n'\
            + r'(Length : (?P<length>[0-9]* Bytes))\n'\
            + r'-{5}DILLO SESSION-{5}\n'\
            + r'(?P<dillo>[A-Za-z0-9-_=\n]*)'\
            + r'-{5}SIGN-{5}\n(?P<hash>[0-9a-fA-F]*)$'
        parsed_buffer = re.match(regex, buffer_data)
        if parsed_buffer:
            this = cls(parsed_buffer['name'], parsed_buffer['type'],
                       parsed_buffer['sign'])
            this.tags = set(parsed_buffer['tags'].split(', '))
            data = ''.join(parsed_buffer['dillo'].splitlines())
            data = urlsafe_b64decode(data)
            this._stream = BytesIO(data)
            this._stream.seek(0)
            if this.get_sign().decode()[15:] == parsed_buffer['hash']:
                return this
            else:
                raise ValueError('Unverified dillO')
        else:
            try:
                import jsonpickle
                import json
                this = jsonpickle.decode(buffer_data)
                urlsafe_b64decode(
                    json.loads(buffer_data)['hash']['py/b64']).decode()
                if this.get_sign().decode()[15:] ==\
                   urlsafe_b64decode(
                        json.loads(buffer_data)['hash']['py/b64']
                   ).decode():
                    return this
                else:
                    raise ValueError('Unverified dillO')
            except ValueError:
                raise
            except Exception:
                raise TypeError('Incorrect File Format')
