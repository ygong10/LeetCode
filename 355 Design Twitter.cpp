typedef tuple<int, int, int> III;

struct MyCompare {
  bool operator() (const III& lhs, const III& rhs) const
  {
      return get<2>(lhs) > get<2>(rhs);      
  }
};

class Twitter {
public:
    /** Initialize your data structure here. */
    unordered_map<int, set<III, MyCompare>> _userTweets;
    unordered_map<int, vector<int>> _usersFollowees;
    int _time;
    Twitter() {
        _time = 0;
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        if (_userTweets.find(userId) == _userTweets.end()){
            set<III, MyCompare> newList;
            _userTweets.insert({userId, newList});
        }
        _userTweets[userId].insert(make_tuple(userId, tweetId, _time)); // insert tweet inside userId's tweets
        for (auto it = _usersFollowees.begin(); it != _usersFollowees.end(); it++){
            auto follower = it->first;
            if (find(it->second.begin(), it->second.end(), userId) != it->second.end()){
                _userTweets[follower].insert(make_tuple(userId, tweetId, _time));
            }
        }
        _time++;       
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        vector<int> result;
        auto it  = _userTweets[userId].begin();
        int counter = 0;
        while (it != _userTweets[userId].end()){
            if (counter == 10){
                return result;
            }
            result.push_back(get<1>(*it));
            it++;
            counter++;
        }
        return result;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */ // followeeId doesn't have to post to exist
    // add flowee to follower's list <follower, followee>
    void follow(int followerId, int followeeId) {
        if (followerId == followeeId){ // can't follow yourself
            return;
        }
        if (_usersFollowees.find(followerId) == _usersFollowees.end()){
            vector<int> newList;
            _usersFollowees.insert({followerId, newList}); // insert a empty vector
        }
        _usersFollowees[followerId].push_back(followeeId); // adds follower to followees
        // add followee's tweets to follower's feed now
        auto tweets = _userTweets.find(followeeId);
        if (tweets != _userTweets.end()){
            for (auto it = tweets->second.begin(); it != tweets->second.end(); it++){ // iterate through a set
                if (get<0>(*it) == followeeId){
                    _userTweets[followerId].insert(*it);
                }
            }
        }

    }

    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId){
            return;
        }
        auto it  = _usersFollowees[followerId].begin();
        while (it != _usersFollowees[followerId].end()){ // remove followees from follower's list
            if (*it == followeeId){
                _usersFollowees[followerId].erase(it);
                break;
            }
            it++;
        }
        // remove followee's tweets from newfeed
        auto it2 = _userTweets[followerId].begin();
        while (it2 != _userTweets[followerId].end()){
            if (get<0>(*it2) == followeeId){
                _userTweets[followerId].erase(it2);
            }
            it2++;
        }
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * vector<int> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */