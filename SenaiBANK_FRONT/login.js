function tryToLogin()
{
    let username = document.getElementById("userName").value;
    let password = document.getElementById("password").value;
    
    if(username.trim() ==="") return;
    if(password.trim() ==="") return;

    let url = "http://localhost:5000/users/login"
    let request = {
        methor: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({"login":username, "password":password})

    };
    fetch(url,request)
    .then(response=>response.json())
    .then(data=>{
        if(data.error) return;

        if(data.jwt_token)
        {
            localStorage.setItem("jwt_token", data.jwt_token);
            window.location.href = "dashboard.html";
        }
    });
}