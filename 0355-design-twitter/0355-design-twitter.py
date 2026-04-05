class Twitter:

    def __init__(self):
        self.time = 0
        self.userFollows = {}
        self.userTweets = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.userTweets: self.userTweets[userId].append([self.time, tweetId, userId])
        else: self.userTweets[userId] = [[self.time, tweetId, userId]]
        self.time = self.time - 1


    def getNewsFeed(self, userId: int) -> List[int]:
        validIds = [userId]
        if userId in self.userFollows:
            validIds.extend(self.userFollows[userId])
        validTweets = []
        for userid in validIds:
            validTweets.extend(self.userTweets.get(userid, []))
        heapq.heapify(validTweets)
        res = heapq.nsmallest(10, validTweets)
        tweetsArr = []
        for tweet in res:
            tweetsArr.append(tweet[1])
        return tweetsArr     

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollows and followeeId not in self.userFollows[followerId]:
            self.userFollows[followerId].append(followeeId)
        else:
            self.userFollows[followerId] = [followeeId]
        print(self.userFollows, "follow")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollows and followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)
        print(self.userFollows, "unfollow")





