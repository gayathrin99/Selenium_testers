import socket
import struct
import textwrap
def ethernet_frame(data):
    dest_mac,src_mac,proto = struct.unpack('! 6s 6s H', data[:14])
    print(dest_mac)
    return get_mac_address(dest_mac), get_mac_address(src_mac), socket.htons(proto), data[14:]
def get_mac_address(bytes_addr):
    bytes_str=map('{:o2x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()
