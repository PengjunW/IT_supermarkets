new Vue({
	el: "#app",
	data: {
		id: "",
		option: "1"
	},
	methods: {
		reportB: function() {
			var that = this;
			this.id = ""
        this.$message({
          message: 'Input success!',
          type: 'success'
        });
		}
	}
})
