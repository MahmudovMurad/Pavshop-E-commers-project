let subscriberForm = document.getElementById("mc-embedded-subscribe-form");
subscriberForm.addEventListener('submit', function (e) {
    e.preventDefault();
    let postData = {
        "email": subscriberForm.email.value
    }

    console.log(postData);
    let res = fetch('/subscribe/' ,{
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": subscriberForm.csrfmiddlewaretoken.value,
            'Authorization': `Bearer ${localStorage.getItem('token')}`

        },
        body: JSON.stringify(postData),
    })
        .then(function(response) {
            console.log('here')
            if(response.ok){
                alert('You are subscribe');
            }else {
                return response.json().then(text => {

                    alert(text.email.join(','));
                    
                })
            }
        return response.json();
        })
})