set -x 
docker run -it --rm \
-u `id -u`:`id -g` \
--net=host \
--env DISPLAY=$DISPLAY \
--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
-v /etc/passwd:/etc/passwd:ro \
-v /etc/group:/etc/group:ro \
-v `pwd`/homedir:/home/`whoami` \
-v `pwd`/catkin_ws:/catkin_ws \
-w /catkin_ws \
--name komatsuna_helper komatsuna_helper bash
