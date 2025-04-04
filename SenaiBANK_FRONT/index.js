function tentarAutorizar()
{
    let token = localStorage.getItem("jwt_token");
    if(!token)
    {
        window.location.href = "login.html"
        return;
    }

    let url = "http://localhost:5000/users/authorize";

    let request = {
        method: "GET",
        Headers: {"Authorization":token}
    };

    fetch(url,request).then(response => response.json()).then(data=>{
        if (data.erro)
        {
            localStorage.removeItem("jwt_token");
            window.location.href = "login.html";
        }
        if (data.status)
        {
            if(data.status === "sucess")
            {
                window.location.href = "dashboard.html";
            }
        }
    })
    .catch(error => {
        localStorage.removeItem("jwt_token");
        window.location.href = "login.html";
    });
}

function logout()
{
    localStorage.removeItem("jwt_token");
    window.location.href = "login.html";
    return;
}