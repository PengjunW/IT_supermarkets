new Vue({
	el: "#app",
	data: {
		newPw: "",
		oldPw: ""
	},
	methods: {

		changePw: function() {
			var that = this;
			axios.put("/users/update/", {
					"password": this.newPw,
			"confirm": this.oldPw
				}, {
					headers: {
						"Authorization": "jwt " + localStorage.getItem('jwt')
					}
				})
				.then(function(response) {
						alert('change success!');
						that.newPw = "";
						that.oldPw = "";
					},
					function(err) {
						alert("change failed")
					})
		}
	}
})
