 tcpdump -nn -i any -e port 80 
tcpdump: WARNING: any: That device doesn't support promiscuous mode
(Promiscuous mode not supported on the "any" device)
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
17:37:36.637688 lo    In  ifindex 1 00:00:00:00:00:00 ethertype IPv4 (0x0800), length 80: 127.0.0.1.60422 > 127.0.0.1.80: Flags [S], seq 3561555335, win 65495, options [mss 65495,sackOK,TS val 1699988454 ecr 0,nop,wscale 7], length 0
17:37:36.637697 lo    In  ifindex 1 00:00:00:00:00:00 ethertype IPv4 (0x0800), length 60: 127.0.0.1.80 > 127.0.0.1.60422: Flags [R.], seq 0, ack 3561555336, win 0, length 0
17:37:36.637743 lo    In  ifindex 1 00:00:00:00:00:00 ethertype IPv4 (0x0800), length 80: 127.0.0.1.60424 > 127.0.0.1.80: Flags [S], seq 2147983586, win 65495, options [mss 65495,sackOK,TS val 1699988454 ecr 0,nop,wscale 7], length 0
17:37:36.637746 lo    In  ifindex 1 00:00:00:00:00:00 ethertype IPv4 (0x0800), length 60: 127.0.0.1.80 > 127.0.0.1.60424: Flags [R.], seq 0, ack 2147983587, win 0, length 0
17:37:36.637895 lo    In  ifindex 1 00:00:00:00:00:00 ethertype IPv6 (0x86dd), length 100: ::1.36068 > ::1.80: Flags [S], seq 2692464002, win 65476, options [mss 65476,sackOK,TS val 280415538 ecr 0,nop,wscale 7], length 0
17:37:36.637903 lo    In  ifindex 1 00:00:00:00:00:00 ethertype IPv6 (0x86dd), length 80: ::1.80 > ::1.36068: Flags [R.], seq 0, ack 2692464003, win 0, length 0
17:37:36.637935 lo    In  ifindex 1 00:00:00:00:00:00 ethertype IPv6 (0x86dd), length 100: ::1.36076 > ::1.80: Flags [S], seq 4281671375, win 65476, options [mss 65476,sackOK,TS val 280415538 ecr 0,nop,wscale 7], length 0
17:37:36.637938 lo    In  ifindex 1 00:00:00:00:00:00 ethertype IPv6 (0x86dd), length 80: ::1.80 > ::1.36076: Flags [R.], seq 0, ack 4281671376, win 0, length 0
^C
8 packets captured
16 packets received by filter
0 packets dropped by kernel

