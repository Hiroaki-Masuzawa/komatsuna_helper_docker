# Komatsuna_helper_docker
## 使い方
### リポジトリのクローン，および，docker imageのビルド
```
cd ~
git clone --recursive https://github.com/Hiroaki-Masuzawa/komatsuna_helper_docker.git
cd komatsuna_helper_docker
./build.sh
```
### 実行
```
cd komatsuna_helper_docker
./run.sh
```
```
roslaunch komatsuna_helper helper.launch
```
### point受信のサンプル実行
```
cd komatsuna_helper_docker
./exec.sh
```
```
source /catkin_ws/devel/setup.bash
rosrun komatsuna_helper sub_point_sample
```