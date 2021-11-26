const removeProductLogic = {
    url : `${location.origin}/api/basket_item_delete/`,

    removeProduct(itemId){
        console.log(itemId);
        return fetch(`${this.url}`,{
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'itemId': itemId
            })


    })

}
}


let removeProduct = document.querySelector('.remove_product')
    removeProduct.onclick = function() {
        alert('Your product deleted')
        window.location.reload(true)
        const itemId = this.getAttribute('data');
        removeProductLogic.removeProduct(itemId);
     
    }  
