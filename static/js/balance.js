var vm = new Vue({
	el: "#app",
	data: {
		balances: 1,
		balance: ""
	},
	created: function() {
		var that = this;
		axios.get("/operations/account/", {
				headers: {
					"Authorization": "jwt " + localStorage.getItem('jwt')
				}
			})
			.then(function(response) {
				that.balances = response.data.account_balance
			})
	},
	methods: {
		addBlance: function() {
			var that = this;
			axios.put("/operations/account/", {
					"account_balance": that.balance
				}, {
					headers: {
						"Authorization": "jwt " + localStorage.getItem('jwt')
					}
				})
				.then(function(response) {
					that.balances = response.data.account_balance
				})
		}
	}
})
