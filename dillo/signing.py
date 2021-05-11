'''
Object Transport Signing Meta Class
Ported from loopyCryptor

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
__version__ = "0.1.0"
__author__ = "Anubhav Mattoo"
__email__ = "anubhavmattoo@outlook.com"
__license__ = "MIT"
__status__ = "Beta"


class Sign():
    """
    Signing Meta-Class for Object Signing
    Signs MD5, SHA256, SHA3_256
    """

    def __init__(self):
        '''
        DO NOT Init this Class
        '''
        raise AttributeError("DO NOT INIT, CYKA!")

    @staticmethod
    def md5(data: bytes, ret_hex=True):
        '''
        MD5 Signature of the Data
        '''
        from Crypto.Hash import MD5
        md5_ = MD5.new()
        data = [data[x:x+500] for x in range(0, len(data), 500)]
        for item in data:
            md5_.update(item)
        return md5_.hexdigest() if ret_hex else md5_

    @staticmethod
    def sha256(data: bytes, ret_hex=True):
        '''
        SHA256 Signature of the Data
        '''
        from Crypto.Hash import SHA256
        sha_ = SHA256.new()
        data = [data[x:x+1024] for x in range(0, len(data), 1024)]
        for item in data:
            sha_.update(item)
        return sha_.hexdigest() if ret_hex else sha_

    @staticmethod
    def sha3_256(data: bytes, ret_hex=True):
        '''
        SHA3_256 Signature of the Data
        '''
        from Crypto.Hash import SHA3_256
        sha_ = SHA3_256.new()
        data = [data[x:x+1024] for x in range(0, len(data), 1024)]
        for item in data:
            sha_.update(item)
        return sha_.hexdigest() if ret_hex else sha_
