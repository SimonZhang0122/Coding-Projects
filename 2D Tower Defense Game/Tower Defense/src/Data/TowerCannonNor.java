package Data;

import java.util.concurrent.CopyOnWriteArrayList;

public class TowerCannonNor extends Tower {

	public TowerCannonNor(TowerType type, Tile startTile, CopyOnWriteArrayList<Enemy> enemies) {
		super(type, startTile, enemies);
	}

	@Override
	public void shoot(Enemy target) {
		super.projectiles.add(
				new ProjectileCannonball(super.type.projectileType, super.target, super.getX(), super.getY(), 32, 32));
	}
}
