
json_dir = "Jsons/"
NUM_FRAMES = 100 # number of frames we take from the vid
videoList = [] # list of videos
videoList.sort()



# for each video what person is the one we look at
POI = []


# flips
def fixData(coordsListX, coordsListY):
  xMax = coordsListX[0]
  xMin = coordsListX[0]
  yMax = coordsListY[0]
  yMin = coordsListY[0]
  for x in coordsListX:
    xMax = max(xMax, x)
    xMin = min(xMin, x)
  for y in coordsListY:
    yMax = max(yMax, y)
    yMin = min(yMin, y)
  
  if xMax - xMin > yMax - yMin:
    return coordsListY, coordsListX # flip the two
  else:
    return coordsListX, coordsListY
  


# takes in the keypoint you want and returns the index in the json file for the ccodinate pair
def getIndex(keyPoint):
  return (keyPoint - 1) * 3


# takes in a json file name
# reads it
# fixes what needs fixing
# outputs a array with its relevent info
# videoIndex = int that says what vid it is (needed for POI)
# jsonFile = string name of the json file
def formatJsonData(videoIndex, jsonFile):
  dataDictionary = json.load(open(jsonFile, 'r')) # The dictionary with the data in it
  dataList = dataDictionary['people'][POI[videoIndex]]['pose_keypoints_2d']
  coordsListX = []
  coordsListY = []
  Kpoint = []
  for i in range(25):
    x = getIndex(i)
    y = x + 1
    coordsListX.append(dataList[x])
    coordsListY.append(dataList[y])
  
  X, Y fixData(coordsListX, coordsListY)
  Kpoints.append(np.array(X))
  Kpoints.append(np.array(Y))
  
  
  return Kpoints
  
  
  
# takes in list of json indecies and then processes those into a 2d array A[frames][info]
# videoIndex = int that says what vid it is (needed for POI)
# jsonStartingPos = at what json in the full list does the vid start (refer to loopVids() to understand)
def proccessVideo(videoIndex, jsonStartingPos):
  jsonFileList = FOLDER[jsonStartingPos : jsonStartingPos + NUM_FRAMES]
  Frames_data = []
  for jsonFile in jsonFileList:
    Kpoints = np.array(formatJsonData(videoIndex, jsonFile))
    Frames_data.append(Kpoints)
  
  return Frames_data

# takes in name of folder of jsons (for all vids)
# returns a 4d data[vid][frames][key_point][x/y (0,1)] (4th dimension is either x or y)
def loopVids():
  
  
  videoList = [] # list of video names

  data = [] # is the final 4d array 
  
  # open folder
  # DRIVE MUST ALREADY BE MOUNTED
  FOLDER = glob.glob("/content/drive/My Drive/PDAFolder/T9_Shared_Drive_2022/Json_List/*.json") # the path will be different per person
  FOLDER.sort()

  
  # Now, iterate through the videos
  for i in range(len(videoList)):
    video = videoList[i]
    # PATH WILL BE DIFFERENT - make sure you change it, also should change Json_list
    startIndex = FOLDER.index("/content/drive/My Drive/PDAFolder/T9_Shared_Drive_2022/Json_List/" + video + "_000000000000" + "_keypoints.json")
    vid_data = np.array(processVideo(i, startIndex))
    data.append(vid_data)
  


  

# loop throguh all jsons in a video
  
  # need to get a list of jsons
  # sort them and find first indexis ( ake a list of those)
  # for each video we take first 100 frames
  # have to fix data for those frames
  # Shove them in an arrays
