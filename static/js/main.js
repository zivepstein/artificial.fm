let metaballShader;

const N_balls = 20,
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
}

// OpenProcessing has a bug where it always creates a scrollbar on Chromium.
function mouseWheel() { // This stops the canvas from scrolling by a few pixels.
	return false;
}