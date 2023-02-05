function dropdown() {
	var x = document.getElementById("navbar");
	if (x.className === "clicked"){
		x.className = "";
	} else {
		x.className = "clicked";
	}
}
