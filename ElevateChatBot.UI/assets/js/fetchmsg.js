function usermsg (msg){
    var chatBox = document.getElementById('storemsg');
    var currenttime = new Date().toLocaleTimeString('en-GB', { hour12: false, hour: '2-digit', minute: '2-digit' });
    var userMsg = { message: msg, time: currenttime };
    var userMsgs = JSON.parse(localStorage.getItem('usermsgs')) || [];
    userMsgs.push(userMsg);
    localStorage.setItem('usermsgs', JSON.stringify(userMsgs));
    chatBox.innerHTML += '<div class="message message-personal"><p>' + msg + '</p> <span class="time">'+ currenttime +'</span></div>';

}

function botmsg (data){
    var chatBox = document.getElementById('storemsg');
    var currenttime = new Date().toLocaleTimeString('en-GB', { hour12: false, hour: '2-digit', minute: '2-digit' });
    var botMsg = {message: data, time: currenttime };
    var botMsgs = JSON.parse(localStorage.getItem('botmsgs')) || [];
    botMsgs.push(botMsg);
    localStorage.setItem('botmsgs', JSON.stringify(botMsgs))
    chatBox.innerHTML += '<div class="message"><p>' + data.answer + '</p><span class="time">'+ currenttime +'</span></div>';
}


function sendmsg(event){
    event.preventDefault();
    console.log("dshjash")
    var message = document.getElementById("question").value; // Retrieve the value of the input field
    if (!message){ // Check if message is empty
        return;
    } else {
        try {
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
                usermsg(message);
                return response.json();
            })
            .then(data => {
                // Handle response data here
                console.log(data)
                document.getElementById("question").value = "";
                botmsg(data);
            })
            .catch(error => {
                console.error('Error sending message:', error);
                botmsgerror ();
            });
        } catch (error) {
            console.error('Error sending message:', error);
            botmsgerror ();
        }
    }
}

document.getElementById('sendmsgform').addEventListener('submit', sendmsg);
