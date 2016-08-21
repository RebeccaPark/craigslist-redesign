var num_star=0;
var c_num_star = document.getElementById("num-star");
var starredPostClassName = document.querySelector(".starred-post")

function setOnclick(stars, i) {
	var star = stars[i];
	var baseClassName = "fa keyword-light-purple";
	star.onclick = function() {
		if (star.className.indexOf("fa-star-o") == -1) {
			star.className = baseClassName + " fa-star-o";
			num_star--;
			display_num_star(num_star);
		} else {
			star.className = baseClassName + " fa-star";
			num_star++;
			display_num_star(num_star);
		}
	};
}

function display_num_star(num_star) {
	if(num_star == 0) {
		starredPostClassName.className = "btn btn-white starred-post hidden";
	} else {
		starredPostClassName.className = "btn btn-white starred-post";
		c_num_star.innerText = num_star;
	}
}

var stars = document.querySelectorAll(".keyword-light-purple");
for (var i = 0; i < stars.length; i++) {
	setOnclick(stars, i);
}

var buttons = document.querySelectorAll(".fa-close");
var rows = document.querySelectorAll(".posting-row");
for (var i = 0; i < buttons.length; i++) {
	setOnClickHideRow (buttons, rows, i);
}

function setOnClickHideRow (buttons, rows, i) {
	var button = buttons[i];
	var row = rows[i];
	button.onclick = function() {
		row.className = "posting-row row hidden";
		console.log("here");
	}
}

var user = document.querySelector(".user");
if (user == null) {
} else {
	user.onclick = function () {
		document.querySelector(".user-drop-down").className = "user-drop-down";
	}
}

var user_drop = document.querySelector(".user-drop-down");
document.querySelector(".drop-down-user").onclick = function () {
	user_drop.className = "user-drop-down hidden";
	user.className = "fa fa-user user";
}
