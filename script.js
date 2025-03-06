async function fetchTweets() {
    const tweetsList = document.getElementById('tweets');
    const loadingDiv = document.getElementById('loading');

    tweetsList.innerHTML = "";
    loadingDiv.classList.remove('hidden');

    try {
        const response = await fetch('http://127.0.0.1:5000/fetch-tweets');  // Backend API for scraping
        const tweets = await response.json();

        loadingDiv.classList.add('hidden');

        for (let tweet of tweets) {
            const sentiment = await analyzeSentiment(tweet.text);
            const tweetItem = document.createElement('li');
            tweetItem.classList.add('tweet', sentiment);
            tweetItem.textContent = `${tweet.text} - (${sentiment})`;
            tweetsList.appendChild(tweetItem);
        }
    } catch (error) {
        loadingDiv.classList.add('hidden');
        alert("Error fetching tweets.");
    }
}

async function analyzeSentiment(text) {
    try {
        const response = await fetch('http://127.0.0.1:5000/analyze', { // Backend API for sentiment analysis
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        const data = await response.json();
        return data.sentiment.toLowerCase();
    } catch (error) {
        return "neutral";
    }
}
