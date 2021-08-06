var vm = new Vue({
    el: "#order",
    data: {
        table: ""
    },
    created: function () {
        this.getOrder();
    },
    methods: {
        getOrder: function () {
            var that = this;
            axios.get("/orders/orders", {
                headers: {
                    "Authorization": "jwt " + localStorage.getItem('jwt')
                }
            })
                .then(function (response) {
                    that.table = response.data.results;
                    console.log(response.data.results);
                })
        },
        payed: function (order) {
            var that = this;
            console.log(order)
            axios.put("/operations/pay/" + order.id + "/", {}, {
                headers: {
                    "Authorization": "jwt " + localStorage.getItem('jwt')
                }
            })
                .then(function (response) {
                    that.getOrder();
                    console.log(response)
                    if(response.results.order_status == 1){

                          that.table.order_status = 1;
                          //location.href = '/user/productlist';
                    }
                    else if(response.results.order_status == 2){

                          that.table.order_status = 2;
                          //location.href = '/user/balance';
                    }
                })
        }
    }
})
