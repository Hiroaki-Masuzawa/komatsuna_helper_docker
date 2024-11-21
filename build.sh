DOCKER_IMAGE_TAG=komatsuna_helper
docker build . -t $DOCKER_IMAGE_TAG
if [ $? -eq 0 ]; then
    docker run -it --rm -u `id -u`:`id -g` \
    -v /etc/passwd:/etc/passwd:ro \
    -v /etc/group:/etc/group:ro \
    -v `pwd`/homedir:/home/`whoami` \
    -v `pwd`/catkin_ws:/catkin_ws \
    -w /catkin_ws \
    $DOCKER_IMAGE_TAG bash -c "catkin build"
fi