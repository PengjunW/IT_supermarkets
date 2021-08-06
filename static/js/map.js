Vue.use(VueGoogleMaps, {
	load: {
		key: ''
	},
});
document.addEventListener('DOMContentLoaded', function() {
	new Vue({
		el: '#root',
		data: {
			center: {
				lat: 55.872473,
				lng: -4.289046
			},
			infoWindowPos: null,
			infoWinOpen: false,
			currentMidx: null,
			infoOptions: {
				content: '',
				pixelOffset: {
					width: 0,
					height: -100,
				}
			},
			markers: [{
				position: {
					lat: 55.872473,
					lng: -4.289046
				},
				infoText: '<strong>Marker 1</strong>'
			}],
			positions: ""
		},
		created: function() {
			var that = this;
			axios.get("/bikes/lists/")
				.then(function(response) {
					that.positions = response.data.results;
					console.log(response.data.results);
				})
		},
		methods: {
			toggleInfoWindow: function(marker, idx) {
				this.infoWindowPos = {
					'lat': marker.lat,
					'lng': marker.lng
				};
				var status = "repairing";
				var bikeid = idx + 1;
				if (marker.status == 1) {
					status = "free";
				} else if (marker.status == 2) {
					status = "using";
				} else if (marker.status == 3) {
					status = "unreparied"
				}
				this.infoOptions.content = '<b> bike_id: ' + idx + '</b><br><b> status: ' + status + '<br>';

				//check if its the same marker that was selected if yes toggle
				if (this.currentMidx == idx) {
					this.infoWinOpen = !this.infoWinOpen;
				}
				//if different marker set infowindow to open and reset current marker index
				else {
					this.infoWinOpen = true;
					this.currentMidx = idx;
				}
			}
		}
	});
});