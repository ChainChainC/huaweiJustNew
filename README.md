# huaweiJustNew

## requirement
`python = 3.7.3`
`numpy = 1.19.4`

## QA
Q：已经输出了控制指令，为什么我的机器人一直不动？

A：大多数情况下是选手没有在输出 OK 之后 flush 标准输出，导致数据留存在缓冲区，没有
真正送给判题器。对于 C/C++，可以使用 fflush(stdout)或 cout << flush，对于 java,可以使用
System.out.flush()，对于 python，可以使用 sys.stdout.flush()