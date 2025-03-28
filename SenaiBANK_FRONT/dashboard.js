function carregarDados()
{
    let token = localStorage.getItem("jwt_token");
    if(!token)
    {
        window.location.href = "login.html";
        return;
    }
}