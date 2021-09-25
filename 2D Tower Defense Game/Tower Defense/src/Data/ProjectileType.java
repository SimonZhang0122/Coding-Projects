package Data;

import org.newdawn.slick.opengl.Texture;
import static Helper.Translator.*;

public enum ProjectileType {

	CannonBall(QuickLoad("CannonBall64 texture"), 5, 800), // this creates a cannon ball with damage and bullet speed
	IceBall(QuickLoad("IceBall"), 3, 900);// this creates a ice ball with damage and bullet speed

	Texture texture;
	int damage;
	float speed;

	ProjectileType(Texture texture, int damage, float speed) {
		this.texture = texture;
		this.damage = damage;
		this.speed = speed;
	}
}
