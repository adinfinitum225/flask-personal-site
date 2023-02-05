function dropdown(button) {
	var x = document.getElementById("navbar");
	if (x.className === "clicked"){
		x.className = "";
		// Javascript needs Unicode characters to be referred to as follows
		button.textContent = button.textContent.replace('\u25B2', '\u25BC');
	} else {
		x.className = "clicked";
		button.textContent = button.textContent.replace('\u25BC', '\u25B2');
	}
}
