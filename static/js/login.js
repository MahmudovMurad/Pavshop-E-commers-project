const LoginLogic = {
    'url' : `${location.origin}/api/loginapi/`,

    fetchToken(email, password) {
        fetch(this.url, {
            method: 'POST',
            headers : {'Content-Type': 'application/json'},
            body : JSON.stringify({
                'email' : email,
                'password' : password,
            })
        }).then(response => response.json()).then(data => {
            console.log(data);
            if (data.access) {
                localStorage.setItem('token', data.access);
            }else {
                alert(data.message);
            }
        });
    }
}

const form = document.querySelector('#login_form');
const submit = document.getElementById('sbmt');



console.log(document.getElementById('login_form'))
document.getElementById('login_form').addEventListener('submit', (e) =>{
    e.preventDefault();
    const email = document.querySelector('#email').value;
    const password = document.querySelector('#password').value;
    console.log(email, password);
    LoginLogic.fetchToken(email, password);
})

    