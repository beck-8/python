#!/usr/bin/env bash
#
# author:wangyancun
# python-version:3.8.1
# Wget's link is a private network disk link, please replace the official website link if it fails!
#
printf "\e[1;34m Install python ... please wait! \e[0m\n"
yum -y groupinstall "Development tools" &>/dev/null
if [ $? -ne 0 ];then
	printf "\e[1;31m Development tools install failed! \e[0m\n"
	exit
fi
yum install -y zlib-devel bzip2-devel openssl-devel sqlite-devel readline-devel libffi-devel wget &>/dev/null
if [ $? -ne 0 ];then
        printf "\e[1;31m The environment install failed! \e[0m\n"
        exit
fi
wget https://service-npqwyu2u-1258401831.ap-hongkong.apigateway.myqcloud.com/release/ceshi/%E5%AD%A6%E4%B9%A0/%E5%8D%83%E9%94%8B%E9%A1%B9%E7%9B%AE%E5%8C%85/Python-3.8.1.tar.xz &>/dev/null
if [ $? -ne 0 ];then
        printf "\e[1;31m The source code package is download failed! \e[0m\n"
        exit
fi
tar xf Python-3.8.1.tar.xz -C /opt/
cd /opt/Python-3.8.1/
sed -i '164s/^#//' Modules/Setup
sed -i '210,213s/^#//' Modules/Setup
./congigure --enable-shared &>/dev/null
make -j $(lscpu |awk 'NR==4{print $2}') &>/dev/null
make install &>/dev/null
echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib" >/etc/profile.d/python3_lib.sh
echo "/usr/local/lib" >/etc/ld.so.conf.d/python3.conf
source /etc/profile
ldcondig
printf "\e[1;32m Install python is completed! \e[0m\n"
