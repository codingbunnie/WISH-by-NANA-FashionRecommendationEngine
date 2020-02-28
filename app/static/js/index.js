

var file = document.getElementById("image");

try {
	file.onchange = function(){

		console.log("Hi")
		if(file.files.length > 0)
		{
		  document.getElementById('file-name').innerHTML = file.files[0].name;
		}
	};
 }
 catch (e) {
	//Handle the error if you wish.
 }


//  let json_data = {'data-uri': data_uri }
	
// $.ajax({
// 	type: 'POST',
// 	url: '/webcam_upload',
// 	contentType: 'application/json; charset=utf-8',
// 	dataType: 'json',
// 	data: JSON.stringify(json_data),
// 	success: function(data) {
// 	console.log(data);
// 	main_dom = document.getElementById("results-prediction");
// 	var image_dom = "";
// 	// full_path = "http://127.0.0.1:5001/" +data.full;
// 	// image_dom += '<img src="'+full_path+'?'+new Date().getTime()+'">';
		
// 	for(let i = 0; i < data.crop.length; i++){

// 		let link = data.crop[i];

// 		image_dom += '<img src="'+link+'?'+new Date().getTime()+'">';
// 	}

// var camera_dom = document.getElementById("my-camera");

// if (camera_dom != null){
// 	CAPTURE_IMG_WIDTH = 640;
// 	CAPTURE_IMG_HEIGHT = 480;	
	
// 	jQuery.ajaxSetup({
// 	  beforeSend: function() {
// 		 $('#loading').removeClass('hidden');
// 	  },
// 	  complete: function(){
// 		 $('#loading').addClass('hidden');
// 	  },
// 	  success: function() {
// 		$('#loading').addClass('hidden');
// 	  }
// 	});
	
	// // HTML5 WEBCAM
	// Webcam.set({
	//   width: CAPTURE_IMG_WIDTH,
	//   height: CAPTURE_IMG_HEIGHT,
	//   image_format: 'jpeg',
	//   jpeg_quality: 90
	// });
	// Webcam.attach( '#my-camera' );
	
	
	// let form_capture = document.getElementById('form-capture-image')
	// $('.btn-capture-image').on('click', function(e) {
	//   e.preventDefault();
	
	//   Webcam.snap(function(data_uri) {
	// 	// display results in page
	// 	// readURL(data_uri, '#input-data-uri')
	// 	let json_data = {'data-uri': data_uri }
	
	// 	$.ajax({
	// 	  type: 'POST',
	// 	  url: '/webcam_upload',
	// 	  contentType: 'application/json; charset=utf-8',
	// 	  dataType: 'json',
	// 	  data: JSON.stringify(json_data),
	// 	  success: function(data) {
	// 		console.log(data);
	// 		main_dom = document.getElementById("results-prediction");
	// 		var image_dom = "";
	// 		// full_path = "http://127.0.0.1:5001/" +data.full;
	// 		// image_dom += '<img src="'+full_path+'?'+new Date().getTime()+'">';
			
	// 		for(let i = 0; i < data.crop.length; i++){
	
	// 			let link = data.crop[i];
	
	// 			image_dom += '<img src="'+link+'?'+new Date().getTime()+'">';
	// 		}
	// 		console.log(image_dom);
	// 		main_dom.innerHTML=image_dom;
	// 		var c = document.getElementById("my-canvas");
	// 		var ctx = c.getContext("2d");
	// 		ctx.clearRect(0, 0, c.width, c.height);
	// 		for(let i = 0; i < data.details.length; i++){
	// 			let positions = data.details[i];
	// 			ctx.beginPath();
	// 			ctx.strokeStyle = "pink";
	// 			ctx.rect(positions[0], positions[1], positions[2], positions[3]);
	// 			ctx.stroke();
	// 		}

			// html = '<ul>'
			// for( let i = 0; i < data['probs'].length; i++) {
			//   data_splitted = data['probs'][i]
	
			//   html += '<li><span class="num">' + data_splitted[0] + '</span> <span class="prob">'+ data_splitted[1] + '</span></li>'
			// }
			// html += '</ul>'
	
			// $('#probs').text('').append(html)
			// $('#class-result').text('Predictions: ' + data['label']);
	
			// $('.box-main').css('height', $('.box-results').height());
// 		  }
// 		});
// 	  });
// 	});
// }


// var predict_interval = setInterval(function () {document.getElementsByClassName("btn-capture-image")[0].click();}, 3000);

// var stop_button = document.getElementsByClassName("btn-capture-stop")[0];

// stop_button.addEventListener("click", stop_capture);

// function stop_capture(){
// 	clearInterval(predict_interval);
// }

// (function() {
// 	var canvas = document.querySelector("#canvas");
// 	var context = canvas.getContext("2d");
// 	canvas.width = 400;
// 	canvas.height = 400;

// 	var Mouse = {x:0, y:0};
// 	var lastMouse = {x:0, y:0};
// 	context.fillStyle = "white";
// 	context.fillRect(0, 0, canvas.width, canvas.height);
// 	context.color = "black";
// 	context.lineWidth = 8;
//     context.lineJoin = context.lineCap = 'round';
	
// 	debug();

// 	canvas.addEventListener("mousemove", function(e) {
// 		lastMouse.x = Mouse.x;
// 		lastMouse.y = Mouse.y;

// 		Mouse.x = e.pageX - this.offsetLeft;
//         Mouse.y = e.pageY - this.offsetTop;
// 	}, false);

// 	canvas.addEventListener("mousedown", function(e) {
// 		canvas.addEventListener("mousemove", onPaint, false);
// 	}, false);

// 	canvas.addEventListener("mouseup", function() {
// 		canvas.removeEventListener("mousemove", onPaint, false);
// 	}, false);

// 	var onPaint = function() {	
// 		context.lineWidth = context.lineWidth;
// 		context.lineJoin = "round";
// 		context.lineCap = "round";
// 		context.strokeStyle = context.color;
	
// 		context.beginPath();
// 		context.moveTo(lastMouse.x, lastMouse.y);
// 		context.lineTo(Mouse.x,Mouse.y );
// 		context.closePath();
// 		context.stroke();
// 	};

// 	function debug() {
// 		$("#clearButton").on("click", function() {
// 			context.clearRect( 0, 0, 280, 280 );
// 			context.fillStyle="white";
// 			context.fillRect(0,0,canvas.width,canvas.height);
// 		});
// 	}
// }());