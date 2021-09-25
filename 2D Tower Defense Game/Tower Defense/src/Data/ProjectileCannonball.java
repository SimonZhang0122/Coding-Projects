package Data;

public class ProjectileCannonball extends Projectile {// creates normal cannon balls

	public ProjectileCannonball(ProjectileType type, Enemy target, float x, float y, int width, int height) {
		super(type, target, x, y, width, height);

	}

	@Override
	public void damage() {
		// super.getTarget().setSpeed(4f);
		super.damage();
	}
}
