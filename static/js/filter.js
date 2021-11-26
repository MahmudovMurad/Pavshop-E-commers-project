const FilterLogic = {
    url: `${location.origin}/api/product/`,
    filterProduct(category_id, brand_id) {
        let url = this.url;
        if (category_id) {
            url += `?category_id=${category_id}`;
        }
        if (brand_id) {
            url += `?brand_id=${brand_id}`;
        }
        
        
        fetch(url, {
            method : 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
            

        })
        .then(res => res.json()).then(data => {
            
            document.querySelector('.product-field').innerHTML = ""
            console.log(data);
            for (let i in data){
                if (data[i]['category']==category_id){
                    console.log(data[i]['category']);
                    document.querySelector('.product-field').innerHTML += `
                    <form  method="post">
                    <div class="col-md-4">
                    <div class="item"> 
                  <!-- Item img -->
                  <div class="item-img"> <img class="img-1" src="${data[i]["cover_image"]}" >
                    <!-- Overlay -->
                    <div class="overlay">
                      <div class="position-center-center">
                        <div class="inn"><a href="${data[i]["cover_image"]}" data-lighter><i class="icon-magnifier"></i></a> <i class="icon-basket add_basket"  data ="${data[i]["id"]}" > </i> </div>
                      </div>
                    </div>
                  </div>
                  
                  <div class="item-name"> <a href="#.">${data[i]["name"]}</a>
                    <p>${data[i]["designer"]}</p>
                  </div>
                  <!-- Price --> 
                  <span class="price"><del style="color:#FFE115;"><small></small>${data[i]["price"]}</del></span>
                 </div>
                 </div>
                 </form>

                    `
                    
                }
                if (data[i]['brand']==brand_id){
                    console.log(data[i]['brand']);
                    
                    document.querySelector('.product-field').innerHTML += `
                    <form  method="post">
                    <div class="col-md-4">
                    <div class="item"> 
                  <!-- Item img -->
                  <div class="item-img"> <img class="img-1" src="${data[i]["cover_image"]}" >
                    <!-- Overlay -->
                    <div class="overlay">
                      <div class="position-center-center">
                        <div class="inn"><a href="${data[i]["cover_image"]}" data-lighter><i class="icon-magnifier"></i></a> <i class="icon-basket add_basket"  data ="${data[i]["id"]}" > </i> </div>
                      </div>
                    </div>
                  </div>
                  
                  <div class="item-name"> <a href="#.">${data[i]["name"]}</a>
                    <p>${data[i]["designer"]}</p>
                  </div>
                  <!-- Price --> 
                  <span class="price"><del style="color:#FFE115;"><small></small>${data[i]["price"]}</del></span>
                 </div>
                 </div>
                 </form>

                    `
                    
                }

                
            }
        })
    }
    
}





let filter = document.getElementsByClassName('category-field');
for (let i = 0; i < filter.length; i++) {
    filter[i].onclick = function () {
        const category_id = this.getAttribute('data');
        FilterLogic.filterProduct(category_id);
    }
}

let filter2 = document.getElementsByClassName('brand-field');
for (let i = 0; i < filter2.length; i++) {
    filter2[i].onclick = function () {
        const brand_id = this.getAttribute('data');
        FilterLogic.filterProduct(brand_id);
    }
}