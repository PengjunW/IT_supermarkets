new Vue({
	el: "#app",
	data: {
		userName: "",
		passWd: "",
		isLoading: false,
	},
	methods: {
		login: function() {
			var that = this;
			axios.post("/users/login/", {
					"username": that.userName,
					"password": that.passWd
				})
				.then(function(response) {
					if (response.data.msg == "fail") {
						that.$message.error(response.data.results.info.non_field_errors.toString());
					} else {
							that.isLoading = true;
							that.$message({
								message: 'success',
								type: 'success'
							});
							localStorage.setItem('superuser', response.data.results.is_superuser);
							localStorage.setItem('jwt', response.data.results.token);
							localStorage.setItem('username', response.data.results.username);
							setTimeout(function() {
								location.href = '/admin/visual'
							}, 2000);
					}
				})
		}
	}
})
