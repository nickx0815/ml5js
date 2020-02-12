// Copyright (c) 2019 ml5
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

/* ===
ml5 Example
PoseNet example using p5.js
=== */



let soundModel = 'https://teachablemachine.withgoogle.com/models/SK49Tmvw/';
let video;
let poseNet;
let poses = [];
let classifier;

// let option = {
//   imageScaleFactor: 0.3,
//   outputStride: 16,
//   flipHorizontal: false,
//   minConfidence: 0.5,
//   maxPoseDetections: 1,
//   scoreThreshold: 0.5,
//   nmsRadius: 20,
//   detectionType: 'single',
//   multiplier: 0.75,
//  }

function setup() {
  frameRate(24);
  createCanvas(640, 480);
  classifier = ml5.soundClassifier(soundModel + 'model.json');
  classifier.classify(gotResult);
  video = createCapture(VIDEO);
  video.size(width, height);

  // Create a new poseNet method with a single detection
  poseNet = ml5.poseNet(video, modelReady);
  // This sets up an event that fills the global variable "poses"
  // with an array every time new poses are detected
  poseNet.on('pose', function(results) {
    poses = results;

  });
  // Hide the video element, and just show the canvas
  video.hide();
}

function modelReady() {
  select('#status').html('Model Loaded');
}

function gotResult(error, results) {
  if (error) {
    console.error(error);
    return;
  }
  // The results are in an array ordered by confidence.
  // console.log(results[0]);
  label = results.slice(0,3)
}

function draw() {
  image(video, 0, 0, width, height);

  drawKeypoints();
  drawSkeleton();

}

// A function to draw ellipses over the detected keypoints
function drawKeypoints(){
  // Loop through all the poses detected
  for (let i = 0; i < poses.length; i++) {
    // For each pose detected, loop through all the keypoints
    let pose = poses[i].pose;
    for (let j = 0; j < pose.keypoints.length; j++) {
      // A keypoint is an object describing a body part (like rightArm or leftShoulder)
      let keypoint = pose.keypoints[j];
      // Only draw an ellipse is the pose probability is bigger than 0.2
      if (keypoint.score > 0.2) {
        fill(255, 0, 0);
        noStroke();
        ellipse(keypoint.position.x, keypoint.position.y, 10, 10);
        //ellipse(100,0,10,10)
        //console.log(keypoint.position.x, keypoint.position.y);
      }
    }
  }
}

// A function to draw the skeletons
function drawSkeleton() {
  // Loop through all the skeletons detected
  for (let i = 0; i < poses.length; i++) {
    let skeleton = poses[i].skeleton;
    // For every skeleton, loop through all body connections
    for (let j = 0; j < skeleton.length; j++) {
      let partA = skeleton[j][0];
      let partB = skeleton[j][1];
      stroke(255, 0, 0);
      line(partA.position.x, partA.position.y, partB.position.x, partB.position.y);
    }
  }
}
