sudo kill -s 9 `ps -ef | grep 'python main.py' | grep -v grep | awk '{print $2}'`
