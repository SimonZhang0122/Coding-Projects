package Data;

import org.newdawn.slick.opengl.Texture;
import static Helper.Translator.*;
import static Helper.Clock.*;
import java.util.ArrayList;
import java.util.concurrent.CopyOnWriteArrayList;

public class TowerCannon {

	private float x, y, timeSinceLastShot, firingSpeed, angle;
	private int width, height, damage, range;
	private Texture baseTexture, cannonTexture;
	private Tile startTile;
	private ArrayList<Projectile> projectiles;
	private CopyOnWriteArrayList<Enemy> enemies;
	private Enemy target;// the enemy the cannon locks onto
	private boolean targeted;

	public TowerCannon(Texture baseTexture, Tile startTile, int damage, int range,
			CopyOnWriteArrayList<Enemy> enemies) {
		this.baseTexture = baseTexture;
		this.cannonTexture = QuickLoad("CannonGun");
		this.startTile = startTile;
		this.x = startTile.getX();
		this.y = startTile.getY();
		this.width = (int) startTile.getWidth();
		this.height = (int) startTile.getHeight();
		this.damage = damage;
		this.range = range;
		this.firingSpeed = 3;
		this.timeSinceLastShot = 0;
		this.projectiles = new ArrayList<Projectile>();
		this.enemies = enemies;
		this.targeted = false;
	}

	private Enemy acquireTarget() {
		Enemy closest = null;
		float closestDistance = 10000;
		for (Enemy e : enemies) {
			if (isInRange(e) && findDistance(e) < closestDistance) {// target enemy within 10000 pixels of range
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

	private float calculateAngle() {// method to calculate the angle the cannon gun needs to be to aim at enemies
		double angleTemp = Math.atan2(target.getY() - y, target.getX() - x);// uses tangent to calculate the angle from
																			// the cannon to the target enemy
		return (float) Math.toDegrees(angleTemp) - 90;// changes the angle to degrees and set it left 90 degrees

	}

	private void shoot() {
		timeSinceLastShot = 0;
//		projectiles.add(new ProjectileIceBall(QuickLoad("Cannonball64 texture"), target, x + TILE_SIZE / 2 - TILE_SIZE / 4,
//				y + TILE_SIZE / 2 - TILE_SIZE / 4, 32, 32, 900, 5));// creates a cannonball on the map
	}

	public void updateEnemyList(CopyOnWriteArrayList<Enemy> newList) {
		enemies = newList;
	}

	public void update() {
		if (!targeted) {
			target = acquireTarget(); // if not targeted, lock onto another target
		}

		if (target == null || target.isAlive() == false)
			targeted = false;

		timeSinceLastShot += Delta();
		if (timeSinceLastShot > firingSpeed) // makes the cannon shoot again after one cannonball is shot
			shoot();

		for (Projectile p : projectiles)
			p.update();
		angle = calculateAngle();// follows and contiune to aim at enemy everytime it updates
		draw();
	}

	public void draw() {// creates cannon texture
		DrawQuadTex(baseTexture, x, y, width, height);
		DrawQuadTexRot(cannonTexture, x, y, width, height, angle);
	}
}