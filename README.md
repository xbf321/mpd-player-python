# MDP Client Player 

Python 包装 mpc 方式，使用 HTTP 协议控制 MPD。

初版。

### 播放

http://127.0.0.1:7170/play

### 暂停

http://127.0.0.1:7170/pause

## 开发

```sh

python -m venv .venv
. .venv/bin/activate
.venv/bin/pip install Flask

flask run --debug --port 7170
```

## 上线

通过 Docker 部署。

```
docker run -d -e MPD_HOST=192.168.100.1 -e MPD_PORT=7160 -p 7170:7170 --name mpd-player-py xbf321/mpd-player-py
```

## mac

```sh
mpc play
mpc pause
mpc repeat on
mpc volume 80
```

## Other
```sh
docker build -t xbf321/mpd-player-py .

docker run -it --rm -e MPD_HOST=192.168.100.1 -e MPD_PORT=7160 -p 7170:7170 mpd-player-py /bin/bash

```
