 ps aux | grep nginx 
27870 root      0:00 nginx: master process nginx -g daemon off;
27920 bird      0:00 nginx: worker process
27921 bird      0:00 nginx: worker process
43270 root      0:00 grep nginx
cl1k346lkgg86gm7thai-iseq:~# cat /proc/27870/root/etc/nginx/nginx.conf 
....
    include /etc/nginx/conf.d/*.conf;
}

strace -p 27870
strace: Process 27870 attached
rt_sigsuspend([], 8