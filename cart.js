var cart = {
    basket: [],
    products: [
        {
            id: 1,
            name: 'Товар 1',
            price: 1000,
            quantity: 1,
        },
        {
            id: 2,
            name: 'Товар 2',
            price: 2000,
            quantity: 1,
        },
        {
            id: 3,
            name: 'Товар 3',
            price: 3000,
            quantity: 2,
        },
    ],
    priceTotal: 0,
    quantity: 0,
    add: function(){
        var basket = this.basket;
        var products = this.products;
        var i;
        var answer = cart.showCatalog();


        for(i = 0; i < products.length; i++){

            if(answer == products[i].id || answer === products[i].name){
                basket.push(products[i]);
                this.priceTotal += products[i].price;
                this.quantity++;
                alert('Добавлен товар: \n' + cart.products[i].name + ' - ' + cart.products[i].price + ' руб.' + '\n\n' + 'Ваша корзина: \n' + 'Кол-во - ' + this.quantity + '\n' + 'Общая стоимость - ' + this.priceTotal + ' руб');
                break;
            }
            else if(answer == null){
                break;
            }
        }

        var message = confirm('Продолжить покупки?');

        if(message == true){
            this.add();
        }
        else{
            alert('Ваша корзина: \n' + 'Кол-во - ' + this.quantity + '\n' + 'Общая стоимость - ' + this.priceTotal + ' руб');
            this.showCart();
        }

        return basket;
    },
    delete: function(){
        var deleteBaslek = confirm("Очистить корзину?");

        if(deleteBaslek == true){
            this.basket.length = 0;
            alert("Корзина очищена");
        }

        return this.basket;
    },
    amount: function(){
        var basket = this.basket;

        if(this.priceTotal == 0){
            for(var i = 0; i < basket.length; i++){
                this.priceTotal += basket[i].price;
                console.log(i);
            }
        }

        return this.priceTotal;
    },
    showCatalog: function(){
        var output = '';
        for(var i = 0; i < cart.products.length; i++){
            output += (i + 1) + ') ' + cart.products[i].name + ' - ' + cart.products[i].price + ' руб.' + '\n';
        }
        return prompt(output);
    },
    showCart: function(){
        var $cart = document.getElementById('cart');
        $cart.style.position = 'absolute';

        if(this.quantity > 0){
            $cart.innerHTML = 'В корзине: ' + this.quantity + ' товар(ов)' + ' на сумму: ' + this.priceTotal + ' руб.';
        }
        else{
            $cart.innerHTML = 'Ваша корзина пуста';
        }

    },
    showCalalogPage: function(){
        var $catalog = document.getElementById('catalog');

        var $product = document.createElement('div');
        $product.className = 'products';


        for(var i = 0; i < this.products.length; i++){
            var $item = document.createElement('div');
            $item.className = 'item';
            $item.style.border = '1px solid black';
            $item.innerHTML = this.products[i].name + '' + this.products[i].brand + '' + this.products[i].price;
            $product.appendChild($item);
        }

        $catalog.appendChild($product);
    }
};

cart.add();