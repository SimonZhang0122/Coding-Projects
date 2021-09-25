package Data;

public class ProjectileIceBall extends Projectile {// creates ice balls that can slow down enemies

	public ProjectileIceBall(ProjectileType type, Enemy target, float x, float y, int width, int height) {
		super(type, target, x, y, width, height);

	}

	@Override
	public void damage() {
		super.getTarget().setSpeed(50f);// this slows the enemies down
		super.damage();
	}
}
