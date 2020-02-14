

function sendPose() {

    if (poses.length != 0 && sendPoses){
      var data = JSON.stringify(poses[0]['pose']);
      let socket = new WebSocket("ws://localhost:8000");
      socket.onopen = function(e) {
        socket.send(JSON.stringify(data))
      };
      document.getElementById("poseLabel").innerHTML = "PoseNet active"; // 6.7;
    }
    if (!sendPoses){
        document.getElementById("poseLabel").innerHTML = "PoseNet deactivated"; // 6.7;
    }
}
function sendSound() {
    //TODO Sprachsteuerung Start und Stop hier einbauen nicht beim request
    if (label.length > 0){

        if (label[0]['label']=="start" && label[0]['confidence']>0.9){
             console.log(typeof label[0]['confidence'])
            if (!document.getElementById("sendPosesid").checked){
                document.getElementById("sendPosesid").click()
                initPoseNet()
            }

        }
        if (label[0]['label']=="stop" && label[0]['confidence']>0.9){
             if (document.getElementById("sendPosesid").checked){
                document.getElementById("sendPosesid").click()
                 initPoseNet()
            }
        }
    }
    if (label.length > 0 && sendSounds){
      var data = JSON.stringify(label)
      let socket = new WebSocket("ws://localhost:8010");
      socket.onopen = function(e) {
        socket.send(JSON.stringify(data))
      };
      var conf  = JSON.stringify(label[0]['confidence']*100)
      document.getElementById("soundLabel").innerHTML = "Sound detected: "+JSON.stringify(label[0]['label'])+" , Confidence: "+conf.substring(0,5)+" %"; // 6.7;
    }
    if (!sendSounds){
        document.getElementById("soundLabel").innerHTML = "Sound Classifier deactivated"; // 6.7;
    }
}
var intervalPose = 50;
var intervalSound = 200;
setInterval(sendPose, intervalPose);
setInterval(sendSound, intervalSound);