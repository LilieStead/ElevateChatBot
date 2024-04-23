function usermsg(msg) {
    var chatBox = document.getElementById('storemsg');
    var currenttime = new Date().toLocaleTimeString('en-GB', { hour12: false, hour: '2-digit', minute: '2-digit' });
    var Msg = { message: msg, time: currenttime, type: "message-personal" };
    var Msgs = JSON.parse(localStorage.getItem('msgs')) || [];
    Msgs.push(Msg);
    localStorage.setItem('msgs', JSON.stringify(Msgs));
    // Update chatBox with the new message
    chatBox.innerHTML += '<div class="message message-personal"><p>' + msg + '</p> <span class="time">'+ currenttime +'</span></div>';

}

function botmsg(msg) {
    var chatBox = document.getElementById('storemsg');
    var currenttime = new Date().toLocaleTimeString('en-GB', { hour12: false, hour: '2-digit', minute: '2-digit' });
    var Msg = { message: msg, time: currenttime, type: "message-bot" };
    var Msgs = JSON.parse(localStorage.getItem('msgs')) || [];
    Msgs.push(Msg);
    localStorage.setItem('msgs', JSON.stringify(Msgs));
    // Update chatBox with the new message
    chatBox.innerHTML += '<div class="message message-bot"><p>' + msg + '</p><span class="time">'+ currenttime +'</span></div>';
}

function typing(){
    var chatBot = document.getElementById("storemsg");
    chatBot.innerHTML += '<div class="message message-bot" id="typing" ><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>';
}

function removetyping(){
    var typingmsg = document.getElementById("typing");
    if (typingmsg) {
        // Remove the div and all its child elements
        typingmsg.parentNode.removeChild(typingmsg);
    }
}

function scrollbottom(){
    var chatBox = document.getElementById('chat');
    chatBox.scrollTop = chatBox.scrollHeight;
}


function sendmsg(event){
    event.preventDefault();
    var message = document.getElementById("question").value; // Retrieve the value of the input field
    if (!message){ // Check if message is empty
        return;
    } else {
        usermsg(message);
        try {
            typing();
            fetch("http://127.0.0.1:5000/prediction", {
                method: 'POST',
                body: JSON.stringify({message}),
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json'
                },
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Handle response data here
                console.log(data)
                document.getElementById("question").value = "";
                
                botmsg(data.answer);
            })
            .catch(error => {
                console.error('Error sending message:', error);
                botmsgerror ();
            })
            .finally(() => {
                scrollbottom();
                removetyping()
            });

        } catch (error) {
            console.error('Error sending message:', error);
            removetyping();
            botmsgerror ();
            scrollbottom();

        }
    }
}

document.getElementById('sendmsgform').addEventListener('submit', sendmsg);
