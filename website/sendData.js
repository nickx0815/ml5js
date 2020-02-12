function sendPoses() {
    if (poses.length != 0){
      var data = JSON.stringify(poses[0]['pose']);
      let socket = new WebSocket("ws://localhost:8000");
      socket.onopen = function(e) {
        socket.send(JSON.stringify(data))
      };
    }
}
function sendSound() {
    if (label.length != 0){
      var data = JSON.stringify(label)
      let socket = new WebSocket("ws://localhost:8010");
      socket.onopen = function(e) {
        socket.send(JSON.stringify(data))
      };
      var conf  = JSON.stringify(label[0]['confidence']*100)
      document.getElementById("soundLabel").innerHTML = "Sound detected: "+JSON.stringify(label[0]['label'])+" , Confidence: "+conf.substring(0,5)+" %"; // 6.7;
      console.log(label)
    }
}
var intervalPoses = 50;
var intervalSound = 200;
setInterval(sendPoses, intervalPoses);
setInterval(sendSound, intervalSound);