import os
from os.path import exists, join, basename, splitext

git_repo_url = 'https://github.com/CMU-Perceptual-Computing-Lab/openpose.git'
project_name = splitext(basename(git_repo_url))[0]
if not exists(project_name):
  # see: https://github.com/CMU-Perceptual-Computing-Lab/openpose/issues/949
  # install new CMake becaue of CUDA10
  !wget -q https://cmake.org/files/v3.13/cmake-3.13.0-Linux-x86_64.tar.gz
  !tar xfz cmake-3.13.0-Linux-x86_64.tar.gz --strip-components=1 -C /usr/local
  # clone openpose
  !git clone -q --depth 1 $git_repo_url
  !sed -i 's/execute_process(COMMAND git checkout master WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}\/3rdparty\/caffe)/execute_process(COMMAND git checkout f019d0dfe86f49d1140961f8c7dec22130c83154 WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}\/3rdparty\/caffe)/g' openpose/CMakeLists.txt
  # install system dependencies
  !apt-get -qq install -y libatlas-base-dev libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler libgflags-dev libgoogle-glog-dev liblmdb-dev opencl-headers ocl-icd-opencl-dev libviennacl-dev
  # install python dependencies
  !pip install -q youtube-dl
  # build openpose
  !cd openpose && rm -rf build || true && mkdir build && cd build && cmake .. && make -j`nproc`
  
from IPython.display import YouTubeVideo

YOUTUBE_ID = 'RXABo9hm8B8'


YouTubeVideo(YOUTUBE_ID)

#!rm -rf youtube.mp4
# download the youtube with the given ID
!youtube-dl -f 'bestvideo[ext=mp4]' --output "youtube.%(ext)s" https://www.youtube.com/watch?v=$YOUTUBE_ID
# cut the first 5 seconds
!ffmpeg -y -loglevel info -i youtube.mp4 -t 5 video.mp4
# detect poses on the these 5 seconds
#!rm openpose.avi
!cd openpose && ./build/examples/openpose/openpose.bin --video ../video.mp4 --disable_blending --write_json ./output/ --display 0  --render_pose 0
# convert the result into MP4
#!ffmpeg -y -loglevel info -i openpose.avi output.mp4


# function to read and formatt the Json
# returns an array of data for X and a 1/0 for y
FRAMES = 100
def ReadJsons(folder_dir):

  # get all files in folder take first couple 
  # !!! problem !!!! how do we make sure that we get the files in order
  files = listdir(folder_dir)[:FRAMES]
  files.sort()
  for F in files:
    # load int a json into dict data
    f = open('data.json')
    data = json.load(f)
    
    
    
    
    
    
# train test split
X, y = shuffle(X, y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# train model    
regr = svm.SVR(kernel = 'rbf')
regr.fit(X_train, y_train)

# predict and accuracy
predY = regr.predict(X_test)
mean_absolute_error(y_test, predY)

# turning score into classification
a = []
for x in predY:
  if x >= .5:
    a.append(1)
    continue
  a.append(0)

isSick = np.array(a)
accuracy_score(y_test, isSick)






