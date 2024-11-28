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
これで以下のプログラムが起動する．
1. カメラの位置とステージの位置をTFで出力するプログラム
1. 上記プログラムのキャリブレーション時に使用するARマーカー検出プログラム
1. 画面を出力し，クリック位置の3次元座標をトピック名`clicked_position`に出力するプログラム
1. ステージ位置とロボット位置をTFで出力するプログラム


### point受信のサンプル実行
```
cd komatsuna_helper_docker
./exec.sh
```
```
source /catkin_ws/devel/setup.bash
rosrun komatsuna_helper sub_point_sample
```

### openmaipulatorシミュレータの実行
- terminal1 (Simulator)
    ```
    cd komatsuna_helper_docker
    ./run.sh
    ```
    ```
    source devel/setup.bash
    roslaunch open_manipulator_gazebo open_manipulator_gazebo.launch
    ```
- terminal2 (Robot controller)
    ```
    cd komatsuna_helper_docker
    ./exec.sh
    ```
    ```
    source devel/setup.bash
    roslaunch open_manipulator_controller open_manipulator_controller.launch use_platform:=false
    ```
- terminal3 (Rviz)
    ```
    cd komatsuna_helper_docker
    ./exec.sh
    ```
    ```
    source devel/setup.bash
    roslaunch komatsuna_helper open_manipulator_rviz.launch
    ```
- terminal4 (GUI)
    ```
    cd komatsuna_helper_docker
    ./exec.sh
    ```
    ```
    source devel/setup.bash
    roslaunch open_manipulator_control_gui open_manipulator_control_gui.launch 
    ```
