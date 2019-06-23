var slider = document.getElementById("myRange");
var output = document.getElementById("sentiment-val");
var negative = document.getElementsByClassName("Negative");
var positive = document.getElementsByClassName("Positive");
var neutral = document.getElementsByClassName("Neutral");
output.innerHTML = "Neutral";

slider.oninput = function() {
  if(this.value==1){
		output.innerHTML = "Negative";
		for (var i=0;i<neutral.length;i+=1){
		neutral[i].style.display = 'none';
		}
		for (var i=0;i<negative.length;i+=1){
			negative[i].style.display = 'block';
		}
		for (var i=0;i<positive.length;i+=1){
			positive[i].style.display = 'none';
		}
	}
	else if(this.value==2){
		output.innerHTML = "Neutral";
		for (var i=0;i<neutral.length;i+=1){
		neutral[i].style.display = 'block';
		}
		for (var i=0;i<negative.length;i+=1){
			negative[i].style.display = 'none';
		}
		for (var i=0;i<positive.length;i+=1){
			positive[i].style.display = 'none';
		}
	}
	else{
		output.innerHTML = "Positive";
		for (var i=0;i<neutral.length;i+=1){
		neutral[i].style.display = 'none';
		}
		for (var i=0;i<negative.length;i+=1){
			negative[i].style.display = 'none';
		}
		for (var i=0;i<positive.length;i+=1){
			positive[i].style.display = 'block';
		}
	}
}

var tw_post = document.getElementsByClassName("twitter-post");
var bg_post = document.getElementsByClassName("blog-post");

function all_click(){
	for (var i=0;i<tw_post.length;i+=1){
		tw_post[i].style.display = 'block';
	}
	for (var i=0;i<bg_post.length;i+=1){
		bg_post[i].style.display = 'block';
	}
}

// function fb_click(){
// 	for (var i=0;i<fb_post.length;i+=1){
// 		fb_post[i].style.display = 'block';
// 	}
// 	for (var i=0;i<tw_post.length;i+=1){
// 		tw_post[i].style.display = 'none';
// 	}
// 	for (var i=0;i<bg_post.length;i+=1){
// 		bg_post[i].style.display = 'none';
// 	}
// }

function tw_click(){
	for (var i=0;i<tw_post.length;i+=1){
		tw_post[i].style.display = 'block';
	}
	for (var i=0;i<bg_post.length;i+=1){
		bg_post[i].style.display = 'none';
	}
}

function bg_click(){
	for (var i=0;i<tw_post.length;i+=1){
		tw_post[i].style.display = 'none';
	}
	for (var i=0;i<bg_post.length;i+=1){
		bg_post[i].style.display = 'block';
	}
}

frame1 = document.getElementById("pie_frame1");
frame2 = document.getElementById("pie_frame2");

function mumbaiChange(){
		frame1.src="mumbai_bjp";
		frame2.src="mumbai_ncp"
}

function delhiChange(){
		frame1.src="delhi_bjp";
		frame2.src="delhi_ncp"
}

function kolkataChange(){
		frame1.src="kolkata_bjp";
		frame2.src="kolkata_ncp"
}

function bengaluruChange(){
		frame1.src="bengaluru_bjp";
		frame2.src="bengaluru_ncp";
}

function hyderabadChange(){
		frame1.src="hyderabad_bjp";
		frame2.src="hyderabad_ncp"
}