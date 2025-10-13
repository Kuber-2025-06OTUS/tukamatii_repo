kubectl debug node/cl1k346lkgg86gm7thai-iseq -it --image=busybox --target=host
tail /host/var/log/pods/homework_myapp_aca9efaa-aa15-400e-8481-6823ba319349/myapp/0.log 
2025-10-13T17:55:23.56154476Z stdout F 2025-10-13T17:55:23+0000 DEBUG This is a debug log that shows a log that can be ignored.
2025-10-13T17:55:25.057539445Z stdout F 2025-10-13T17:55:25+0000 DEBUG This is a debug log that shows a log that can be ignored.
2025-10-13T17:55:25.477570183Z stdout F 2025-10-13T17:55:25+0000 INFO This is less important than debug log and is often used to provide context in the current task.
2025-10-13T17:55:29.827716741Z stdout F 2025-10-13T17:55:29+0000 INFO This is less important than debug log and is often used to provide context in the current task.
2025-10-13T17:55:31.354799031Z stdout F 2025-10-13T17:55:31+0000 DEBUG This is a debug log that shows a log that can be ignored.
2025-10-13T17:55:35.286871005Z stdout F 2025-10-13T17:55:35+0000 INFO This is less important than debug log and is often used to provide context in the current task.
2025-10-13T17:55:37.909526029Z stdout F 2025-10-13T17:55:37+0000 WARN A warning that should be ignored is usually at this level and should be actionable.
2025-10-13T17:55:39.000162431Z stdout F 2025-10-13T17:55:38+0000 WARN A warning that should be ignored is usually at this level and should be actionable.
2025-10-13T17:55:43.006023379Z stdout F 2025-10-13T17:55:43+0000 DEBUG This is a debug log that shows a log that can be ignored.
2025-10-13T17:55:44.933894354Z stdout F 2025-10-13T17:55:44+0000 INFO This is less important than debug log and is often used to provide context in the current task.