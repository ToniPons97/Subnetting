def decimalToBinary(number):
    dividend = 1
    remainder = 0
    exp = 0
    binary = 0
    
    while dividend != 0:
        dividend = int(divmod(number / 2, 1)[0])
        remainder = number % 2
        number = dividend
        binary += remainder * 10 ** exp
        exp += 1

    return binary


def ipToBinary(ip):
    ipBinary = [list(str(decimalToBinary(i))) for i in ip]

    max_length = 0

    for i, v in enumerate(ipBinary):
        for j, k in enumerate(v):
            ipBinary[i][j] = int(ipBinary[i][j])

    for i in ipBinary:
        if len(i) > max_length:
            max_length = len(i)
    
    for i in ipBinary:
        if len(i) < max_length:
            while len(i) < max_length:
                i.insert(0, 0)
    return ipBinary


def ipStringToDecimal(ipstring):
    return [int(i) for i in ipstring.split(".")]

def ipListToString(ipList):
    ipString = ""
    for i in ipList:
        ipString += str(i) + "."
    return ipString[:-1]


def getNetworkPrefix(ipaddress, netmask):
    ipaddress = ipStringToDecimal(ipaddress)
    netmask = ipStringToDecimal(netmask)

    networkPrefix = []

    if len(ipaddress) == len(netmask):
        for i, j in enumerate(ipaddress):
            networkPrefix.append(j & netmask[i])
    else:
        return "ip address and network mask lengths do not match."

    return networkPrefix

def getCIDR(binaryNetmaskList):
    unpackedNetmask = [j for i in binaryNetmaskList for j in i]
    counter = 0

    for i in unpackedNetmask:
        if i == 1:
            counter += 1
        else:
            break

    return counter

def getMaxHosts(CIDR):
    return 2 ** (32 - CIDR) - 2