REPOSITORY='scikit-learn-sample'

IMAGE_ID=$(docker image ls -q ${REPOSITORY})
# イメージがまだ存在しなければイメージを作成
if [ -z "$IMAGE_ID" ]; then
  # Imageを作成
  docker build ./ -t ${REPOSITORY}
  IMAGE_ID=$(docker image ls -q ${REPOSITORY})
fi

# コンテナを起動 & コンテナの中に入る
PWD=$(pwd)
WORKDIR='/app'
docker run --rm -v ${PWD}:${WORKDIR} -it ${IMAGE_ID} /bin/bash
