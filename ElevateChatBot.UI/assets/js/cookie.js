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
    var Msgs = JSON.parse(localStorage.getItem('msgs')) || [];
    var Chatbox = document.getElementById('storemsg');
    Msgs.forEach(function(item){
        var type = item.type; // Assuming 'type' is a property of each message item
        var message = item.message; // Assuming 'message' is a property of each message item
        var time = item.time; // Assuming 'time' is a property of each message item
        Chatbox.innerHTML += '<div class="message '+ type +'"><p>' + message + '</p> <span class="time">'+ time +'</span></div>';
    });
}
