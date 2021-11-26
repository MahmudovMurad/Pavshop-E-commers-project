window.addEventListener("load", async function () {
    let response = await fetch(
        `${location.origin}/api/card/`, {
        method: "GET",
        headers: {
            'Content-Type': "application/json",
            "Authorization": `Bearer ${localStorage.getItem("token")}`
        },
    });

    let responseData = await response.json();
    let basket = document.querySelector(".basket-ul");
    let total = 0
    basket.innerHTML = "";
    if (responseData) {
        for (i of responseData) {
            console.log(i);
            basket.innerHTML += `
            <li>
                        <div class="media-left">
                          <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${i['product']['cover_image']}" alt="..."> </a> </div>
                        </div>
                        <div class="media-body">
                          <h6 class="media-heading">${i['product']['name']}</h6>
                          <span class="price">${i['product']['price']} USD</span> <span class="qty">QTY: ${i['quantity']}</span> </div>
            </li>
             
            `
        }
        
    }


})

const BasketLogic = {
    url: `${location.origin}/api/card/`,

    addProduct(productId, quantity) {
        console.log(localStorage.getItem('token'))
        console.log(productId, quantity)
        return fetch(`${this.url}`, {

            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',

                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product_id': productId,
                'quantity': quantity
            })

        })
            .then(response => response.json()).then(data => {
                console.log(data)

                let basket = document.querySelector(".basket-ul");
                basket.innerHTML = "";
                for (i of data) {
                    basket.innerHTML += `
            <li>
                        <div class="media-left">
                          <div class="cart-img"> <a href="#"> <img class="media-object img-responsive" src="${i['product']['cover_image']}" alt="..."> </a> </div>
                        </div>
                        <div class="media-body">
                          <h6 class="media-heading">${i['product']['name']}</h6>
                          <span class="price">${i['product']['price']} USD</span> <span class="qty">QTY: ${i['quantity']}</span> </div>
            </li>
            
            `
                }
       

            });
    }
}

let AddToBasket = document.getElementsByClassName('add_basket')
for (let i = 0; i < AddToBasket.length; i++) {
    console.log(AddToBasket[i])
    AddToBasket[i].onclick = function () {
        const productId = this.getAttribute('data');
        const quantity = 1;
        BasketLogic.addProduct(productId, quantity);

    }
}


let AddTooBasket = document.getElementsByClassName('add_to_basket')
for (let i = 0; i < AddTooBasket.length; i++) {
    console.log(AddTooBasket[i])
    AddTooBasket[i].onclick = function () {
        let productId = this.getAttribute('data');
        let quantity = parseInt(document.querySelector('.btn-default').getAttribute('title'));
        BasketLogic.addProduct(productId, quantity);
    }
}







