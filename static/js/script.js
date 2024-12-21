document.getElementById("ask-cheese-button").addEventListener("click", function() {
    // Clear the question input field
    document.getElementById("question").value = '';

    // Add the shake class to the cheese ball
    document.getElementById("cheese-ball").classList.add("shake");

    // Define the cheesy responses
    const responses = [
        "Yes, definitely gouda!",
        "No, absolutely not.",
        "Maybe... but brie says no.",
        "Yes, but only with extra cheese.",
        "Ask again with more cheddar!",
        "Possibly parmesan...",
        "The cheese ball is unsure.",
        "Cheese says: why not?"
    ];

    // Randomly select a response
    const randomResponse = responses[Math.floor(Math.random() * responses.length)];

    // Display the response
    document.getElementById("answer").innerText = randomResponse;

    // Remove the shake class after the animation ends
    setTimeout(function() {
        document.getElementById("cheese-ball").classList.remove("shake");
    }, 500);  // Matches the animation duration
});
