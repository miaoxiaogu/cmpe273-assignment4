# Result for Part I.
Implement Rendezvous hashing to shard the data.

```
python3 cache_client_hrw.py
Connecting to server at 127.0.0.1:4000
b'e621944d55b827774fa6f9813ddeacd9'
Connecting to server at 127.0.0.1:4002
b'4cc00164086b6002dcfe67b2e82d465f'
Connecting to server at 127.0.0.1:4003
b'8fa95b8382f3d190f3efc8ef2699eaa5'
Connecting to server at 127.0.0.1:4003
b'77086357f450285ec1afdcfd00741755'
Connecting to server at 127.0.0.1:4003
b'cc8c1505c8b33d7e6079ea43c5b767d6'
Connecting to server at 127.0.0.1:4000
b'e621944d55b827774fa6f9813ddeacd9'
Number of Users=6
Number of Users Cached=5
cc8c1505c8b33d7e6079ea43c5b767d6
Connecting to server at 127.0.0.1:4003
b'{"name": "Lisbeth Stacker", "email": "lstacker@gmail.com", "age": 24}'
8fa95b8382f3d190f3efc8ef2699eaa5
Connecting to server at 127.0.0.1:4003
b'{"name": "Irish Rackers", "email": "irackers@gmail.com", "age": 22}'
4cc00164086b6002dcfe67b2e82d465f
Connecting to server at 127.0.0.1:4002
b'{"name": "Bari Pushard", "email": "bpushard@gmail.com", "age": 21}'
77086357f450285ec1afdcfd00741755
Connecting to server at 127.0.0.1:4003
b'{"name": "Agueda Letsinger", "email": "aletsinger@gmail.com", "age": 23}'
e621944d55b827774fa6f9813ddeacd9
Connecting to server at 127.0.0.1:4000
b'{"name": "John Smith", "email": "jsmith@gmail.com", "age": 20}'
```
# Part II.
Implement consistent hashing to shard the data.
```
python3 cache_client_consistent.py
Connecting to server at 127.0.0.1:4002
b'e621944d55b827774fa6f9813ddeacd9'
Connecting to server at 127.0.0.1:4001
b'4cc00164086b6002dcfe67b2e82d465f'
Connecting to server at 127.0.0.1:4003
b'8fa95b8382f3d190f3efc8ef2699eaa5'
Connecting to server at 127.0.0.1:4001
b'77086357f450285ec1afdcfd00741755'
Connecting to server at 127.0.0.1:4003
b'cc8c1505c8b33d7e6079ea43c5b767d6'
Connecting to server at 127.0.0.1:4002
b'e621944d55b827774fa6f9813ddeacd9'
Number of Users=6
Number of Users Cached=5
77086357f450285ec1afdcfd00741755
Connecting to server at 127.0.0.1:4001
b'{"name": "Agueda Letsinger", "email": "aletsinger@gmail.com", "age": 23}'
8fa95b8382f3d190f3efc8ef2699eaa5
Connecting to server at 127.0.0.1:4003
b'{"name": "Irish Rackers", "email": "irackers@gmail.com", "age": 22}'
cc8c1505c8b33d7e6079ea43c5b767d6
Connecting to server at 127.0.0.1:4003
b'{"name": "Lisbeth Stacker", "email": "lstacker@gmail.com", "age": 24}'
4cc00164086b6002dcfe67b2e82d465f
Connecting to server at 127.0.0.1:4001
b'{"name": "Bari Pushard", "email": "bpushard@gmail.com", "age": 21}'
e621944d55b827774fa6f9813ddeacd9
Connecting to server at 127.0.0.1:4002
b'{"name": "John Smith", "email": "jsmith@gmail.com", "age": 20}'
```
