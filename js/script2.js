import * as posenet from '@tensorflow-models/posenet';
const imageScaleFactor = 0.50;
const flipHorizontal = false;
const outputStride = 16;
const imageElement = document.getElementById('cat');

const net = await posenet.load();

const pose = await net.estimateSinglePose(imageElement, scaleFactor, flipHorizontal, outputStride);
console.log(pose)