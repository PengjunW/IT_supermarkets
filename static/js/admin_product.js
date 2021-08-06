new Vue({
 el: "#app",
 data: {
  table: ""
 },
 mounted: function() {
  this.getGoods();
 },
 methods: {
          getBike: function() {
           var that = this;
           axios.get("/goods/lists/")
            .then(function(response) {
             console.log(response.data.results);
             that.table = response.data.results;
            })
          },
  getGoods: function () {
            var that = this;
            axios.get("/goods/lists/", {
                headers: {
                    "Authorization": "jwt " + localStorage.getItem('jwt')
                }
            })
                .then(function (response) {
                    that.table = response.data.results;
                    console.log(response.data.results);
                })
        },
  submit: function(id, lat, lng) {
   axios.patch("/bikes/update/" + id + "/", {
     'lat': lat,
     'lng': lng
    }, {
     headers: {
      "Authorization": "jwt " + localStorage.getItem('jwt')
     }
    })
    .then(function(response) {
     console.log(response.data.results);
     that.table = response.data.results;
    })
  }
 }
})