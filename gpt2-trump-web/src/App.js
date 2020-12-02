import React from "react";
import FakeTweet from "fake-tweet";
import "fake-tweet/build/index.css";
import KT from './KT.png';

function App() {
  const config = {
    user: {
      nickname: "KT",
      name: "Katie Partington",
      avatar: KT,
      verified: true,
      locked: false
    },
    display: "default",
    text: "@akshaytree Fat cake",
    image: "",
    date: "3:47 PM · Dec 1, 2020",
    app: "Twitter for iPad",
    retweets: 32000,
    quotedTweets: 100,
    likes: 12700
  };
  return (
    <div className="App">
      <FakeTweet config={config} />
    </div>
  );
}

export default App;