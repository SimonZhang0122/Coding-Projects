package Data;

import static Helper.Clock.Delta;
import static Helper.Translator.DrawQuadTex;
import static Helper.Translator.DrawQuadTexRot;

import java.util.ArrayList;
import java.util.concurrent.CopyOnWriteArrayList;

import org.newdawn.slick.opengl.Texture;

public abstract class Tower implements Entity {

	private float x, y, timeSinceLastShot, firingSpeed, angle;
	private int width, height, damage, range, cost;
	public Enemy target;
	private Texture[] textures;
	private CopyOnWriteArrayList<Enemy> enemies;
	private boolean targeted;
	public ArrayList<Projectile> projectiles;
	public TowerType type;

	public Tower(TowerType type, Tile startTile, CopyOnWriteArrayList<Enemy> enemies) {// constructor for all cannon
																						// towers
		this.type = type;
		this.textures = type.textures;
		this.damage = type.damage;
		this.range = type.range;
		this.cost = type.cost;
		this.x = startTile.getX();
		this.y = startTile.getY();
		this.width = startTile.getWidth();
		this.height = startTile.getHeight();
		this.enemies = enemies;
		this.targeted = false;
		this.timeSinceLastShot = 0f;
		this.projectiles = new ArrayList<Projectile>();
		this.firingSpeed = type.firingSpeed;
		this.angle = 0f;
	}

	private Enemy acquireTarget() {
		Enemy closest = null;
		float closestDistance = 384;// range to target enemy
		for (Enemy e : enemies) {
			if (isInRange(e) && findDistance(e) < closestDistance && e.isAlive()) {// target enemy within targeting
																					// range and alive
				closestDistance = findDistance(e);
				closest = e;
			}
		}
		if (closest != null)
			targeted = true;
		return closest;
	}

	private boolean isInRange(Enemy e) {
		float xDistance = Math.abs(e.getX() - x);
		float yDistance = Math.abs(e.getY() - y);
		if (xDistance < range && yDistance < range)// check if the enemy is within the range
			return true;
		return false;
	}

	private float findDistance(Enemy e) {
		float xDistance = Math.abs(e.getX() - x);
		float yDistance = Math.abs(e.getY() - y);
		return xDistance + yDistance; // returns the total amount of pixels from enemy to cannon tower
	}

	private float calculateAngle() {
		double angleTemp = Math.atan2(target.getY() - y, target.getX() - x);// uses tangent to calculate the angle from
																			// the cannon to the target enemy
		return (float) Math.toDegrees(angleTemp) - 90;// changes the angle to degrees and set it left 90 degrees

	}

	public abstract void shoot(Enemy target);// every different type of tower must have their own type of shoot method

	public void updateEnemyList(CopyOnWriteArrayList<Enemy> newList) {
		enemies = newList;
	}

	public void update() {
		if (!targeted) {
			target = acquireTarget(); // if not targeted, lock onto another target
		} else {
			angle = calculateAngle();
			if (timeSinceLastShot > firingSpeed) {// makes the cannon shoot again after one cannonball is shot
				shoot(target);
				timeSinceLastShot = 0;
			}
		}

		if (target == null || target.isAlive() == false)// disable targeting when target dies
			targeted = false;

		timeSinceLastShot += Delta();

		for (Projectile p : projectiles)
			p.update();

		draw();
	}

	public void draw() {
		DrawQuadTex(textures[0], x, y, width, height);// add texture but not rotation to first texture
		if (textures.length > 1)
			for (int i = 0; i < textures.length; i++)
				DrawQuadTexRot(textures[i], x, y, width, height, angle);// add rotatable texture to second texture on
																		// top of non rotation texture
	}

	public float getX() {
		return x;
	}

	public float getY() {
		return y;
	}

	public int getWidth() {
		return width;
	}

	public int getHeight() {
		return height;
	}

	public void setX(float x) {
		this.x = x;
	}

	public void setY(float y) {
		this.y = y;
	}

	public void setWidth(int width) {
		this.width = width;
	}

	public void setHeight(int height) {
		this.height = height;
	}

	public Enemy getTarget() {
		return target;
	}

	public int getCost() {
		return cost;
	}
}
