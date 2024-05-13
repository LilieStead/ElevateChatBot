function botmsgerror (){
    var chatBox = document.getElementById('storemsg');
    var currenttime = new Date().toLocaleTimeString('en-GB', { hour12: false, hour: '2-digit', minute: '2-digit' });
    console.log(currenttime)
    chatBox.innerHTML += '<div class="message "><p> Im currently unavailable at the moment please try again later</p><span class="time">'+ currenttime +'</span></div>';
}

function chatstatus(){
    
    fetch("http://127.0.0.1:5000/status")
    .then(response => {
        if (response.ok) {
            var wellcomemsg = "Welcome to our chatbot! 🤖 Got questions? Don't hesitate to ask! We're here to help. Just a heads up: we save unresolved questions to learn and improve, but we don't collect personal data. Your privacy matters to us! So, fire away with your queries, and let's learn together!";
            if (!cookieExists){
                // error handling if the user by passes cookie popup 
                botmsg(wellcomemsg);
            }
            else if (!checkCookie('chatcookie')) {
                localStorage.removeItem("msgs");
                createCookie('chatcookie', 'Chatcookie', 10);
                botmsg(wellcomemsg)
            }
            else{
                loadmsgs()
            }
            return response.text();
        }
        throw new Error("Network response was not ok");
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        botmsgerror();
        console.error('There was a problem with your fetch operation:', error);
        const inputbox = document.getElementById("question");
        const sendbtn = document.getElementById("sendbtn");
        inputbox.disabled = true;
        sendbtn.disabled = true;
    });
}
