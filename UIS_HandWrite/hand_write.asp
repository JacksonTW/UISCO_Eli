<!DOCTYPE html>
<html lang="zh-TW">
<meta http-equiv="Content-Type" content="text/html; charset=big5" />
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<title>WorkFlow手寫簽名測試</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style type="text/css">
#canvas{  }
#canvasDiv{
	background-image:url(background.jpg);
	background-size:     cover;                     
    background-repeat:   no-repeat;
    background-position: center center;
}
</style>

</head>
<body id="bb">

<div id="canvasDiv" ></div>

<br>

<button id="btn_clear">清除</button>

<button id="btn_submit">提交</button>

<script language="javascript">


var canvasDiv = document.getElementById('canvasDiv');
var canvas = document.createElement('canvas');
var screenwidth = (window.innerWidth > 0) ? window.innerWidth : screen.width;

var canvasWidth = screenwidth;
var canvasHeight = 320;
document.addEventListener('touchmove', onDocumentTouchMove, false);
var point = {};
point.notFirst = false;
canvas.setAttribute('width', canvasWidth);
canvas.setAttribute('height', canvasHeight);
canvas.setAttribute('id', 'canvas');
canvasDiv.appendChild(canvas);
if (typeof G_vmlCanvasManager != 'undefined') {
    canvas = G_vmlCanvasManager.initElement(canvas);
}
var context = canvas.getContext("2d");
/*var ptrn = context.createPattern(img, 'no-repeat');
context.fillStyle = ptrn;
context.fillRect(0, 0, canvas.width, canvas.height);
*/
var img = new Image();
img.src = "Transparent.png";

img.onload = function() {
    var ptrn = context.createPattern(img, 'repeat');
    context.fillStyle = ptrn;
    context.fillRect(0, 0, canvas.width, canvas.height);
}
canvas.addEventListener("touchstart", function(e) {
	//console.log(e);
    var mouseX = e.touches[0].pageX - this.offsetLeft;
    var mouseY = e.touches[0].pageY - this.offsetTop;
    paint = true;
    addClick(e.touches[0].pageX - this.offsetLeft, e.touches[0].pageY - this.offsetTop);
	//console.log(e.touches[0].pageX - this.offsetLeft, e.touches[0].pageY - this.offsetTop);
    redraw();
});



canvas.addEventListener("touchend", function(e) {
	//console.log("touch end");
    paint = false;
});

canvas.addEventListener("touchmove", function(e) {
    if (paint) {
		//console.log("touchmove");
        addClick(e.touches[0].pageX - this.offsetLeft, e.touches[0].pageY - this.offsetTop, true);
		//console.log(e.touches[0].pageX - this.offsetLeft, e.touches[0].pageY - this.offsetTop);
        redraw();
    }

});

canvas.addEventListener("mousedown", function(e) {
    var mouseX = e.pageX - this.offsetLeft;
    var mouseY = e.pageY - this.offsetTop;
    paint = true;
    addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
    redraw();
});
canvas.addEventListener("mousemove", function(e) {
    if (paint) {
        addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
        redraw();
    }
});
canvas.addEventListener("mouseup", function(e) {
    paint = false;
});
canvas.addEventListener("mouseleave", function(e) {
    paint = false;
});
document.getElementById("btn_clear").addEventListener("click", function() {
    canvas.width = canvas.width;
});
document.getElementById("btn_submit").addEventListener("click", function() {
    $("#qmimg").attr("src", canvas.toDataURL("image/png"));
});


function onDocumentTouchStart(event) {
    if (event.touches.length == 1) {
        event.preventDefault();
        // Faking double click for touch devices
        var now = new Date().getTime();
        if (now - timeOfLastTouch < 250) {
            reset();
            return;
        }
        timeOfLastTouch = now;
        mouseX = event.touches[0].pageX;
        mouseY = event.touches[0].pageY;
        isMouseDown = true;

    }

}



function onDocumentTouchMove(event) {

    if (event.touches.length == 1) {
        event.preventDefault();
        mouseX = event.touches[0].pageX;
        mouseY = event.touches[0].pageY;
    }
}



function onDocumentTouchEnd(event) {
    if (event.touches.length == 0) {
        event.preventDefault();
        isMouseDown = false;
    }
}


var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var paint;

function addClick(x, y, dragging)
{
    clickX.push(x);
    clickY.push(y);
    clickDrag.push(dragging);
}



function redraw() {

    //canvas.width = canvas.width; // Clears the canvas
    // context.strokeStyle = "#df4b26";  //橘紅色
    context.strokeStyle = "########";    //全黑色
    context.lineJoin = "round";
    context.lineWidth = 5;             // /* 原本線為 2, 因簽名要清楚故改為5 */
    while (clickX.length > 0) {
        point.bx = point.x;
        point.by = point.y;
        point.x = clickX.pop();
        point.y = clickY.pop();
        point.drag = clickDrag.pop();
        context.beginPath();
        if (point.drag && point.notFirst) {
            context.moveTo(point.bx, point.by);
        } else {
            point.notFirst = true;
            context.moveTo(point.x - 1, point.y);
        }
        context.lineTo(point.x, point.y);
        context.closePath();
        context.stroke();
    }

    /*

      for(var i=0; i < clickX.length; i++)

      {		

        context.beginPath();

        if(clickDrag[i] && i){

          context.moveTo(clickX[i-1], clickY[i-1]);

         }else{

           context.moveTo(clickX[i]-1, clickY[i]);

         }

         context.lineTo(clickX[i], clickY[i]);

         context.closePath();

         context.stroke();

      }

      */

}
</script>

<img  id="qmimg"  />

</body>

</html>