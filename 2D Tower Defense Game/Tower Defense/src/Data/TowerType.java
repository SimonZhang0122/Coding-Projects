package Data;

import org.newdawn.slick.opengl.Texture;
import static Helper.Translator.*;

public enum TowerType {

	CannonRed(new Texture[] { QuickLoad("CannonBase"), QuickLoad("CannonGun") }, ProjectileType.CannonBall, 5, 850, 1,
			15), // standard cannon
	CannonIce(new Texture[] { QuickLoad("CannonBase"), QuickLoad("CannonGun2") }, ProjectileType.IceBall, 2, 1000, 1,
			20);// cannon that creates projectiles that slows down enemies

	Texture[] textures;
	ProjectileType projectileType;
	int damage, range, cost;
	float firingSpeed;

	TowerType(Texture[] textures, ProjectileType projectileType, int damage, int range, float firingSpeed, int cost) {
		this.textures = textures;
		this.projectileType = projectileType;
		this.damage = damage;
		this.range = range;
		this.firingSpeed = firingSpeed;
		this.cost = cost;
	}
}
