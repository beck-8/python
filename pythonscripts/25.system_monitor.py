# psutil: 监控系统的CPU, memory, disk, network, process
# 第三方模块: 别人写的模块, 发布到了 pypi.org上面; 通过pip命令安装第三方模块;
import psutil


# cpu monitor functions
# 求机器的逻辑核心是
cpus = psutil.cpu_count(logical=True)
print("cpu逻辑核心数为: {}".format(cpus))

# 总体占用时间
cpu_info = psutil.cpu_times()
print(cpu_info)

# 每个CPU分别占用时间
cpu_info = psutil.cpu_times(percpu=True)
print(cpu_info)

# 求CPU在规定时段内, 运行所占用的时间百分比
cpu_rate = psutil.cpu_percent(interval=5, percpu=False)
print("cpu在5秒内所占用的百分比: {}".format(cpu_rate))

cpu_rate = psutil.cpu_percent(interval=5, percpu=True)
print("cpu在5秒内分别所占用的百分比: {}".format(cpu_rate))

# cpu时间占比情况
cpu_rate = psutil.cpu_times_percent(interval=5, percpu=True)
print("cpu总体时间占比情况: {}".format(cpu_rate))

# 查看CPU的状态
cpu_stat = psutil.cpu_stats()
print(cpu_stat)

# 求得CPU的频率
cpu_freq = psutil.cpu_freq()
print(cpu_freq)


# memory monitor functions
memory_info = psutil.virtual_memory()
print(memory_info)
print(memory_info.percent)

swap_info = psutil.swap_memory()
print(swap_info.percent)

# disk monitor functions
disk_partition = psutil.disk_partitions()
print(disk_partition[0].device)

disk_usage = psutil.disk_usage(psutil.disk_partitions()[0].mountpoint)
print(disk_usage)

diskIO = psutil.disk_io_counters()
print(diskIO)

# network monitor functions
network_info = psutil.net_io_counters()
print(network_info)

# process monitor functions
if 18981 in psutil.pids():
    process = psutil.Process(1)
    print(process.name())  # 获取进程名字
    print(process.exe())  # 获取进程执行路径
    print(process.status())  # 获取进程状态
    # print(process.num_threads())  # 获取进程开启的线程数
    print(process.create_time())  # 获取进程创建时间
    print(process.cpu_times())  # 获取user、system 两个 CPU 时间
    print(process.memory_percent())  # 获取进程内存利用率
    print(process.memory_info())  # 获取进程内存rss、vms信息
    # print(process.io_counters())  # 进程IO信息,包括读写IO数及字节数
