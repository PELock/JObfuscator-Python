#!/usr/bin/env python

###############################################################################
#
# JObfuscator WebApi interface usage example.
#
# In this example we will obfuscate sample source with custom options.
#
# Version        : v1.04
# Language       : Python
# Author         : Bartosz Wójcik
# Web page       : https://www.pelock.com
#
###############################################################################

#
# include JObfuscator module
#
from jobfuscator import JObfuscator

#
# if you don't want to use Python module, you can import directly from the file
#
#from pelock.jobfuscator import JObfuscator

#
# create JObfuscator class instance (we are using our activation key)
#
myJObfuscator = JObfuscator("ABCD-ABCD-ABCD-ABCD")

#
# global obfuscation options
#
# when disabled will discard any @Obfuscate annotation declaration
# in the Java source code
#
# you can disable a particular obfuscation strategy globally if it
# fails or you don't want to use it without modifying the source codes
#
# by default all obfuscation strategies are enabled
#

#
# should the source code be compressed (both input & compressed)
#
myJObfuscator.enableCompression = True

#
# change linear code execution flow to non-linear version
#
myJObfuscator.mixCodeFlow = True

#
# rename variable names to random string values
#
myJObfuscator.renameVariables = True

#
# rename method names to random string values
#
myJObfuscator.renameMethods = True

#
# shuffle order of methods in the output source
#
myJObfuscator.shuffleMethods = True

#
# encrypt integers using more than 15 floating point math functions from the java.lang.math.* class
#
myJObfuscator.intsMathCrypt = True

#
# encrypt strings using polymorphic encryption algorithms
#
myJObfuscator.cryptStrings = True

#
# for each method, extract all possible integers from the code and store them in an array
#
myJObfuscator.intsToArrays = True

#
# for each method, extract all possible doubles from the code and store them in an array
#
myJObfuscator.dblsToArrays = True

#
# source code in Java format
#
sourceCode = """import java.util.*;
import java.lang.*;
import java.io.*;

//
// you must include custom annotation
// to enable entire class or a single
// method obfuscation
//
@Obfuscate
class Ideone
{
    //@Obfuscate
    public static double calculateSD(double numArray[])
    {
        double sum = 0.0, standardDeviation = 0.0;
        int length = numArray.length;

        for(double num : numArray) {
            sum += num;
        }

        double mean = sum/length;

        for(double num: numArray) {
            standardDeviation += Math.pow(num - mean, 2);
        }

        return Math.sqrt(standardDeviation/length);
    }

    //
    // selective obfuscation strategies
    // can be applied for the entire
    // class or a single method (by
    // default all obfuscation strategies
    // are enabled when you use @Obfuscate
    // annotation alone)
    //
    //@Obfuscate(
    //  ints_math_crypt = true,
    //  crypt_strings = true,
    //  rename_methods = false,
    //  rename_variables = true,
    //  shuffle_methods = true,
    //  mix_code_flow = true,
    //  ints_to_arrays = true,
    //  dbls_to_arrays = true
    // )
    public static void main(String[] args) {

        double[] numArray = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        double SD = calculateSD(numArray);

        System.out.format("Standard Deviation = %.6f", SD);
    }
}"""

#
# by default all obfuscation options are enabled, so we can just simply call
#
result = myJObfuscator.obfuscate_java_source(sourceCode)

#
# result[] array holds the obfuscation results as well as other information
#
# result["error"]         - error code
# result["output"]        - obfuscated code
# result["demo"]          - was it used in demo mode (invalid or empty activation key was used)
# result["credits_left"]  - usage credits left after this operation
# result["credits_total"] - total number of credits for this activation code
# result["expired"]       - if this was the last usage credit for the activation key it will be set to True
#
if result and "error" in result:

    # display obfuscated code
    if result["error"] == JObfuscator.ERROR_SUCCESS:

        # format output code for HTML display
        print(result["output"])
    else:
        print(f'An error occurred, error code: {result["error"]}')

else:
    print("Something unexpected happen while trying to obfuscate the code.")
