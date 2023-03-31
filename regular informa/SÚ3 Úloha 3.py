with open('SÚ3 ramce.txt') as ramce:
    ramce = tuple(r.split() for r in ramce.readlines())

with open('UDP_ramce.txt', 'w+') as udp, open('TCP_ramce.txt', 'w+') as tcp:
    tcpList, udpList = [], []

    for r in ramce:
        match r[0]:
            case 'UDP':
                udpList.append(' '.join(r) + '\n')
            case'TCP':
                tcpList.append(' '.join(r) + '\n')

    tcp.write(f'Pocet TCP ramcov je: {len(tcpList)}\n{"".join(tcpList)}')
    udp.write(f'Pocet UDP ramcov je: {len(udpList)}\n{"".join(udpList)}')