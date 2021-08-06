$(document).ready(function(){
	let pathname = location.pathname;
	if (localStorage.getItem('jwt') === null) {
		if (pathname != '/' && pathname != '/login.html') {
			localStorage.setItem("path",pathname);
			location.href = "/"
		}
	}
});



