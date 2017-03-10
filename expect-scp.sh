echo "Enter system IP: "
read ip
echo "Enter system password: "
read  -s pass

out=$(expect -c "spawn scp -r /home/rr.sh root@$ip:/home/
expect \"root@$ip's password:\"
send \"$pass\r\"
expect \"*\"
interact
")

echo $out


out=$(expect -c "spawn scp -r /home/rr.sh root@$ip:/home/
expect \"root@$ip's password:\"
send \"$pass\r\"
expect \"*\"
interact
")

echo $out
