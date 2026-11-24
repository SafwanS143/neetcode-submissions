import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.counter = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId), ...]
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        for user in self.followMap[userId] | {userId}:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                timestamp, tweet = self.tweets[user][index]
                heapq.heappush(heap, (-timestamp, tweet, index, user))

        while heap and len(feed) < 10:
            _, tweet, index, user = heapq.heappop(heap)
            feed.append(tweet)
            if index > 0:
                index -= 1
                timestamp, tweet = self.tweets[user][index]
                heapq.heappush(heap, (-timestamp, tweet, index, user))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)