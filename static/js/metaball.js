class Metaball {
	constructor() {
		const size = Math.pow(Math.random(), 2);
		this.vel = p5.Vector.random2D().mult(1 + (1 - size)/ 8);
		this.radius = 40 * size + 20;
		
		this.pos = new p5.Vector(width / 2, height / 2);
	}
	
	update() {
		this.pos.add(this.vel);
		
		if (this.pos.x < this.radius || this.pos.x > width  - this.radius) this.vel.x *= -1;
		if (this.pos.y < this.radius || this.pos.y > height - this.radius) this.vel.y *= -1;
	}
}