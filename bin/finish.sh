REPOSITORY='scikit-learn-sample'

IMAGE_ID=$(docker images ${REPOSITORY} --format='{{.ID}}')
if [ -n "$IMAGE_ID" ]; then
  docker rmi ${IMAGE_ID}
  echo 'Dockerイメージを削除しました！'
fi
