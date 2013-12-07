'''
a script to generate the hosts file for some domains.
and just call the 'socket.gethostbyname_ex' function and no others
'''

import sys
import socket

def main():
    if len(sys.argv) != 2:
        print("spec the input file")
        sys.exit()

    domain_list=open(sys.argv[1]).readlines()
    host_dict={}
    for domain in domain_list:
        try:
            host_dict[domain]=socket.gethostbyname_ex(domain.strip())[2]
        except Exception as e:
            pass

    with open('hosts','w') as hosts:
        for domain in host_dict:
            for host in host_dict[domain]:
                hosts.write("{}\t{}\n".format(host,domain))

if __name__=='__main__':
    main()
    
