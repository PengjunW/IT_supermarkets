var vm = new Vue({
    el: "#order",
    data: {
        table: "",
        url1: 'https://img1.baidu.com/it/u=4068431406,2476608392&fm=253&fmt=auto&app=120&f=JPEG?w=640&h=432',
        url2: 'https://img2.baidu.com/it/u=1031375126,2665295960&fm=253&fmt=auto&app=120&f=JPG?w=640&h=377',
        url3:'https://img1.baidu.com/it/u=1676806351,1882478013&fm=26&fmt=auto&gp=0.jpg',
        url4:'https://img1.baidu.com/it/u=3717660014,1772191209&fm=26&fmt=auto&gp=0.jpg',
        url5:'https://img1.baidu.com/it/u=4068431406,2476608392&fm=253&fmt=auto&app=120&f=JPEG?w=640&h=432',
        url6: 'https://img0.baidu.com/it/u=546897615,3066788421&fm=15&fmt=auto&gp=0.jpg',
        num: 1
    },
    created: function () {
        this.getGoods();
    },
    methods: {
        getGoods: function () {
            var that = this;
            axios.get("/goods/lists", {
                headers: {
                    "Authorization": "jwt " + localStorage.getItem('jwt')
                }
            })
                .then(function (response) {
                    that.table = response.data.results;
                    //console.log(response.data.results);
                })
        },
		addShoppingCart: function(a) {
			var that = this;
			axios.post("/orders/shoppingCart/", {
					'nums':that.num,
					'goods':a.goods_id
				}, {
					headers: {
						"Authorization": "jwt " + localStorage.getItem('jwt')
					}
				})
				.then(function(response) {
				    console.log(this.table)
				    console.log("1231")
				    //console.log(item_number)
					//localStorage.setItem("Order", response.data.results.order_id);
					//localStorage.setItem("BikeId", that.rentbike);
					location.href = '/user/shoppingcart';


				})
		}
    }
})
