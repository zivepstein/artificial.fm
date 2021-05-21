let metaballShader;

const N_balls = 60,
			metaballs = [];

function preload() {
	metaballShader = getShader(this._renderer);
}

function setup() {
	createCanvas(windowWidth, windowHeight, WEBGL);
	shader(metaballShader);
	
	for (let i = 0; i < N_balls; i ++) metaballs.push(new Metaball());
}

function draw() {
	var data = [];

	
	for (const ball of metaballs) {
		ball.update();
		data.push(ball.pos.x, ball.pos.y, ball.radius);
	}
	
	metaballShader.setUniform("metaballs", data);

	rect(0, 0, width, height);
	stroke(200);
	line(0, 0, width, height);
	stroke(100);
	
}

// OpenProcessing has a bug where it always creates a scrollbar on Chromium.
function mouseWheel() { // This stops the canvas from scrolling by a few pixels.
	return false;
}