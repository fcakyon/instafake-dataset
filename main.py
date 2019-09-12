import json
import pandas as pd

#%% Import automated/nonautomated data
with open("Data/automatedAccountData.json") as json_file:
    automatedAccountData = json.load(json_file)
with open("Data/nonautomatedAccountData.json") as json_file:
    nonautomatedAccountData = json.load(json_file)
    
#%% Import fake/real data
with open("Data/fakeAccountData.json") as json_file:
    fakeAccountData = json.load(json_file)
with open("Data/realAccountData.json") as json_file:
    realAccountData = json.load(json_file)
    
#%% Create automated/nonautomated dataframe
def CreateDataFrame1(accountDataList):
    dataFrame = pd.DataFrame({})
    
    for accountData in accountDataList:
        userFollowerCount = accountData["userFollowerCount"]
        userFollowingCount = accountData["userFollowingCount"]
        followerFollowingRatio = userFollowerCount/max(1,userFollowingCount)
        
        tempDataFrame = pd.Series({"userMediaCount":accountData["userMediaCount"],
                                      "userFollowerCount":accountData["userFollowerCount"],
                                      "userFollowingCount":accountData["userFollowingCount"],
                                      "userHasHighlighReels":accountData["userHasHighlighReels"],
                                      "userHasExternalUrl":accountData["userHasExternalUrl"],
                                      "userTagsCount":accountData["userTagsCount"],
                                      "followerFollowingRatio":followerFollowingRatio,
                                      "userBiographyLength":accountData["userBiographyLength"],
                                      "usernameLength":accountData["usernameLength"],
                                      "usernameDigitCount":accountData["usernameDigitCount"],
                                      "automatedBehaviour":accountData["userFollowingCount"],
                                    })
        dataFrame = dataFrame.append(tempDataFrame, ignore_index=True)
    
    return dataFrame

automatedDataFrame = CreateDataFrame1(automatedAccountData)
nonautomatedDataFrame = CreateDataFrame1(nonautomatedAccountData)
    
#%% Create fake/real dataframe
def CreateDataFrame2(accountDataList):
    dataFrame = pd.DataFrame({})
    
    for accountData in accountDataList:
        userFollowerCount = accountData["userFollowerCount"]
        userFollowingCount = accountData["userFollowingCount"]
        followerFollowingRatio = userFollowerCount/max(1,userFollowingCount)
        
        tempDataFrame = pd.Series({"userMediaCount":accountData["userMediaCount"],
                                  "userFollowerCount":accountData["userFollowerCount"],
                                  "userFollowingCount":accountData["userFollowingCount"],
                                  "userHasProfilPic":accountData["userHasProfilPic"],
                                  "userIsPrivate":accountData["userIsPrivate"],
                                  "followerFollowingRatio":followerFollowingRatio,
                                  "userBiographyLength":accountData["userBiographyLength"],
                                  "usernameLength":accountData["usernameLength"],
                                  "usernameDigitCount":accountData["usernameDigitCount"],
                                  "isFake":accountData["isFake"],
                                    })
        dataFrame = dataFrame.append(tempDataFrame, ignore_index=True)
    
    return dataFrame

fakeDataFrame = CreateDataFrame2(fakeAccountData)
realDataFrame = CreateDataFrame2(realAccountData)
dataFrame = pd.concat([fakeDataFrame,realDataFrame])

#%% Visualize fake/real dataframe
import seaborn as sns
import matplotlib.pyplot as plt

g = sns.stripplot( x="isFake", y='userMediaCount', data=dataFrame,jitter = True)
g.set(ylim=(-10, 1010))
plt.xlabel("User Is Fake")
plt.ylabel("Number of User Media")

g = sns.stripplot( x="isFake", y='userFollowerCount', data=dataFrame,jitter = True)
g.set(ylim=(-10, 1010))
plt.xlabel("User Is Fake")
plt.ylabel("Number of User Follower")

automatedDataFrame['userHasHighlighReels'].value_counts()
nonautomatedDataFrame['userHasHighlighReels'].value_counts()