let soundModel = 'https://teachablemachine.withgoogle.com/models/SK49Tmvw/';
let video;
let poseNet;
let poses = [];
let label = [];
let classifier;
var sendSounds
var sendPoses

function setup() {
    frameRate(24);
    createCanvas(640, 480);
    classifier = ml5.soundClassifier(soundModel + 'model.json');
    classifier.classify(gotResult);
    video = createCapture(VIDEO);
    video.size(width, height);
    sendSounds = document.getElementById("sendPosesid").checked
    sendPoses = document.getElementById("sendSoundid").checked
    initPoseNet()

}

function initPoseNet() {
    sendSounds = document.getElementById("sendSoundid").checked
    sendPoses = document.getElementById("sendPosesid").checked
    var imageScaleFactorid = parseInt(document.getElementById("imageScaleFactorid").value)
    var outputStrideid = parseInt(document.getElementById("outputStrideid").value)
    var minConfidenceid = parseInt(document.getElementById("minConfidenceid").value)
    var maxPoseDetectionsid = parseInt(document.getElementById("maxPoseDetectionsid").value)
    var scoreThresholdid = parseInt(document.getElementById("scoreThresholdid").value)
    var nmsRadiusid = parseInt(document.getElementById("nmsRadiusid").value)
    var multiplierid = parseInt(document.getElementById("multiplierid").value)
    var detectionTypeid = document.getElementById("detectionTypeid").value
     if (document.getElementById("flipHorizontalid").checked){
        flipHorizontalid = true
    } else {
        flipHorizontalid = false
    }

    let options = {
        imageScaleFactor: imageScaleFactorid,
        outputStride: outputStrideid,
        flipHorizontal: flipHorizontalid,
        minConfidence: minConfidenceid,
        maxPoseDetections: maxPoseDetectionsid,
        scoreThreshold: scoreThresholdid,
        nmsRadius: nmsRadiusid,
        detectionType: detectionTypeid,
        multiplier: multiplierid,
    }
    poseNet = ml5.poseNet(video);
    poseNet.on('pose', function (results) {
        poses = results;
    });
    video.hide();
}


function gotResult(error, results) {
    if (error) {
        console.error(error);
        return;
    }
    label = results.slice(0, 3)
}

function draw() {
    image(video, 0, 0, width, height);
    drawKeypoints();
    drawSkeleton();
}

function drawKeypoints() {
    for (let i = 0; i < poses.length; i++) {
        let pose = poses[i].pose;
        for (let j = 0; j < pose.keypoints.length; j++) {
            let keypoint = pose.keypoints[j];
            if (keypoint.score > 0.2) {
                fill(255, 0, 0);
                noStroke();
                ellipse(keypoint.position.x, keypoint.position.y, 10, 10);
            }
        }
    }
}

function drawSkeleton() {
    for (let i = 0; i < poses.length; i++) {
        let skeleton = poses[i].skeleton;
        for (let j = 0; j < skeleton.length; j++) {
            let partA = skeleton[j][0];
            let partB = skeleton[j][1];
            stroke(255, 0, 0);
            line(partA.position.x, partA.position.y, partB.position.x, partB.position.y);
        }
    }
}