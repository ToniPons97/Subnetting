#!/usr/local/bin/python3
import argparse
from ipprocessing import getNetworkPrefix, ipStringToDecimal, ipToBinary, ipListToString, getCIDR, getMaxHosts


def receiveConfig():
    parser = argparse.ArgumentParser(description="Get network information from ip address and subnet mask")
    parser.add_argument("--ip", help="ip address")
    parser.add_argument("--netmask", help="network mask")

    return parser.parse_args()


def main():
    config = receiveConfig()

    if config.ip and config.netmask:
        networkPrefix = ipListToString(getNetworkPrefix(config.ip, config.netmask))
        netmaskBinary = ipToBinary(ipStringToDecimal(config.netmask))

        print(f"Network: {networkPrefix}/{getCIDR(netmaskBinary)}")
        print(f"Hosts: {getMaxHosts(getCIDR(netmaskBinary))}")
        print(f"Network prefix: {networkPrefix}")
    else:
        if not config.ip:
            print("ip missing")
        if not config.netmask:
            print("Network mask missing")


if __name__ == "__main__":
    main()