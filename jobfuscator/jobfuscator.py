#!/usr/bin/env python

###############################################################################
#
# JObfuscator is a source code obfuscator for the Java programming language.
# Obfuscate and protect your Java source code and algorithms from hacking,
# cracking, reverse engineering, decompilation, and technology theft.
# 
# JObfuscator provides advanced Java source code parsing based on AST trees,
# multiple advanced obfuscation strategies are available.
#
# Version      : JObfuscator v1.04
# Python       : Python v3
# Dependencies : requests (https://pypi.python.org/pypi/requests/)
# Author       : Bartosz Wójcik (support@pelock.com)
# Project      : https://www.pelock.com/products/jobfuscator
# Homepage     : https://www.pelock.com
#
###############################################################################

import zlib
import base64

# required external package - install with "pip install requests"
import requests


class JObfuscator(object):
    """JObfuscator module"""

    # 
    # @var string default JObfuscator WebApi endpoint
    # 
    API_URL = "https://www.pelock.com/api/jobfuscator/v1"

    # 
    # @var string WebApi key for the service
    # 
    _apiKey = ""

    # 
    # @var bool should the source code be compressed
    # 
    enableCompression = True

    # 
    # @var bool change linear code execution flow to non-linear version
    # 
    mixCodeFlow = True

    # 
    # @var bool rename variable names to random string values
    # 
    renameVariables = True

    # 
    # @var bool rename method names to random string values
    # 
    renameMethods = True

    # 
    # @var bool shuffle functions order in the output source
    # 
    shuffleMethods = True

    #
    # @var bool encrypt integers using more than 15 floating point math functions from the java.lang.Math.* class
    #
    intsMathCrypt = True

    #
    # @var bool encrypt strings using polymorphic encryption algorithms
    # 
    cryptStrings = True

    #
    # @var bool for each method, extract all possible integers from the code and store them in an array
    #
    intsToArrays = True

    #
    # @var bool for each method, extract all possible doubles from the code and store them in an array
    #
    dblsToArrays = True

    # 
    # @var integer success
    # 
    ERROR_SUCCESS = 0

    # 
    # @var integer invalid size for source code (it's 1500 bytes max. for demo version)
    # 
    ERROR_INPUT_SIZE = 1

    # 
    # @var integer input source is empty
    # 
    ERROR_INPUT = 2

    # 
    # @var integer Java source code parsing error
    # 
    ERROR_PARSING = 3

    # 
    # @var integer Java parsed code obfuscation error
    # 
    ERROR_OBFUSCATION = 4

    # 
    # @var integer error while generating output code
    # 
    ERROR_OUTPUT = 5

    def __init__(self, api_key=None, enable_all_obfuscation_options=True):
        """Initialize JObfuscator class

        :param api_key: Activation key for the service (it can be empty for demo mode)
        :param enable_all_obfuscation_options: Enable or disable all of the obfuscation options
        """

        self._apiKey = api_key
        
        self.enableCompression = enable_all_obfuscation_options
        self.mixCodeFlow = enable_all_obfuscation_options
        self.renameVariables = enable_all_obfuscation_options
        self.renameMethods = enable_all_obfuscation_options
        self.shuffleMethods = enable_all_obfuscation_options
        self.intsMathCrypt = enable_all_obfuscation_options
        self.cryptStrings = enable_all_obfuscation_options
        self.intsToArrays = enable_all_obfuscation_options
        self.dblsToArrays = enable_all_obfuscation_options

    def login(self):
        """Login to the service and get the information about the current license limits

        :return: An array with the results or False on error
        :rtype: bool,dict
        """

        # parameters
        params = {"command": "login"}

        return self.post_request(params)

    def obfuscate_java_file(self, java_file_path):
        """Obfuscate Java source code file using provided parameters

        :param java_file_path: Java source code *.java file path
        :return: An array with the results or False on error
        :rtype: bool,dict
        """

        source_file = open(java_file_path, 'r')
        source = source_file.read()
        source_file.close()
    
        if not source:
            return False
    
        return self.obfuscate_java_source(source)

    def obfuscate_java_source(self, java_source):
        """Obfuscate Java source code using provided parameters

        :param java_source: Java source code
        :return: An array with the results or False on error
        :rtype: bool,dict
        """

        # additional parameters
        params_array = {"command": "obfuscate", "source": java_source}

        return self.post_request(params_array)

    def post_request(self, params_array):
        """Send a POST request to the server

        :param params_array: An array with the parameters
        :return: An array with the results or false on error
        :rtype: bool,dict
        """

        # add activation key to the parameters array
        if self._apiKey:
            params_array["key"] = self._apiKey

        #
        # obfuscation strategies
        #
        if self.mixCodeFlow:
            params_array["mix_code_flow"] = "1"
        if self.renameVariables:
            params_array["rename_variables"] = "1"
        if self.renameMethods:
            params_array["rename_methods"] = "1"
        if self.shuffleMethods:
            params_array["shuffle_methods"] = "1"
        if self.intsMathCrypt:
            params_array["ints_math_crypt"] = "1"
        if self.cryptStrings:
            params_array["crypt_strings"] = "1"
        if self.intsToArrays:
            params_array["ints_to_arrays"] = "1"
        if self.dblsToArrays:
            params_array["dbls_to_arrays"] = "1"

        #
        # check if compression is enabled
        #
        if "source" in params_array and self.enableCompression and params_array["source"]:

            compressed_data = zlib.compress(bytes(params_array["source"], 'utf-8'), 9)
            base64_encoded_data = base64.b64encode(compressed_data).decode()

            params_array["source"] = base64_encoded_data
            params_array["compression"] = "1"

        response = requests.post(self.API_URL, data=params_array)

        # no response at all or an invalid response code
        if not response or not response.ok:
            return False

        # decode to json array
        result = response.json()

        # depack output code back into the string
        if "output" in result and self.enableCompression and result["error"] == self.ERROR_SUCCESS:

            result["output"] = str(zlib.decompress(base64.b64decode(result["output"])), "utf-8")

        # return original JSON response code
        return result
