var sendpose = true;
var sendsound = true;

function sendPose() {

    if (poses.length != 0 && sendPoses) {
        console.log(poses[0]['pose'])
        var data = JSON.stringify(poses[0]['pose']);
        let socket = new WebSocket("ws://localhost:8000");
        socket.onopen = function (e) {
            socket.send(JSON.stringify(data))
            console.log("send")
        };
        document.getElementById("poseLabel").innerHTML = "PoseNet active"; // 6.7;
        sendpose = true;
    }
    if (!sendPoses && sendpose) {
        let socket = new WebSocket("ws://localhost:8000");
        socket.onopen = function (e) {
            socket.send("false")
        };
        document.getElementById("poseLabel").innerHTML = "PoseNet deactivated"; // 6.7;
        sendpose = false;
    }
}

function sendSound() {
    if (label.length > 0) {

        if (label[0]['label'] == "start" && label[0]['confidence'] > 0.9) {
            if (!document.getElementById("sendPosesid").checked) {
                document.getElementById("sendPosesid").click()
                initPoseNet()
                sendpose = true;
            }

        } else if (label[0]['label'] == "stop" && label[0]['confidence'] > 0.9) {
            if (document.getElementById("sendPosesid").checked) {
                document.getElementById("sendPosesid").click()
                initPoseNet()
                if (sendpose) {
                    let socket = new WebSocket("ws://localhost:8000");
                    socket.onopen = function (e) {
                        socket.send("false")
                    };
                    document.getElementById("poseLabel").innerHTML = "PoseNet deactivated"; // 6.7;
                    sendpose = false;
                }
            }
        } else if (label[0]['label'] == "close" && label[0]['confidence'] > 0.9) {
            if (document.getElementById("sendPosesid").checked) {
                document.getElementById("sendPosesid").click()
                initPoseNet()
            }

        }
    }
    if (label.length > 0 && sendSounds) {
        if (label[0]['confidence'] > 0.9) {
            console.log("YOH")
            var data = JSON.stringify(label)
            let socket = new WebSocket("ws://localhost:8010");
            socket.onopen = function (e) {
                socket.send(JSON.stringify(data))
            };
            var conf = JSON.stringify(label[0]['confidence'] * 100)
            document.getElementById("soundLabel").innerHTML = "Sound detected: " + JSON.stringify(label[0]['label']) + " , Confidence: " + conf.substring(0, 5) + " %"; // 6.7;
        }
        sendsound = true;
    }
    if (!sendSounds && sendsound) {
        let socket = new WebSocket("ws://localhost:8010");
        socket.onopen = function (e) {
            socket.send("false")
        };

        document.getElementById("soundLabel").innerHTML = "Sound Classifier deactivated"; // 6.7;
        sendsound = false;
    }
}








var intervalPose = 50;
var intervalSound = 200;
setInterval(sendPose, intervalPose);
setInterval(sendSound, intervalSound);