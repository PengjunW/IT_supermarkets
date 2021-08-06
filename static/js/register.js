new Vue({
	el: "#app",
	data: {
		username: "",
		user_err: "",
		passwd: "",
		passwd_err: "",
		confirm: "",
		confirm_err: "",
		email: "",
		email_err: "",
		isLoading: false
	},
	methods: {

		register: function() {
			var that = this;
			axios.post("/users/register/", {
					"username": this.username,
					"password": this.passwd,
					"confirm": this.confirm,
					"email": this.email
				})
				.then(function(response) {
						that.isLoading = true;
						that.$message({
							message: 'success',
							type: 'success'
						});
						setTimeout(function() {
							location.href = '/user/profile'
						}, 2000);
					},
					function(err) {
						console.log(err.response.data)
						that.user_err = err.response.data.username != null ? err.response.data.username.toString() : "";
						that.passwd_err = err.response.data.password != null ? err.response.data.password[0].toString() : "",
							that.passwd_err = err.response.data.non_field_errors != null ? err.response.data.non_field_errors[0].toString() :
							"",
							that.confirm_err = err.response.data.confirm != null ? err.response.data.confirm.toString() : "",
							that.email_err = err.response.data.email != null ? err.response.data.email.toString() : "";




					}
				)
		}
	}
})
