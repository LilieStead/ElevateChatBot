
function cookieExists (CookieName){
    var allCookies = document.cookie.split(";");
    for (var i = 0; i < allCookies.length; i++){
        var cookie = allCookies[i].trim();
        if (cookie.indexOf(CookieName + '=') === 0){
            return true
        }
    }
    return false
}


function consentCookieCreate (cookieName){
    var day = new Date();
    day.setTime(day.getTime() + (365 * 24 * 60 * 60 * 1000));
    var expires = "expires=" + day.toUTCString();
    document.cookie = cookieName + "=" + "accepted" + ";" + expires + ";path=/";
}
// consentCookieCreate(cookiename);

function cookieconsent() {
    var cookiename = "consentCookie"; // Added 'var' to define the variable locally
    if (!cookieExists(cookiename)) {
        var popup = document.getElementById('custom-popup');
        popup.style.display = 'flex';
        var cookiebtn = document.getElementById('close-popup');
        cookiebtn.addEventListener('click', function() { // Added comma after 'click'
            consentCookieCreate(cookiename); // Fixed variable name
            location.reload();
        });
    } else {
        chatstatus()
        return;
    }
}

cookieconsent();