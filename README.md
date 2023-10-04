# IPv4 Network & Broadcast Address Identifier
October 2023

## Objective
- Identify proper IPv4 Addresses utilizing a given IP address with its Subnet Mask for Networking practices.

## How to Use (Bash)
1. Make sure you have Python3 installed on your device.
2. Download the script and navigate to the project's directory.
3. Locate and give the script executable permissions via your CLI: `chmod u+x net_identifier.py`
4. Run the script via the CLI: `./net_identifer.py`
5. Enter your given IPV4 address to test and Subnet Mask.
6. Results should come in seconds.

## Defining the Code
### Imports
- Line 1: Shebang line to let system know Python3 is the interpreter we will utilize.
- Line 2: Import the `ipaddress` module built-in.

### Identifier
- Line 5: Defines our identifier function and takes input as String IP/Subnet Mask.
- Line 7-8: Converts the String inputs into IPv4 objects.
- Line 10: Returns the newly converted inputs onto our logic function.
- Line 12-13: Except block handles issues with the format of the input, throwing an error message.

### Logics
- Line 17-18: Checks if the parameters are private IP Addresses utilizing our module's checker, returning a message if not private.
- Line 20-21: Creates the Network Address (bundled IP Address & Subnet Mask) and the Broadcast Address objects.
- Line 23: Returns a message using printf to add in variables.

### Inputs & End
- Line 26-27: Gather the inputs of the user for IPv4 and Subnet Mask
- Line 29-30: Calls in initial identifier function with User input, ending with printing the results after the entire script runs.