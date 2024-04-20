// Function to check if a cookie exists
function checkCookie(chatcookie) {
    console.log("cookie lookedup");
    // Split cookies by semicolon and trim any leading or trailing whitespace
    var cookies = document.cookie.split(';').map(cookie => cookie.trim());
    // Loop through the cookies array
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        // If the cookie name matches, return true
        if (cookie.indexOf(chatcookie + '=') === 0) {
            return true;
        }
    }
    // If the cookie doesn't exist, return false
    return false;
}

// Function to create a new cookie with an expiration time of 10 minutes
function createCookie(chatcookie, cookieValue, minutesToExpire) {
    console.log("cookie made");
    var expirationDate = new Date();
    expirationDate.setTime(expirationDate.getTime() + (minutesToExpire * 60 * 1000)); // Convert minutes to milliseconds
    var expires = "expires=" + expirationDate.toUTCString();
    document.cookie = chatcookie + "=" + cookieValue + ";" + expires + ";path=/";
}



function loadmsgs() {
    const loaduser = JSON.parse(localStorage.getItem("usermsgs")) || [];
    const loadbot = JSON.parse(localStorage.getItem("botmsgs")) || [];

    const loadmsgs = [];
    for (let i = 0; i < Math.max(loaduser.length, loadbot.length); i++) {
        if (loaduser[i]) loadmsgs.push({ message: loaduser[i].message, type: 'message message-personal', timestamp: loaduser[i].time });
        if (loadbot[i]) loadmsgs.push({ message: loadbot[i].message, type: 'message', timestamp: loadbot[i].time });
    }

    const chatBox = document.getElementById('storemsg');
    chatBox.innerHTML = loadmsgs.map(msg => {
        return `<div class="${msg.type}"><p>${msg.message}</p><span class="time">${msg.timestamp}</span></div>`;
    }).join("");
}