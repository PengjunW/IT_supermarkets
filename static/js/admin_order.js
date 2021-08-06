new Vue({
 el: "#app",
 data: {
  table: ""
 },
 mounted: function() {
  this.getOrder();
 },
 methods: {
         getOrder: function () {
            var that = this;
            axios.get("/orders/manage/", {
                headers: {
                    "Authorization": "jwt " + localStorage.getItem('jwt')
                }
            })
                .then(function (response) {
                    that.table = response.data.results;
                    console.log(response.data.results);
                })
        }
    }
})