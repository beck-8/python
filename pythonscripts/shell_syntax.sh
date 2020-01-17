#!/usr/bin/env bash
#
# usage: syntax

for i in {1..10};do
  {
    echo ${i}
  }&
done


while true;do
  {
    echo "hello"
  }&
done


if [ ! -f /etc/hosts ];then
  echo "/etc/hosts not exists"
else
  echo "/etc/hosts exists"
fi


read -p "please input: " variable
case ${variable} in
  1)
    echo "1"
    ;;
  2)
    echo "2"
    ;;
  *)
    echo "error"
    ;;
esac

