
function closechat(){
    var open = document.getElementById("chatbotJ");
    var close = document.getElementById("chatbotbuttonJ");
    open.classList.add('disabled');
    close.classList.remove('disabled');
    void open.offsetWidth;
}

function openchat(){
    var open = document.getElementById("chatbotJ");
    var close = document.getElementById("chatbotbuttonJ");
    open.classList.remove('disabled');
    close.classList.add('disabled');
    void open.offsetWidth;
    scrollbottom();
}


